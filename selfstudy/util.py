# Disjoint data set algorithms
"""
  Definition of a set.
"""
class Node:
  def __init__(self, parent):
    self.parent = parent
    self.rank = 0

def makeSet(val):
  return Node(val)
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
  if u.rank < v.rank:
    u.parent = v
  elif u.rank > v.rank:
    v.parent = u
  else:
    u.parent = v
    v.rank += 1
