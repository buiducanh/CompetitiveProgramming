def compare(x, bx, y, by):
    xx = 0
    for idx, i in enumerate(x):
        xx += i*(bx**idx)
    yy = 0
    for idx, i in enumerate(y):
        yy += i*(by**idx)
    if xx > yy:
        return '>'
    elif xx == yy:
        return '='
    else:
        return '<'
    

from sys import stdin
#inp = open("in", "r")
inp = stdin
nx, bx = map(int, inp.readline().strip().split())
x = map(int, inp.readline().strip().split())
ny, by = map(int, inp.readline().strip().split())
y = map(int, inp.readline().strip().split())
print(compare(list(reversed(x)), bx, list(reversed(y)), by))
