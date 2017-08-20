n = int(raw_input())
nums = map(int, raw_input().strip().split())
i = 0
while i < n and nums[i] == 0:
    i += 1
if i == n:
    res = 0
else:
    res = 1
while i < n:
    cnt = 1
    i += 1
    while i < n and nums[i] == 0:
        i += 1 
        cnt += 1
    if i < n and nums[i] == 1:
        res *= cnt
print(res)
