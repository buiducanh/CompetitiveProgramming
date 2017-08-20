def histogram(a):
    l = [0 for i in xrange(len(a))]
    r = [len(a)-1 for i in xrange(len(a))]
    for i in range(1, len(a)):
        if a[i] > a[i-1]:
            l[i] = i-1
        else:
            l[i] = l[i-1]
            while l[i] != 0 and a[i] <= a[l[i]]:
                l[i] = l[l[i]]
    for i in range(len(a)-2, -1, -1):
        if a[i] > a[i+1]:
            r[i] = i+1
        else:
            r[i] = r[i+1]
            while r[i] != len(a)-1  and a[i] <= a[r[i]]:
                r[i] = r[r[i]]
    max = 0
    for i in range(1, len(a) - 2):
        area = (r[i] - l[i] - 1)*a[i]
        if max < area:
            max = area
    return max

def solve(m, n, a):
    ones = [[0 for j in xrange(n+2)] for i in xrange(m)] 
    for i in xrange(m):
        for j in xrange(n):
            if a[i][j] == 1:
                if i == 0:
                    ones[i][j+1] = 1
                else:
                    ones[i][j+1] = ones[i-1][j+1] + 1
    max = 0
    for i in xrange(m):
        area = histogram(ones[i])
        if max < area:
            max = area
    return max
    
inp = open("qbrect.in", "r")
m, n = map(int, inp.readline().strip().split())
a = []
for i in xrange(m):
   a.append(map(int, inp.readline().strip().split()))
print solve(m, n, a)
