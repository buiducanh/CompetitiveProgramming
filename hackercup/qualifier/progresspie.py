mid = (50, 50)
eps = .000001
r = 50
def comp(x, y):
    if abs(x*1.0 - y) < eps:
        return 0
    return 1 if x > y else -1

from math import acos
from math import sqrt
from math import pi

def lengthAB(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def length(v):
    return sqrt(v[0]**2+v[1]**2)

def dot_product(v,w):
   return v[0]*w[0]+v[1]*w[1]

def determinant(v,w):
   return v[0]*w[1]-v[1]*w[0]

def inner_angle(v,w):
   cosx=dot_product(v,w)/(length(v)*length(w))
   rad=acos(cosx) # in radians
   return rad*180/pi # returns degrees

def angle_clockwise(A, B):
    inner=inner_angle(A,B)
    det = determinant(A,B)
    if det <= 0: #this is a property of the det. If the det < 0 then B is clockwise of A
        return inner
    else: # if the det > 0 then A is immediately clockwise of B
        return 360-inner


def query(p, a):
    if p == 0:
        return False

    dist = lengthAB(mid, a)
    if comp(r, dist) == -1:
        return False

    angle = angle_clockwise((0, 50), (a[0] - 50, a[1] - 50))
    if comp(angle*100.0 / 360, p) == 1:
        return False
    return True



from sys import stdin
inp = stdin
t = int(inp.readline().strip())

for i in range(t):
    p, x, y = map(int, inp.readline().strip().split())
    if query(p, (x, y)):
        res = 'black'
    else:
        res = 'white'
    print("Case #{}: {}".format(str(i + 1), res))

