def toBase3(n):
    base3 = []
    while n > 0:
        temp = n % 3
        n /= 3
        base3.append(temp)
    return base3

def weigh(n):
    base3 = toBase3(n)
    l = []
    r = []
    i = 0
    while i < len(base3):
        if base3[i] == 2:
            l.append(3**i)
            leftover = 1
            base3[i] = 0
            j = i + 1
            if j == len(base3):
                base3.append(0)
            while leftover > 0 and j < len(base3):
                leftover -= 1
                base3[j] += 1
                if base3[j] == 3:
                    base3[j] = 0
                    leftover += 1
                    if j + 1 == len(base3):
                        base3.append(0)
                j += 1
        elif base3[i] == 1:
            r.append(3**i)
        i += 1
    return n, list(reversed(l)), list(reversed(r))

from sys import stdin, stdout
#inp = open("in", "r")
inp = stdin
t = int(inp.readline().strip())
for i in range(t):
    n = int(inp.readline().strip())
    _, left, right = weigh(n)
    stdout.write("left pan:")
    for i in left:
        stdout.write(" " + str(i))
    stdout.write("\n")
    stdout.write("right pan:")
    for i in right:
        stdout.write(" " + str(i))
    stdout.write("\n\n")
