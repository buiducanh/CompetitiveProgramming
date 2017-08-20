def weight(n, a):
    count = [0 for i in xrange(1 << 20)]
    max = 0
    for i in a:
       count[i] += 1 
       if i > max:
           max = i
    res = 0
    for i in range(0, max + 30):
        while count[i] > 1:
            count[i] -= 2
            count[i+1] += 1
        if count[i] == 1:
            res += 1
    return res

from sys import stdin
# inp = open("3.in", "r")
inp = stdin
n = int(inp.readline().strip())
a = map(int, inp.readline().strip().split())
print weight(n, a)
