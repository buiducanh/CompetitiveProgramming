def sherlock(n, m):
    partsum = []
    sum = 0
    for i in m:
        sum += i
        partsum.append(sum)
    for i in range(n):
        leftsum = partsum[i] - m[i]
        rightsum = partsum[n-1] - partsum[i]
        if leftsum == rightsum:
            return "YES"
    return "NO"

from sys import stdin
#inp = open("in", "r")
inp = stdin
t = int(inp.readline().strip())
for i in range(t):
    n = int(inp.readline().strip())
    m = map(int, inp.readline().strip().split())
    print(sherlock(n,list(m)))
