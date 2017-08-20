def myfibo(a, b, n):
    if n == 1:
        return a
    if n == 2:
        return b
    c = a + b
    n = n - 3
    for i in xrange(n):
        a, b, c = b, c, b + c
    return c

a, b, n = map(int, raw_input().strip().split())
print myfibo(a, b, n)

