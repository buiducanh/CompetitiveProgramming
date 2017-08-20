inp = open('high_security.in', 'r')
out = open('out.txt', 'w')
t = int(inp.readline().strip())
def security(n, g):
    cur = True
    result = 0
    for i in range(2, n + 2):
        if cur and g[0][i - 1] == '.':
            if g[0][i - 2] == 'X' and g[0][i] == 'X' and g[1][i - 1] == '.':
                g[1][i - 1] = 'G'
                result += 1
            elif g[1][i - 2] == 'X' and g[1][i] == 'X' and g[1][i - 1] == '.':
                cur = False
                g[0][i-1] = 'G'
                result += 1
            elif g[0][i] == 'X':
                g[0][i - 1] = 'G'
                result += 1
        if g[0][i] == 'X':
            cur = True
    cur = True
    for i in reversed(range(0, n + 1)):
        if g[1][i] == 'G':
            cur = False
        if cur and g[1][i] == 'X' and g[1][i + 1] == '.':
            if g[0][i + 1] != 'G':
                cur = False
                g[1][i + 1] = 'G'
                result += 1
            elif i + 2 < n + 2 and g[1][i + 2] == '.':
                cur = False
                g[1][i + 1] = 'G'
                result += 1

        if g[1][i] == 'X':
            cur = True
    # print(g[0])
    # print(g[1])
    # print()
    return result


for i in range(t):
    n = int(inp.readline().strip())
    g = [list('X' + inp.readline().strip() + 'X') for i in range(2)]
    # if i + 1 != 3: continue
    out.write('Case #{}: {}\n'.format(str(i+1), security(n, g)))

inp.close()
out.close()

otherSol = open('high_security.out', 'r')
mySol = open('out.txt', 'r')
for line in mySol:
    otherLine = otherSol.readline().strip()
    if int(line.split(": ")[-1]) != int(otherLine.split(": ")[-1]):
        print(line, otherLine)
