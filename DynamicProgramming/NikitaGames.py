def NikitaGame(A):
    tot = sum(A)
    tar = tot/2
    n = len(A)
    if n == 0:
        return 0
    elif tot % 2 != 0:
        return 0
    elif tot == 0:
        return n - 1
    else:
        s, i = 0, 0
        while i < n and s != tar:
            s += A[i]
            i += 1
        if i >= n:
            return 0
        return 1 + max(NikitaGame(A[:i]), NikitaGame(A[i:]))

t = int(raw_input())
for _ in xrange(t):
    n = int(raw_input())
    A = [int(x) for x in raw_input().split()]
