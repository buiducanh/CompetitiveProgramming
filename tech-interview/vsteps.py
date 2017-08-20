from sys import stdin
def solve(n, k, a):
    res = [0,1]
    b = 0
    for id, i in enumerate(a):
        if i > 1:
            b = id
            break
        
    for i in range(2,n+1):
        if a[b] != i:
            res.append((res[i-1] + res[i-2]) % 14062008)
        else:
            res.append(0)
            if b < len(a)-1: b += 1
    print res
    return res[n]

# inp = open("vsteps.in", "r")
inp = stdin
# test = int(inp.readline())
n, k = map(int, inp.readline().split())
a = [0]
if k > 0: a = map(int, inp.readline().split())
print solve(n, k, a)
