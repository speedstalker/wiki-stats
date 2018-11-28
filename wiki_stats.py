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
            n = int(initdesc[0])
            _nlinks = int(initdesc[1])

            self._titles = []
            self._n = n
            self._sizes = array.array('L', [0]*n)
            self._links = array.array('L', [0]*_nlinks)
            self._redirect = array.array('B', [0]*n)
            self._offset = array.array('L', [0]*(n+1))

            for i in range(n):
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
        pass

    def get_links_from(self, _id):
        pass

    def get_id(self, title):
        pass

    def get_number_of_pages(self):
        pass

    def is_redirect(self, _id):
        pass

    def get_title(self, _id):
        pass

    def get_page_size(self, _id):
        pass


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
    else:
        print('Файл с графом не найден')
        sys.exit(-1)

    # TODO: статистика и гистограммы