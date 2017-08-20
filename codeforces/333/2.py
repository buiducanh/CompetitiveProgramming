def longest(m):
    if len(m) <= 1:
        return len(m)
    min = m[0]
    max = m[0]
    count = 1
    mm = [1 for i in m]
    result = 1
    for idx, _ in enumerate(m):
        if idx == 0:
            continue
        if m[idx] == m[idx - 1]:
            mm[idx] = mm[idx-1] + 1
            mm[idx - 1] = 0
    for idx, num in enumerate(m[1:]):
        # print count, result, idx + 1, max, min
        if abs(min - num) == 2 or abs(max - num) == 2:
            count = 1 + mm[idx]
            if count > result:
                result = count
            if num > m[idx]:
                max = num
                min = m[idx]
            else:
                max = m[idx]
                min = num
        else:
            if min > num:
                min = num
            if max < num:
                max = num
            count += 1
            if count > result:
                result = count
    return result    

from sys import stdin
#inp = open("in", "r")
inp = stdin
n = int(inp.readline().strip())
if n > 1:
    m = map(int, inp.readline().strip().split())
    print longest(m[:n])
else:
    print n 
