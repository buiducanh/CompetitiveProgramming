def meat(n, a, p):
    min = 100
    res = 0
    for i in xrange(len(a)):
        if p[i] < min:
            min = p[i]
        res += a[i]*min
    return res
from sys import stdin
#inp = open("1.in", "r")
inp = stdin
n = int(inp.readline().strip())
a = []
p = []
for i in xrange(n):
    x, y = map(int, inp.readline().strip().split())
    a.append(x)
    p.append(y)

print meat(n, a, p)
