from sys import stdin, stdout
inp = stdin

n = int(inp.readline().strip())
cnt = 0
inspect = True

if n == 0:
    num = 0
else:
    num = 1
    for i in inp.readline().strip().split():
        newNum = res = int(i)
        if newNum == 0:
            num = 0
            cnt = 0
            break
        if inspect:
            while res >= 10.0:
                res /= 10.0
            if res > 1.0:
                inspect = False
                num = newNum
            else:
                cnt += len(i) - 1
        else:
            cnt += len(i) - 1

final = [str(num)] + ['0' for i in range(cnt)]
print ''.join(final)

# res = 1
# for i in inp.readline().strip().split():
#     res *= int(i)
#     if res == 0:
#         break
# print res

