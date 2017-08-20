from collections import deque
def findOrder1(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    from collections import deque
    q = deque()
    indeg = [0 for i in range(numCourses)]
    adj = [[] for i in range(numCourses)]
    for edge in prerequisites:
        adj[edge[0]].append(edge[1])
        indeg[edge[1]] += 1
    result = []
    for i in range(numCourses):
        if indeg[i] == 0:
            q.append(i)
    while q:
        cur = q.popleft()
        result.append(cur)
        if cur < len(adj):
            while adj[cur]:
                k = adj[cur].pop()
                indeg[k] -= 1
                if indeg[k] == 0:
                    q.append(k)
    if len(result) != numCourses:
        return []
    return list(reversed(result))
def findOrder(numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        from collections import deque
        q = deque()
        level = [0 for j in range(numCourses)]
        ancestor = [-1 for i in range(numCourses)]
        for i in range(numCourses):
            q.append(i)
            while q:
                cur = q.popleft()
                if cur < len(prerequisites) and prerequisites[cur]:
                    for k in prerequisites[cur]:
                        if level[k] < level[cur] + 1:
                            if ancestor[k] == cur:
                                return []
                            level[k] = level[cur] + 1
                            ancestor[k] = cur
                            q.append(k)
        result = [[] for i in range(numCourses)]
        for i in range(numCourses):
            result[level[i]].append(i)
        return list(reversed(reduce(lambda x,y: x + y, result)))
n = 2
g = [
    [1, 0]
]
print findOrder1(n, g)
