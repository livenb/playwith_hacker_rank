mod = 1000000007
def hack_rank_city(A):
    sum_of_dist = 0
    dist_corner = 0
    num_node = 1
    diameter = 0
    for step in A:
        sum_of_dist = sum_of_dist * 4 + (num_node * 12 + 8) \
                        * (dist_corner + num_node * step) \
                        + (num_node * 2 + 1) ** 2 * step
        dist_corner = dist_corner * 4 + (diameter + step * 2) * num_node\
                        + (diameter + step * 3) * num_node * 2\
                        + diameter * 2 + step * 3
        num_node = num_node * 4 + 2
        diameter = diameter * 2 + step * 3
        sum_of_dist %= mod
        dist_corner %= mod
        num_node %= mod
        diameter %= mod
    return sum_of_dist

n = int(raw_input())
A = [int(x) for x in raw_input().split()]
res = hack_rank_city(A)
print res
