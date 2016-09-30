# Enter your code here. Read input from STDIN. Print output to STDOUT
def build_graph(m):
    graph = {}
    for i in xrange(m):
        node1, node2 = [int(x) for x in raw_input().split()]
        # it is a undirected graph, hence bidirectional
        if node1 not in graph:
            graph[node1] = set()
        if node2 not in graph:
            graph[node2] = set()
        graph[node1].add(node2)
        graph[node2].add(node1)
    return graph


def BFS(graph, start, n):
    '''
    return a list of shortest length from start to each node
    '''
    visited = set()
    dist = [n*10 for i in xrange(n)]
    queue = []
    queue.append(start)
    dist[start-1] = 0
    while queue:
        node = queue.pop(0)
        d = dist[node-1]
        if node not in visited:
            visited.add(node)
            for adj in graph[node]:
                queue.append(adj)
                if d + 1 < dist[adj-1]:
                    dist[adj-1] = d + 1
    return dist


def main():
    queries = int(raw_input())
    for q in xrange(queries):
        n, m = [int(x) for x in raw_input().split()]
        graph = build_graph(m)
        start = int(raw_input())
        if start in graph:
            dist = BFS(graph, start, n)
            res = ''
            for i in xrange(n):
                if dist[i] == n*10:
                    res += str(-1) + ' '
                elif i == start - 1:
                    continue
                else:
                    res += str(dist[i] * 6) + ' '
            print res
        else:
            dist = [-1 for i in xrange(n-1)]
            print ' '.join(map(str, dist))


if __name__ == "__main__":
    main()
