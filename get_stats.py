from wiki_stats import WikiGraph
import sys
import os
import array
import statistics


def get_redirect_percentage(wg):
    n = wg.get_number_of_pages()
    redirect_count = 0
    for id in range(0, n):
        if wg.is_redirect(id):
            redirect_count += 1

    return redirect_count/n


def get_array_stats(wg, arr):
    stats = dict()

    stats['avg']      = statistics.mean(arr)
    stats['maxval']   = max(arr)
    stats['maxcount'] = arr.count(stats['maxval'])
    maxindex          = arr.index(stats['maxval'])
    stats['maxtitle'] = wg.get_title(maxindex)
    
    stats['minval']   = min(arr)
    stats['mincount'] = arr.count(stats['minval'])
    minindex          = arr.index(stats['minval'])
    stats['mintitle'] = wg.get_title(minindex)

    return stats

def get_links_from_stats(wg):
    linksfrom = array.array('L', [wg.get_number_of_links_from(i) for i in range(wg.get_number_of_pages())])
    return get_array_stats(wg, linksfrom)

def get_links_to_stats(wg):
    linksto = array.array('L', [0]*wg.get_number_of_pages())
    for i in range(wg.get_number_of_pages()):
        if not wg.is_redirect(i):
            links = wg.get_links_from(i)
            for link in links:
                linksto[link] += 1

    return get_array_stats(wg, linksto)

def get_redirects_to_stats(wg):
    redirectsto = array.array('L', [0]*wg.get_number_of_pages())
    for i in range(wg.get_number_of_pages()):
        if wg.is_redirect(i):
            links = wg.get_links_from(i)
            for link in links:
                redirectsto[link] += 1

    return get_array_stats(wg, redirectsto)

def get_stats(wg):
    print("Redirect percentage: ", get_redirect_percentage(wg) * 100, "%\n")

    linksfrom   = get_links_from_stats(wg)
    linksto     = get_links_to_stats(wg)
    redirectsto = get_redirects_to_stats(wg)
    
    print("Количество статей с максимальным количеством внешних ссылок: ", linksfrom['maxcount'])
    print("Статья с наибольшим количеством внешних ссылок: ", linksfrom['maxtitle'])
    print("Среднее количество внешних ссылок на статью: ", linksto['avg'])
    print("Минимальное количество перенаправлений на статью: ", redirectsto['minval'])
    print("Количество статей с минимальным количеством внешних перенаправлений: ", redirectsto['mincount'])
    print("Максимальное количество перенаправлений на статью: ", redirectsto['maxval'])
    print("Количество статей с максимальным количеством внешних перенаправлений: ", redirectsto['maxcount'])
    print("Статья с наибольшим количеством внешних перенаправлений: ", redirectsto['maxtitle'])
    print("Среднее количество внешних перенаправлений на статью: ", redirectsto['avg'])

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: get_stats.py <файл с графом статей>')
        sys.exit(-1)

    if not os.path.isfile(sys.argv[1]):
        print('Файл с графом не найден')
        sys.exit(-1)

    wg = WikiGraph()
    wg.load_from_file(sys.argv[1])

    get_stats(wg)
