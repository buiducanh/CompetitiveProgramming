def least_required(a, b):
    if a >= b:
        return 3
    return min(abs(b - a - 1) // 10, 3)
def contest2(n, nums):
    nums.append(nums[-1])
    cur = 1
    result = 0
    i = 1
    while i < n + 1:
        gap = least_required(nums[i - 1], nums[i])
        if gap == 0:
            cur += 1 
            i += 1
        else:
            missing = 4 - cur 
            if missing <= gap:
                result += missing
                cur += missing
            else:
                result += gap 
                cur += gap + 1
                i += 1
        if cur == 4:
            cur = 1
            i += 1
    return result
def contest(n, nums):
    nums.append(nums[-1])
    segments = [1 for i in range(n)]
    segments.append(0)
    for i in reversed(range(n - 1)):
        if least_required(nums[i], nums[i + 1]) == 0:
            segments[i] += segments[i + 1] 
    i = 0
    cur = 1
    result = 0
    while i < n:
        if segments[i] >= 4:
            i += 4
        else:
            to_be_created = least_required(nums[i], nums[i + 1])
            if to_be_created == 0:
                cur += 1
                i += 1
            else:
                if to_be_created > 4 - cur: 
                    result += 4 - cur
                    cur = 1
                    i += 1
                else:
                    missing = 4 - (segments[i + 1] + cur + to_be_created)
                    if missing <= 0: 
                        i += 1 + (4 - cur - to_be_created)
                        cur = 1
                        result += to_be_created
                    else:
                        i += 1 
                        cur += to_be_created + segments[i + 1] 
    return result
                


from sys import stdin, stdout
inp = open("coding_contest.in", 'r')
t = int(inp.readline().strip())
#out = open("out.txt", 'w')
#for i in range(t):
#    n = int(inp.readline().strip())
#    nums = map(int, inp.readline().strip().split())
#    out.write("Case #{}: {}\n".format(i + 1, contest2(n, nums)))

otherSol = open('coding_contest.out', 'r')
mySol = open('out.txt', 'r')
for line in mySol:
    otherLine = otherSol.readline().strip()
    if int(line.split(": ")[-1]) != int(otherLine.split(": ")[-1]):
        print(line, otherLine)
