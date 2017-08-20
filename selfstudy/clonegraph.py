# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, root):
        nodes = {}
        def recurHelper(node):
            if node is None:
                return None
            newNode = UndirectedGraphNode(node.label)
            nodes[node.label] = newNode
            for i in range(len(node.neighbors)):
                adjNode = node.neighbors[i]
                if adjNode.label not in nodes:
                    newAdjNode = recurHelper(adjNode)
                else:
                    newAdjNode = nodes[adjNode.label]
                newNode.neighbors.append(newAdjNode)
            return newNode
        return recurHelper(root)
