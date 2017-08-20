from sys import stdin
def solve(a):
    map = {}
    result = 0
    for i in a:
        map[i] = 1
    for i in a:
        if not map[i]:
            continue
        count = 1
        l = i - 1
        r = i + 1
        while l in map:
            count += 1
            map[l] = None
            l -= 1
        while r in map:
            count += 1
            map[r] = None
            r += 1
        if count > result:
            result = count
    return result
a = map(int, stdin.readline().split())
print solve(a)
