from sys import stdin
def parent(i):
    return (i - 1) // 2
def left_child(i):
    return (i*2 + 1)
def right_child(i):
    return (i+1)*2
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def down_heap(self):
        cur = 0
        while left_child(cur) < self.size():
            left = left_child(cur)
            right = right_child(cur)
            next = cur
            if self.heap[next][0] > self.heap[left][0]:
                next = left
            if right < self.size():
                if self.heap[next][0] > self.heap[right][0]:
                    next = right
            if cur == next:
                break
            self.heap[cur], self.heap[next] = self.heap[next], self.heap[cur]
            cur = next

    def up_heap(self):
        cur = self.size() - 1
        while parent(cur) >= 0 and self.heap[cur][0] < self.heap[parent(cur)][0]:
            self.heap[cur], self.heap[parent(cur)] = self.heap[parent(cur)], self.heap[cur]
            cur = parent(cur)

    def size(self):
        return len(self.heap)

    def insert(self, val):
        self.heap.append(val)
        self.up_heap()

    def peek(self):
        return self.heap[0]

    def remove(self):
        if self.size() == 0: return
        result = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.down_heap()
        return result

    def print_heap(self):
        result = ''
        if self.size() == 0:
            return result
        cur = [0]
        while len(cur) > 0:
            next = []
            for i in cur:
                result += str(self.heap[i]) + ' '
                if left_child(i) < self.size():
                    next.append(left_child(i))
                if right_child(i) < self.size():
                    next.append(right_child(i))
            result += '\n'
            cur = next
        return result

    def __str__(self):
        return self.print_heap()

def laundry(l, n, m, d, nums):
    import queue
    w = queue.PriorityQueue()
    dry = [0 for i in range(m)]
    dryIndex = 0
    for i in range(len(nums)):
        w.put((nums[i], i))
    while l > 0:
        l -= 1
        timeFinishW, washIndex = w.get()
        w.put((timeFinishW + nums[washIndex], washIndex))
        timeDrierReady = max(dry[dryIndex], timeFinishW)
        dry[dryIndex] = timeDrierReady + d
        dryIndex = (dryIndex + 1) % m
    return dry[(dryIndex + m - 1) % m]


from sys import stdout
inp = open('laundro_matt.in', 'r')
out = stdout#open('out.txt', 'w')
t = int(inp.readline().strip())
for i in range(t):
    l, n, m, d = map(int, inp.readline().strip().split())
    nums = list(map(int, inp.readline().strip().split()))
    if i + 1 != 7: continue
    out.write("Case #{}: {}\n".format(i + 1, laundry(l, n, m, d, nums)))