def MandragoraForest(H, n):
    '''
    At each step, choose eat or battle
    depends on if the sum of S * H after this step larger than
    the sum of the current step
    (S+1) * sum(H[i+1]) < S * sum(H[i])
    '''
    H = sorted(H)
    s = 1
    p = 0
    H_sum = sum(H)
    for i in xrange(n):
        H_sum -= H[i]
        if H_sum > s * H[i]:
            s += 1
        else:
            p += H[i]*s
    return p

t = int(raw_input())
for _ in xrange(t):
    n = int(raw_input())
    H = [int(x) for x in raw_input().split()]
    p = MandragoraForest(H, n)
    print p
