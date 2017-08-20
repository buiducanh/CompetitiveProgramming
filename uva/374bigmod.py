def bigmod(b, p, m):
    if p <= 1:
        return (b**p) % m
    if p % 2 != 0:
        return (b % m) * bigmod(b, p - 1, m)
    return (bigmod(b, p // 2, m) * bigmod(b, p // 2, m)) % m

b = int(raw_input())
p = int(raw_input())
m = int(raw_input())
print(bigmod(b, p, m))
