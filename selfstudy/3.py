n = int(raw_input().strip())

nums = map(int, raw_input().strip().split())

order = map(int, raw_input().strip().split())

def sol1(n, nums, order):
    iterSum = [0] + nums
    for i in range(1, n + 1):
      iterSum[i] = iterSum[i] + iterSum[i - 1]

    def getSumInRange(iterSum, i, j):
      if j == 0:
        return 0

      return iterSum[j] - iterSum[i]

    class Node:
      def __init__(self, val, next=None):
        self.val = val
        self.next = next

    root = Node(0)
    root.next = Node(n + 1)
    for idx in order:
      l = root
      newNode = Node(idx)
      max = 0
      while l.next:
        if idx > l.val and idx < l.next.val:
          newNode.next = l.next
          l.next =  newNode
        sum = getSumInRange(iterSum, l.val, l.next.val - 1)
        if sum > max:
          max = sum
        l = l.next
      print(max)

def sol2(n, nums, order):
    """
      Definition of a set.
    """
    class Node:
      def __init__(self, sum):
        self.parent = self
        self.rank = 0
        self.sum = sum

    def makeSet(sum):
      return Node(sum)
    """
      Find the representative of the set using the value.

      Implements path compression by setting all the parents to the set's root.
    """
    def find(u):
      if u.parent != u.parent:
        u.parent = find(u.parent)
      return u.parent

    """
      Unions the two disjointed sets.

      Also makes sure to maintain a shallow tree by
      attaching the root of the smaller tree to the bigger tree.

      Note that the rank of the set would only increase when rank[u] == rank[v].

      * Distinction between rank of depth is made because path compression doesn't
      care about the rank, and so the depth of the tree no longer equals the rank.
    """
    def union(u, v):
      u = find(u)
      v = find(v)
      if u == v:
        return u
      if u.rank < v.rank:
        v.sum += u.sum
        u.parent = v
      elif u.rank > v.rank:
        u.sum += v.sum
        v.parent = u
      else:
        v.sum += u.sum
        u.parent = v
        v.rank += 1
      return u.parent

    sets = [None for i in range(n)]
    ans = [0 for i in range(n)]
    max = 0
    for i in range(1, n):
        addIndex = order[-i] - 1
        u = makeSet(nums[addIndex])
        set = u
        sets[addIndex] = u
        if addIndex > 0 and sets[addIndex - 1]:
            set = union(u, sets[addIndex - 1])
        if addIndex < n - 1 and sets[addIndex + 1]:
            set = union(u, sets[addIndex + 1])
        if set.sum > max:
            max = set.sum
        ans[-i - 1] = max
    for i in ans:
        print(i)

# sol1(n, nums, order)
sol2(n, nums, order)
