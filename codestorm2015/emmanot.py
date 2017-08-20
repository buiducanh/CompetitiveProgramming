def count2(t):
    if t < 1:
        return 0
    res = 1
    for i in xrange(t - 1):
        res += (i + 4) / 2
    return res

def count(t):
    if t < 1:
        return 0
    elif t == 1:
        return 1
    elif t == 2:
        return 3
    res = 1
    t = t - 1
    tt = t / 2
    l = 2 
    r = tt + 1
    res = res + (r - l + 1) * ( l + r )
    if t % 2 == 0:  
        return res
    else:
        return res + r + 1


t = int(raw_input())
b = 0
for i in xrange(t):
    a = count(i)
    if i > 0:
        b += (i) / 2 + 1
    if a != b:
        print a, b
