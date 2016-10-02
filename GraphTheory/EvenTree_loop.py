def build_tree(m):
    tree = {}
    for i in xrange(m):
        node1, node2 = [int(x) for x in raw_input().split()]
        if node2 not in tree:
            tree[node2] = set()
        tree[node2].add(node1)
        #print node1, node2
    return tree


def find_even_tree(my_tree, root):
    visited = set()
    parents = {root:[]}
    cut_edge = 0
    edge = 0
    queue = [root]
    while queue:
        node = queue.pop()
        if node not in visited:
             visited.add(node)
             queue.extend(my_tree[node])
             

def main():
    n, m = [int(x) for x in raw_input().split()]
    my_tree = build_tree(m)
    number, cut_edge = find_even_tree(my_tree, 1)
    print cut_edge


if __name__ == '__main__'
    main()
