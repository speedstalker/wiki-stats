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
            self._sizes = array.array('L', [0]*self._n)
            self._links = array.array('L', [0]*self._nlinks)
            self._redirect = array.array('B', [0]*self._n)
            self._offset = array.array('L', [0]*(self._n+1))

            for i in range(self._n):
                title = f.readline()
                titledesc = f.readline().split()

                self._titles.append(title.strip())

                self._sizes[i]    = int(titledesc[0])
                self._redirect[i] = int(titledesc[1])
                self._offset[i+1] = self._offset[i] + int(titledesc[2])
                for j in range(self._offset[i], self._offset[i+1]):
                    self._links.append(int(f.readline()))

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


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл
