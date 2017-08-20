n , k  = map(int, raw_input().split(" "))
nums = map(int, raw_input().split())

from Queue import PriorityQueue
q = PriorityQueue()
for i in nums:
    q.put(i)

sum = -1
ans = 0
while not q.empty():
    first = q.get()
    if first >= k:
        print ans
        break
    if q.empty():
        print -1
        break
    second = q.get()
    sum = first + 2*second
    q.put(sum)
    ans = ans + 1
