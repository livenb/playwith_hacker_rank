def land_input():
    m, n = [int(x) for x in raw_input().split()]
    land = []
    for _ in xrange(m):
        land.append([True if x == 'x' else False for x in raw_input()])
    return land, m, n


def get_left_mat(land, m, n):
    mat = []
    for i in xrange(m):
        curr = 0
        row = []
        for j in xrange(n):
            if land[i][j]:
                row.append(-1)
                curr = 0
            else:
                row.append(curr)
                curr += 1
        mat.append(row)
    return mat


def get_upper_mat(land, m, n):
    land_trans = map(list, zip(*land))
    mat_trans = get_left_mat(land_trans, n, m)
    mat = map(list, zip(*mat_trans))
    return mat


def search_perimeter(land, left_mat, upper_mat, m, n):
    res = 0
    for i in xrange(1, m+1):
        for j in xrange(1, n+1):
            if not land[-i][-j]:
                left = left_mat[-i][-j]
                upper = upper_mat[-i][-j]
                if res < 2*(left+upper):
                    for k in reversed(xrange(1, left+1)):
                        for p in reversed(xrange(1, upper+1)):
                            if res < 2*(k+p):
                                if (not land[-i-p][-j-k]) and\
                                  (upper_mat[-i][-j-k] >= p) and\
                                  (left_mat[-i-p][-j] >= k):
                                    temp = 2*(k+p)
                                    res = max(res, temp)
                                    if res == 2 * (m+n-2):
                                        return res
    if res == 0:
        return 'impossible'
    else:
        return res


land, m, n = land_input()
left_mat = get_left_mat(land, m, n)
upper_mat = get_upper_mat(land, m, n)
res = search_perimeter(land, left_mat, upper_mat, m, n)
print res
