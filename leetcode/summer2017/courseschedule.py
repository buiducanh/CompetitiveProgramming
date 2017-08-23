class Solution(object):
    visited = None
    adj = None
    valid = None

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.adj = [set() for i in range(numCourses)]
        for pair in prerequisites:
            self.adj[pair[0]].add(pair[1])

        self.visited = [False for i in range(numCourses)]
        self.valid = [False for i in range(numCourses)]

        for course in range(numCourses):
            if len(self.adj[course]) == 1:
                if not self.dfsToSatisfyRequirements(course):
                    return False
        return True

    def dfsToSatisfyRequirements(self, i):
        if self.valid[i]:
            return True
        if self.visited[i]:
            return False
        self.visited[i] = True
        for req in self.adj[i]:
            if not self.dfsToSatisfyRequirements(req):
                return False
        self.valid[i] = True
        return True


n = int(raw_input().strip())
edges = []
while True:
    try:
        i, j = map(int, raw_input().strip().split())
        edges.append((i, j))
    except Exception:
        break

print(Solution().canFinish(n, edges))
