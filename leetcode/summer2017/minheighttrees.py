class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        if n == 0:
            return []

        adj = [[] for i in range(n)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        q = []
        for i in range(n):
            if len(adj[i]) == 1:
                q.append(i)
        while True:
            next_leaves = []
            for cur in q:
                for e in adj[cur]:
                    adj[e].remove(cur)
                    if len(adj[e]) == 1:
                        next_leaves.append(e)
            if not next_leaves:
                return q
            q = next_leaves


    def findMinHeightTreesWRONG(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for i in range(n)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        if len(edges) < n:
            visited = [False for i in range(n)]
            for i in range(n):
                if not visited[i] and not isTree(i, adj, visited):
                    return []
        else:
            return []

        visited = [False for i in range(n)]
        before = [0 for i in range(n)]
        after = [0 for i in range(n)]
        dfs(0, before, after, 0, adj)

        cur = 0
        other_offset = 0
        max_sub = after[cur]
        max_other = 0
        while True:
            if max_sub == max_other + other_offset:
                return [cur]

            visited[cur] = True

            sub = max_sub
            other = max_other
            after_1 = after_2 = -(1 << 31)
            max_e = None
            for e in adj[cur]:
                if not visited[e] and after[e] > after_2:
                    if after[e] > after_1:
                        after_1, after_2 = after[e], after_1
                        max_e = e
                    else:
                        after_2 = after[e]
            print(cur, max_e, max_sub, max_other + other_offset, after_1, after_2)
            if after_2 > max_other + other_offset + 1:
                if (abs(max_sub - max_other - other_offset) == 1 and
                after_1 == max_sub and
                after_2 + 1 == max_other + other_offset):
                    return [cur, max_e]

                max_other = after_2
                other_offset = 1
                max_sub = after_1
            else:
                if (abs(max_sub - max_other - other_offset) == 1 and
                abs(after_1 - max_other - other_offset - 1) == 1):
                    return [cur, max_e]
                other_offset += 1
                max_sub = after_1
            cur = max_e



def dfs(i, before, after, d, adj, p = None):
    before[i] = d
    max_after = d
    for e in adj[i]:
        if e == p:
            continue
        max_after = max(max_after, dfs(e, before, after, d + 1, adj, i))
    after[i] = max_after - before[i]
    return max_after


def isTree(i, adj, visited, p = None):
    if visited[i]:
        return False
    visited[i] = True
    for e in adj[i]:
        if e != p and not isTree(e, adj, visited, i):
            return False
    visited[i] = False
    return True


n = int(raw_input().strip())
edges = []
while True:
    try:
        i, j = map(int, raw_input().strip().split())
        edges.append((i,j))
    except Exception:
        break
s = Solution()
print(s.findMinHeightTrees(n, edges))
