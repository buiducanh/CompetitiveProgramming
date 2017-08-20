from sys import stdin
inp = open('text_editor.in', 'r')

def print_next(lcp, a, b):
    return (len(a)- lcp) + (len(b) - lcp) + 1


def textEditor(n, k, words):
    words.sort()
    lcp = [[0 for i in range(n)] for j in range(n)]
    for i in range(1, n):
        for j in range(i):
            c = 0
            for o in range(len(words[j])):
                if words[j][o] != words[i][o]:
                    break
                c += 1
            lcp[i][j] = c
    dp = [[999999999 for i in range(k + 1)] for j in range(n)]
    for i in range(n):
        dp[i][1] = len(words[i]) + 1
    for i in range(1, n):
        for j in range(2, k + 1):
            min = i - 1
            for o in range(j - 2, i - 1):
                if dp[min][j - 1] + print_next(lcp[i][min], words[min], words[i]) > dp[o][j - 1] + print_next(lcp[i][o], words[o], words[i]):
                    min = o
            dp[i][j] = dp[min][j - 1] + print_next(lcp[i][min], words[i], words[min])
    result = 9999999999999
    for i in range(0, n):
        if result > dp[i][k] + len(words[i]):
            result = dp[i][k] + len(words[i])

    return result




out = open('out.txt', 'w')
t = int(inp.readline().strip())
for i in range(t):
    n, k = map(int, inp.readline().strip().split())
    words = [inp.readline().strip() for j in range(n)]
    out.write('Case #{}: {}\n'.format(i + 1, textEditor(n, k, words)))

inp.close()
out.close()

otherSol = open('text_editor.out', 'r')
mySol = open('out.txt', 'r')
for line in mySol:
    otherLine = otherSol.readline().strip()
    if int(line.split(": ")[-1]) != int(otherLine.split(": ")[-1]):
        print(line, otherLine)
