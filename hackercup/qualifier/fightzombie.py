from sys import stdin
eps = .000001
def comp(x, y):
    if abs(x*1.0 - y) < eps:
        return 0
    return 1 if x > y else -1

comb = [[-1 for i in range(500)] for j in range(500)]

def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        if comb[n][k] == -1:
            ntok = 1
            ktok = 1
            i = n
            for t in xrange(1, min(k, n - k) + 1):
                ntok *= i
                ktok *= t
                i -= 1
            comb[n][k] = ntok // ktok
        return comb[n][k]
    else:
        return 0

def parseDice(dice):
    times, dice = dice.split('d')
    ops = None
    if '+' in dice:
        ops = '+'
    elif '-' in dice:
        ops = '-'

    if ops:
        sides, offset = dice.split(ops)
        offset = ops + offset
    else:
        sides = dice
        offset = 0
    return tuple(map(int, (times, sides, offset)))

def genA(i, k):
    # ith coefficients of (x^k)/(1-x)^k
    return choose(i - 1, i - k)

def genB(i, m, n):
    # ith coefficients of (1 - x^m)^n
    if i % m != 0:
        return 0
    i /= m
    return (-1)**(i) * choose(n, i)

def defeatProbability(h, dice):
    total = dice[1]**dice[0]
    realDamage = h - dice[2]
    maxDamage = dice[1] * dice[0]
    minDamage = dice[0]
    if realDamage <= minDamage:
        return 1
    if realDamage - minDamage < maxDamage - realDamage:
        start = minDamage
        end = realDamage - 1
        losing = True
    else:
        start = realDamage
        end = maxDamage
        losing = False


    positions = 0
    for i in range(start, end + 1):
        count = 0
        for j in range(i + 1):
            count += genA(j, dice[0]) * genB(i - j, dice[1], dice[0])
        positions += count

    prob = 1.0 * positions / total
    if losing:
        return 1 - prob
    else:
        return prob



def fight(h, dices):
    res = 0
    for dice in dices:
        prob = defeatProbability(h, dice)
        if comp(prob, res) == 1:
            res = prob
    return res

inp = stdin
#inp = open("fighting_the_zombie.txt", 'r')
t = int(inp.readline().strip())
for i in range(t):
    h, s = map(int, inp.readline().strip().split())
    dices = list(map(parseDice, inp.readline().strip().split()))
    res = fight(h, dices)
    print("Case #{}: {:0.6f}".format(i + 1, res))
