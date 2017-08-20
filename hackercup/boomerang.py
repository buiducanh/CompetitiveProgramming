from math import sqrt
import random
eps = 0.0000001
def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0
def compareFloat(a, b):
    if abs(a - b) < eps:
        return 0
    if a > b:
        return 1
    else:
        return -1

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, p):
        return sqrt((p.x - self.x)**2 + (p.y - self.y)**2)

def qsort(dist, l, r):
    i = l
    j = r
    pivot = dist[random.randint(0, r)]
    while True:
        while (i < len(dist)) and (compareFloat(dist[i], pivot) == -1):
            i += 1
        while (j > 0) and (compareFloat(dist[j], pivot) == 1):
            j -= 1
        if i <= j:
            if i < j:
                tmp = dist[i]
                dist[i] = dist[j]
                dist[j] = tmp
            i += 1
            j -= 1
        if i > j:
            break
    if l < j:
        qsort(dist, l, j)
    if i < r:
        qsort(dist, i, r)


def boomerang(n, ps):
    result = 0
    pdist = [[] for i in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = ps[i].distance(ps[j])
            pdist[i].append(d)
            pdist[j].append(d)
    for i in range(n):
        pdist[i].sort()
        dp = [0 for j in range(n - 1)]
        for j in range(1, n - 1):
            if compareFloat(pdist[i][j], pdist[i][j - 1]) == 0:
                dp[j] = dp[j - 1] + 1
            if j + 1 == n - 1 or compareFloat(pdist[i][j], pdist[i][j + 1]) != 0:
                result += choose(dp[j] + 1, 2)
    return result

def boomerang1(n, ps):
    result = 0
    pdist = [{} for i in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = "{0:.7f}".format(ps[i].distance(ps[j]))
            if not d in pdist[i]:
                pdist[i][d] = 1
            else:
                pdist[i][d] += 1
            if not d in pdist[j]:
                pdist[j][d] = 1
            else:
                pdist[j][d] += 1
    for distl in pdist:
        for key, val in distl.items():
            result += choose(val, 2)
    return result

inp = open('boomerang_constellations.txt', 'r')
out = open('out.txt', 'w')
t = int(inp.readline().strip())
for i in range(t):
    n = int(inp.readline().strip())
    points = []
    for j in range(n):
        x, y = map(int, inp.readline().strip().split())
        points.append(Point(x, y))
    out.write("Case #{}: {}\n".format(i + 1, boomerang1(n, points)))
