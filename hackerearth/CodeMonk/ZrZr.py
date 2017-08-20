def sumBase(n, p):
    res = 0
    while n != 0:
        res += n % p
        n = n / p
    return res

def zrzr(n):
    fiveCount = (n - sumBase(n, 5)) / (5 - 1)
    a = 0
    return a + fiveCount

from sys import stdin
# inp = open("ZrZr.in", "r")
inp = stdin
test = int(inp.readline().strip())
for i in xrange(test):
    n = int(inp.readline().strip())
    print zrzr(n)
