import math 
def solve(a):
    l = [0 for i in a]
    r = [len(a) - 1 for i in a]
    for i in range(1, len(a)):
        if a[i] <= a[i-1]:
            l[i] = l[i-1]
            while l[i] != 0 and a[i] <= a[l[i]]:
                l[i] = l[l[i]]
        else:
            l[i] = i-1
    for i in range(len(a) - 2, -1, -1):
        if a[i] <= a[i+1]:
            r[i] = r[i+1]
            while r[i] != len(a) - 1 and a[i] <= a[r[i]]:
                r[i] = r[r[i]]
        else:
            r[i] = i+1
    res = 0
    for id,i in enumerate(a):
        area = (r[id] - l[id] - 1) * i
        if res < area:
            res = area
    print l, r
    return res

inp = open("histogram.in", "r")
a = [0]
a = a + map(int, inp.readline().split())
a.append(0)
print solve(a)
