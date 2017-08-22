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


    def findMinHeightTreesDP(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for i in range(n)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        height1 = [-(1 << 31) for i in range(n)]
        height2 = list(height1)
        dfsForSubtree(0, height1, height2, adj)
        dp = [0 for i in range(n)]
        dfsAdjustWithAccumulation(0, height1, height2, adj, dp, 0)

        min_height = min(dp)
        res = []
        for i in range(n):
            if dp[i] == min_height:
                res.append(i)
        return res


def dfsForSubtree(i, height1, height2, adj, p = None):
    for e in adj[i]:
        if e != p:
            dfsForSubtree(e, height1, height2, adj, i)
            subtree_max = height1[e] + 1
            if subtree_max > height1[i]:
                height1[i], height2[i] = subtree_max, height1[i]
            elif subtree_max > height2[i]:
                height2[i] = subtree_max
    height1[i] = max(height1[i], 0)


def dfsAdjustWithAccumulation(i, height1, height2, adj, dp, acc, p = None):
    dp[i] = max(height1[i], acc)
    for e in adj[i]:
        if e != p:
            other_path = height1[i] + 1 if height1[e] + 1 != height1[i] else height2[i] + 1
            dfsAdjustWithAccumulation(e, height1, height2, adj, dp, max(acc + 1, other_path), i)


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
print(s.findMinHeightTreesDP(n, edges))
