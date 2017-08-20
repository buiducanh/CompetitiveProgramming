import heapq

def lazyLoad(nums):
    nums = [-i for i in nums]
    heapq.heapify(nums)
    res = 0
    n = len(nums)
    while n > 0:
        item = abs(heapq.heappop(nums))
        need = 50 // item + (1 if 50 % item > 0 else 0)
        if n < need:
            break
        else:
            n -= need
        res += 1
    return res


from sys import stdin
inp = stdin

t = int(inp.readline().strip())

for i in range(t):
    n = int(inp.readline().strip())
    nums = []
    for j in range(n):
        nums.append(int(inp.readline().strip()))
    res = str(lazyLoad(nums))
    print "Case #{}: {}".format(str(i + 1), res)
