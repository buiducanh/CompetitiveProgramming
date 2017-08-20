from sys import stdin
def price(n, p, m):
    cur = 0
    sum = 0
    result = 0
    for i in range(n):
        sum += m[i]
        while sum > p:
            sum -= m[cur]
            cur += 1
        if sum <= p:
            result += i - cur + 1
    return result
inp = open('the_price_is_correct.txt', 'r')
out = open('out.txt', 'w')
t = int(inp.readline().strip())
for i in range(t):
    n, p = map(int, inp.readline().strip().split())
    m = list(map(int, inp.readline().strip().split()))
    out.write('Case #{}: {}\n'.format(str(i + 1), str(price(n, p, m))))
out.close()
inp.close()
