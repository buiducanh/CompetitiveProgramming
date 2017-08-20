from math import sqrt
def prime(n):
    if n > 2 and n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)+1), 2):
        if n % i == 0:
            return False
    return True
def lovely(n):
    if prime(n):
        return n 
    res = 2 if n >= 2 and n % 2 == 0 else 1
    while n % 2 == 0:
        n = n // 2
    i = 3
    while n >= 3:
        while not prime(i): 
            i += 2
        if n % i == 0:
            res *= i
        while n % i == 0:
            n = n // i
        i += 2
    return res

from sys import stdin
inp = stdin
n = int(inp.readline().strip())
print lovely(n)
