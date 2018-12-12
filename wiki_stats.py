#!/usr/bin/python3

import os
import sys
import math

import array

import statistics

from matplotlib import rc
#rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename, encoding='utf8') as f:
            initdesc = f.readline().split()

            self._n = int(initdesc[0])
            self._nlinks = int(initdesc[1])

            self._titles = []
            self._max_size = -math.inf
            self._sizes = array.array('L', [0]*self._n)
            self._links = array.array('L', [0]*self._nlinks)
            self._redirect = array.array('B', [0]*self._n)
            self._offset = array.array('L', [0]*(self._n+1))

            for i in range(self._n):
                title = f.readline()
                titledesc = f.readline().split()

                self._titles.append(title.strip())

                self._sizes[i]    = int(titledesc[0])
                self._max_size    = max(self._max_size, self._sizes[i])
                self._redirect[i] = int(titledesc[1])
                self._offset[i+1] = self._offset[i] + int(titledesc[2])
                for j in range(self._offset[i], self._offset[i+1]):
                    self._links[j] = int(f.readline())

        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return self._offset[_id + 1] - self._offset[_id]

    def get_links_from(self, _id):
        return self._links[self._offset[_id]:self._offset[_id + 1]]

    def get_id(self, title):
        return self._titles.index(title)

    def get_number_of_pages(self):
        return self._n

    def is_redirect(self, _id):
        return self._redirect[_id]

    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._pagesize[_id]

    def draw_images(self):
        self.hist_links_from()
        self.hist_links_to()
        self.hist_redirects()
        self.hist_sizes()

    def hist_links_from(self, fname="links_from.png"):
        nlinks = array.array('L', [0] * self.get_number_of_pages())
        for i in range(self.get_number_of_pages()):
            nlinks[i] = self.get_number_of_links_from(i)
        hist(fname, nlinks, 200, "Количество статей", "Количество ссылок",
             "Распределение количества ссылок из статьи")

    def hist_links_to(self, fname="links_to.png"):
        nlinks = array.array('L', [0] * self.get_number_of_pages())
        for i in range(self.get_number_of_pages()):
            nlinks[self._links[i]] += 1
        hist(fname, nlinks, 200, "Количество статей", "Количество ссылок",
             "Распределение количества ссылок на статью")

    def hist_redirects(self, fname="redirects.png"):
        nredirects = array.array('L', [0] * self.get_number_of_pages())
        for i in range(self.get_number_of_pages()):
            if self.is_redirect(i):
                nredirects[self._links[self._offset[i]]] += 1
        hist(fname, nredirects, 20, "Количество статей", "Количество ссылок",
             "Распределение количества перенаправлений на статью")

    def hist_sizes(self, fname="sizes.png"):
        hist(fname, self._sizes, 100, "Количество статей", "Размер статьи",
             "Распределение размеров статей")


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green',
         alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    plt.hist(data, bins, facecolor=facecolor, alpha=alpha,
             edgecolor='black', linewidth=0.3)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)

    # plt.show()
    if not os.path.exists("img"):
        os.makedirs("img")
    plt.savefig(os.path.join("img", fname))
