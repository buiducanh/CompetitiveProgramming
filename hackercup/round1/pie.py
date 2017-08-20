from sys import stdin
inp = stdin
inp = open("pie_progress.txt", "r")

import heapq
def buyPies(n, m, pies):
    for i in range(n):
        heapq.heapify(pies[i])
    pDays = [0 for i in range(n)]
    cost = 0
    for i in range(n):
        minCost = 1 << 31
        minDay = -1
        for j in range(i + 1):
            if not pies[j]:
                continue
            # account for change in tax
            newCost = - pDays[j]**2 + (pDays[j] + 1)**2
            # plus pie cost
            pieCost = pies[j][0]
            newCost += pieCost

            if newCost < minCost:
                minDay = j
                minCost = newCost
        heapq.heappop(pies[minDay])
        pDays[minDay] += 1
        cost += minCost
    return cost


t = int(inp.readline().strip())

for i in range(t):
    n, m = map(int, inp.readline().strip().split())
    pies = []
    for j in range(n):
        pies.append(list(map(int, inp.readline().strip().split())))
    print("Case #{}: {}".format(i + 1, buyPies(n, m, pies)))
