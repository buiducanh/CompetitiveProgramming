from sys import stdin, stdout
#inp = open("in", "r")
inp = stdin
prime = [True] * 32010
for i in range(2, 32011):
    for j in range(2, i + 1):
        if i * j >= 32010:
            break
        prime[i*j] = False
t = int(inp.readline().strip())
for i in range(t):
    n = int(inp.readline().strip())
    result = []
    for i in range(2, n / 2 + 1):
        if prime[i] and prime[n - i]:
            result.append((i, n - i))
    print "{} has {} representation(s)".format(n, len(result))
    for x, y in result:
        print "{}+{}".format(x, y)
    print ""

