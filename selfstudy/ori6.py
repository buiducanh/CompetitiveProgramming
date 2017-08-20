def fibo(n):
    if n == 0:
        return
    if n <= 2:
        print [1 for i in range(n)]
        return
    dp = [1, 1]
    while len(dp) < n:
        dp.append(dp[-1] + dp[-2])
    print(dp)

for i in range(15):
    fibo(i)
