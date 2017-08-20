from sys import stdin
from collections import deque
'''class Node:
    def __init__(self, val, link):
        self.
class deque:
    q = []
    def '''

kx = [1, 0, -1, 0]
ky = [0, 1, 0, -1]
def fourDirection(x, y):
    for i in xrange(len(kx)):
        newx = x + kx[i]
        newy = y + ky[i]
        yield(newx, newy)

def withinBound(x, y, n, m):
    if x < 0 or x >= n:
        return False
    if y < 0 or y >= m:
        return False
    return True


def solve(a, n, m, minh, h):
    result = 0
    count = 0
    max = [[0 for x in xrange(m)] for y in xrange(n)]
    for hgt in range(h, minh -1 , -1):
        fill = [[0 for x in xrange(m)] for y in xrange(n)]
        for i in xrange(n):
            for j in xrange(m):
                if a[i][j] >= hgt:
                    fill[i][j] = 0
                else:
                    fill[i][j] = hgt - a[i][j]
        '''for i in fill:
            print
            for j in i:
                print(j)'''
        # stdin.readline()
        q = deque()
        for i in xrange(n):
            if fill[i][0] != 0:
                q.append((i,0))
            if fill[i][m-1] != 0:
                q.append((i,m-1))
        for i in xrange(m):
            if fill[0][i] != 0:
                q.append((0,i))
            if fill[n-1][i] != 0:
                q.append((n-1,i))
        while q:
            x, y = q.popleft()
            if fill[x][y] == 0:
                continue
            fill[x][y] = 0
            for newx, newy in fourDirection(x, y):
                if withinBound(newx, newy, n, m):
                    if fill[newx][newy] != 0:
                        q.append((newx, newy))
        volume = 0
        for idx, i in enumerate(fill):
            for idy, j in enumerate(i):
                if max[idx][idy] < j:
                    max[idx][idy] = j
    for i in max:
        for j in i:
            result += j 
    return result

'''import random
n = 100
m = 100
wr = open("pbcwater.txt","w")
wr.write(str(n)+" "+str(m)+"\n")
for i in range(0,m):
    for j in range(0,n):
        x = random.randrange(1,1000)
        wr.write(str(x)+" ")
    wr.write("\n")
wr.close()'''
# inp = open("pbcwater.txt", "r")
inp = stdin
n, m = map(int, inp.readline().split())
a = []
for i in xrange(n):
    row = map(int, inp.readline().split())
    a.append(row)
max = 0
min = 1000
for i in a:
    for j in i:
        if max < j:
            max = j
        if min > j:
            min = j
print solve(a, n, m, min, max)
inp.close()
