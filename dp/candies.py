# Enter your code here. Read input from STDIN. Print output to STDOUT
def candies_update(r, prev, curr):
    if curr <= prev:
        r = 1 
    elif curr > prev:
        r += 1
    return r


def forward(n):
    r_lst = []
    arr = []
    for i in xrange(n):
        x = int(raw_input())
        arr.append(x)
        if i == 0:
            r = 1
            prev = x
        else:
            r = candies_update(r, prev, x)
            prev = x
        r_lst.append(r)
    return arr, r_lst


def back_check(arr, r_lst, n):
    for j in reversed(xrange(n)):
        if j != n-1:
            if arr[j] > arr[j+1] and r_lst[j] <= r_lst[j+1]:
                r_lst[j] = r_lst[j+1] + 1
    return sum(r_lst)


n = int(raw_input())
arr, r_lst = forward(n)
s = back_check(arr, r_lst, n)
print s
