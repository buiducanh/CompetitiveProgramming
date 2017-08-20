# inp = open("1.in", "r")
import sys
from math import sqrt
inp = sys.stdin
xh, yh = map(int, inp.readline().split())
n = int(inp.readline().strip())
shortest_time = sys.maxint * 1.0
def dist(a, b, x, y):
    return sqrt(abs(a-x)*abs(a-x) + abs(b-y)*abs(b-y))
for i in range(n):
    x, y, v = map(int, inp.readline().split())
    distance = dist(xh,yh,x,y)
    shortest_time = min(shortest_time, distance/v)

print(shortest_time)
