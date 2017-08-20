# Disjoint data set algorithms
"""
  Definition of a set.
"""
class Node:
  def __init__(self, parent):
    self.parent = parent if parent else self
    self.rank = 0

def makeSet(val=None):
  return Node(val)
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
  elif u.rank > v.rank:
    v.parent = u
  else:
    u.parent = v
    v.rank += 1

class Kruskal:
    def __init__(self, graph):
        self.graph = graph
    def solution(self):
        edges = graph['edges']
        edges.sort()
        sets = {}
        min_span_tree = set()
        for edge in edges:
            w, a, b = edge
            if a == 'f' and b == 'i':
                min_span_tree.add(edge)
                break

        for i in graph['vertices']:
            sets[i] = makeSet()
        for edge in edges:
            w, a, b = edge
            if find(sets[a]) != find(sets[b]):
                union(sets[a], sets[b])
                min_span_tree.add(edge)
        return min_span_tree

directed_edges = [
                (7, 'L', 'c'),
                (5, 'L', 'a'),
                (8, 'L', 'b'),
                (4, 'a', 'c'),
                (5, 'a', 'b'),
                (8, 'c', 'e'),
                (3, 'c', 'd'),
                (4, 'b', 'd'),
                (7, 'b', 'h'),
                (5, 'd', 'e'),
                (6, 'd', 'h'),
                (7, 'd', 'f'),
                (4, 'h', 'f'),
                (6, 'h', 'j'),
                (8, 'e', 'g'),
                (3, 'f', 'g'),
                (8, 'f', 'i'),
                (4, 'g', 'j'),
                (6, 'g', 'k'),
                (4, 'g', 'i'),
                (5, 'j', 'm'),
                (3, 'i', 'k'),
                (12, 'i', 'l'),
                (4, 'k', 'l'),
                (5, 'k', 'W'),
                (5, 'k', 'm'),
                (8, 'l', 'W'),
            ]
undirected_edges = []
for w, a, b in directed_edges:
    undirected_edges.append((w, a, b))
    undirected_edges.append((w, b, a))
graph = {
        'vertices': [
            'L', 'W'
            ] + [chr(i) for i in range(97, 123)],
        'edges': undirected_edges
        }

algo = Kruskal(graph)
tree = algo.solution()
print(tree)
print(map(lambda x: x[1:], tree))
print(sum(map(lambda x: x[0], tree)))
