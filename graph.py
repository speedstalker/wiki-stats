from wiki_stats import WikiGraph
import sys
import os

def bfs(wg, fromId, toId):
    # open_set   - nodes to be processed
    # closed_set - nodes that were processed
    # meta       - reverse graph
    open_set = list()
    closed_set = set()
    meta = dict()

    meta[fromId] = None
    open_set.append(fromId)

    while open_set:
        subtree_root = open_set.pop(0)

        if subtree_root == toId:
            return construct_path(fromId, toId, meta)

        for child in wg.get_links_from(subtree_root):
            if child in closed_set:
                continue

            if child not in open_set:
                meta[child] = subtree_root # create metadata for these nodes
                open_set.append(child)     # enqueue these nodes

        closed_set.add(subtree_root)

# Produce a backtrace of the actions taken to find the goal node, using the 
# recorded meta dictionary
def construct_path(fromId, toId, meta):
    action_list = [toId]
    state = toId
  
    # Continue until you reach root meta data
    while state != fromId:
        state = meta[state]
        action_list.append(state)
  
    action_list.reverse()
    return action_list


def find_way(wg, fromTitle, toTitle, used = []):
    fromId = wg.get_id(fromTitle)
    toId   = wg.get_id(toTitle)
    path = bfs(wg, fromId, toId)
    for link in path:
        print (wg.get_title(link), end =" -> ")

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if not os.path.isfile(sys.argv[1]):
        print('Файл с графом не найден')
        sys.exit(-1)

    wg = WikiGraph()
    wg.load_from_file(sys.argv[1])

    find_way(wg, "Python", "Список_файловых_систем")
