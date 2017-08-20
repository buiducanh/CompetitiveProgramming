from sys import stdin
inp = stdin
inp = open('manic_moving.txt', 'r')
inf = 1 << 31

def moveRC(k, g, tasks, cost, nextL, nextUL, loaded, cur):
    if nextL == k:
        while loaded > 0:
            ul = tasks[nextUL][1]
            cost += g[cur][ul]
            cur = ul
            nextUL += 1
            loaded -= 1
        if cost >= inf:
            cost = -1
    else:
        l = tasks[nextL][0]
        ul = tasks[nextUL][1]

        if loaded == 0:
            cost = moveRC(k, g, tasks, cost + g[cur][l], nextL + 1, nextUL, loaded + 1, l)
            cost += g[cur][l]
            cur = l
            nextL += 1
            loaded += 1

        elif loaded == 1:
            cost = min(moveRC(k, g, tasks, cost + g[cur][l], nextL + 1, nextUL, loaded + 1, l),
            moveRC(k, g, tasks, cost + g[cur][ul], nextL, nextUL + 1, loaded - 1, ul))

        else:
            cost = moveRC(k, g, tasks, cost + g[cur][ul], nextL, nextUL + 1, loaded - 1, ul)
    return cost

def move(n, m, k, g, tasks):
    for u in range(n):
        for i in range(n):
            for j in range(n):
                if g[i][j] > g[i][u] + g[u][j]:
                    g[i][j] = g[i][u] + g[u][j]
    # wall
    for i in range(n):
        g[i].append(inf)
    g.append([inf for i in range(n + 1)])
    tasks.append((n, n))

    return moveRC(k, g, tasks, 0, 0, 0, 0, 0)

    nextL  = 0
    nextUL = 0
    loaded = 0
    cost = 0
    cur = 0

    while nextL < k:
        l = tasks[nextL][0]
        ul = tasks[nextUL][1]

        if loaded == 0:
            load = True

        elif loaded == 1:
            ll = tasks[nextL + 1][0]
            ull = tasks[nextUL + 1][1]

            if (g[cur][ul] + min(g[l][ll], g[l][ull]) <
                    g[cur][l] + min(g[ul][l], g[ul][ull])):
                load = False
            else:
                load = True
        else:
            load = False

        if load:
            if g[cur][l] == inf:
                return -1
            cost += g[cur][l]
            cur = l
            nextL += 1
            loaded += 1
        else:
            if g[cur][ul] == inf:
                return -1
            cost += g[cur][ul]
            cur = ul
            nextUL += 1
            loaded -= 1

    while loaded > 0:
        ul = tasks[nextUL][1]
        if g[cur][ul] == inf:
            return -1
        cost += g[cur][ul]
        cur = ul
        nextUL += 1
        loaded -= 1

    return cost



t = int(inp.readline().strip())

for i in range(t):
    n, m, k = map(int, inp.readline().strip().split())
    g = [[inf for jj in range(n)] for j in range(n)]
    for j in range(n):
        g[j][j] = 0
    for j in range(m):
        a, b, w = map(int, inp.readline().strip().split())
        a -= 1
        b -= 1
        g[a][b] = min(g[a][b], w)
        g[b][a] = min(g[b][a], w)
    tasks = []
    for j in range(k):
        a, b = map(int, inp.readline().strip().split())
        a -= 1
        b -= 1
        tasks.append((a, b))
    print("Case #{}: {}".format(i + 1, move(n, m, k, g, tasks)))

