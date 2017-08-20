import sys
kx = [0, -1, 0, 1, 1, 1, -1, -1]
ky = [1, 0, -1, 0, 1, -1, 1, -1]

def fourDirection(x, y, n, m):
    for i in xrange(len(kx)):
        newx = x + kx[i]
        newy = y + ky[i]
        if newx < 0 or newx >= n: continue
        if newy < 0 or newy >= m: continue
        yield (newx, newy)

def isBasin(x, y, m):
    for newx, newy in fourDirection(x,y, len(m), len(m[0])):
        if m[newx][newy] < m[x][y]:
            return False
    return True

def isFloodable(ox, oy, x, y, m):
    for newx, newy in fourDirection(x,y, len(m), len(m[0])):
        if m[newx][newy] <= m[ox][oy] and not (newx == ox and newy == oy):
            return False
    return True

def flood_fill(x, y, m, mark, basin):
    if mark[x][y] != 0: return 
    mark[x][y] = basin
    for newx, newy in fourDirection(x, y, len(m), len(m[0])):
        if newx == 2 and newy == 2:
            print m[x][y], m[newx][newy], newx, newy,\
                x, y, isFloodable(x, y, newx, newy, m)
        if mark[newx][newy] == 0 and m[newx][newy] >= m[x][y] and \
        (isFloodable(x, y, newx, newy, m)):
            flood_fill(newx, newy, m, mark, basin)


def find_max_basin(m):
    mark = [[0 for x in m[0]] for y in m]
    basin = 0 
    for idx, row in enumerate(m):
        for idy, val in enumerate(row):
            if isBasin(idx, idy, m) and mark[idx][idy] == 0:
                basin += 1
                flood_fill(idx, idy, m, mark, basin) 
    for row in mark:
        print 
        for val in row:
            print val,

inp = open("in.txt", "r")
m = []
l = int(inp.readline())
for i in xrange(l):
    row = map(int, inp.readline().split(" "))
    m.append(row)

for row in m:
    print 
    for val in row:
        print val,
print 
find_max_basin(m)
