# Disjoint data set algorithms
"""
  Definition of a set.
"""
class Node:
  def __init__(self, parent, pid):
    self.parent = parent if parent else self
    self.rank = 0
    self.pid = pid

def makeSet(val, pid):
  return Node(val, pid)
"""
  Find the representative of the set using the value.

  Implements path compression by setting all the parents to the set's root.
"""
def find(u):
  if u.parent != u:
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
  if u.rank < v.rank:
    u.parent = v
    v.pid = u.pid
  elif u.rank > v.rank:
    v.parent = u
    u.pid = v.pid
  else:
    u.parent = v
    v.rank += 1
    v.pid = u.pid

n, m, k = list(map(int, raw_input().strip().split()))

socks = list(map(int, raw_input().strip().split()))

days = []

sets = [makeSet(None, i) for i in range(n)]
dictOfSets = {}
for i in range(n):
    dictOfSets[i] = [i]

for i in range(m):
    l, r = list(map(int, raw_input().strip().split()))
    l -= 1
    r -= 1
    days.append((l, r))
    if find(sets[l]) != find(sets[r]):
        union(sets[l], sets[r])
        if sets[l].parent == sets[l]:
            if r in dictOfSets:
                dictOfSets[l].append(*dictOfSets[r])
                del dictOfSets[r]
        if sets[r].parent == sets[r]:
            if l in dictOfSets:
                dictOfSets[r].append(*dictOfSets[l])
                del dictOfSets[l]

ans = 0
for key in dictOfSets:
    val = dictOfSets[key]
    count = [0 for i in range(k + 1)]
    max = 0
    color = 0
    for i in range(k):
        count[i+1] = 0

    for sockid in val:
        count[socks[sockid]] += 1
        if count[socks[sockid]] > max:
            color = socks[sockid]
            max = count[socks[sockid]]
    ans += len(val) - max

print(ans)
