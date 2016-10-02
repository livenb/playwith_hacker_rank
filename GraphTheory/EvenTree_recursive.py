# Enter your code here. Read input from STDIN. Print output to STDOUT
def build_tree(m):
    tree = {}
    for i in xrange(m):
        node1, node2 = [int(x) for x in raw_input().split()]
        if node2 not in tree:
            tree[node2] = set()
        tree[node2].add(node1)
        # print node1, node2
    return tree


def find_even_tree(node, my_tree):
    tree_node_number = 1
    cut_edge = 0
    sub_cut_edge = 0
    # print "my node", node
    if node in my_tree:
        for next_node in my_tree[node]:
            # print "my next node is " , next_node
            sub_tree_number, sub_cut_edge = find_even_tree(next_node, my_tree)
            if sub_tree_number % 2 == 0:  # even
                sub_cut_edge += 1
            else:
                tree_node_number += sub_tree_number
            cut_edge += sub_cut_edge
            # print "my cut_edge is" , cut_edge
    return tree_node_number, cut_edge


def main():
    n, m = [int(x) for x in raw_input().split()]
    my_tree = build_tree(m)
    number, cut_edge = find_even_tree(1, my_tree)
    print cut_edge

if __name__ == '__main__':
    main()
