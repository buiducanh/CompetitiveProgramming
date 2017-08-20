from sys import stdin
inp = stdin#open('in.txt', 'r')

def lcutTree(l, r, k):
    ll = []
    rr =[]
    orgl, orgr = l, r
    while l != 0:
        ll.append(l % k)
        l //= k
    ll.reverse()
    while r != 0:
        rr.append(r % k)
        r //= k
    rr.reverse()
    firstP = min(len(ll), len(rr)) - 1
    if k**firstP < orgl:
        firstP += 1
    lastP = max(len(ll), len(rr)) - 1
    if firstP > lastP:
        yield -1
    for i in range(firstP, lastP + 1):
        yield k**i

l, r, k = map(int, inp.readline().strip().split())
for i in lcutTree(l, r, k):
    print i,
