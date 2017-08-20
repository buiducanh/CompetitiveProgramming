from math import sqrt
def distance(a, b):
    return sqrt((b[1] - a[1]) ** 2 + (a[0] - b[0]) ** 2)
n, x1, y1, x2, y2 = map(int, raw_input().strip().split())
#f1 = [0] * n
#f2 = [0] * n
r1 = 0
r2 = 0
coors = []
for i in range(n):
    x, y = map(int, raw_input().strip().split())
    coors.append((x, y))
    #f1[len(coors) - 1] = distance((x1, y1), (x , y))
    #f2[len(coors) - 1] = distance((x2, y2), (x , y))
    d1 = distance((x1, y1), (x, y))
    d2 = distance((x2, y2), (x, y))
    if d1 <= r1 or d2 <= r2:
        continue
    if d1**2 + r2**2 < d2**2 + r1**2:  
        r1 = d1
    else:
        r2 = d2

print(int(r1**2 + r2**2))
