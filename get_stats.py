from wiki_stats import WikiGraph
import sys
import os


def get_redirect_percentage(wg):
    n = wg.get_number_of_pages()
    redirect_count = 0
    for id in range(0, n):
        if wg.is_redirect(id):
            redirect_count += 1

    return redirect_count/n


def get_stats(wg):
    print("Redirect percentage: ", get_redirect_percentage(wg) * 100, "%\n")

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if not os.path.isfile(sys.argv[1]):
        print('Файл с графом не найден')
        sys.exit(-1)

    wg = WikiGraph()
    wg.load_from_file(sys.argv[1])

    get_stats(wg)

