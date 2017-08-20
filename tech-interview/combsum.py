def combsum2(c, t):
    c.append(-1)
    c = [c[i] for i in range(len(c)) if c[i] != c[i+1]]
    dp = []

def combsum(c, res, sum, i, t):
    if t == 0:
        res.append(sum[:])
        return
    next = 1
    while i + next < len(c) and c[i] == c[i + next]:
        next += 1
    if i == len(c):
        return
    count = 0
    combsum(c, res, sum, i + next, t)
    while t - (count) * c[i] >= c[i]:
        sum.append(c[i])
        count += 1
        combsum(c, res, sum, i + next, t - (count) * c[i])
    while count > 0:
        sum.pop()
        count -= 1

inp = open("combsum.in", "r")
c = map(int, inp.readline().strip().split())
t = int(inp.readline().strip())
res = []
combsum(c, res, [], 0, t)
print res
print combsum2(c, t)
