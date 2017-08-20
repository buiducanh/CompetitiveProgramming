days = int(raw_input().strip())

pizzas = list(map(int, raw_input().strip().split()))

remain = 0
for i in range(len(pizzas)):
    if remain == 1 and pizzas[i] % 2 == 1:
        remain = 0
    elif remain == 1 and pizzas[i] == 0:
        break
    elif remain == 0 and pizzas[i] % 2 == 1:
        remain = 1

if remain:
    print "NO"
else:
    print "YES"

