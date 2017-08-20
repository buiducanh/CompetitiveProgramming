import sys
class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.next = None
        self.val = val
    def print_tree(self):
        p = self
        firstNext = None
        while p:
            print p.val,
            if not firstNext:
                if p.left:
                    firstNext = p.left
                else:
                    firstNext = p.right
            p = p.next
            if not p:
                p = firstNext
                firstNext = None
         
def print_recur(node):
    if not node:
        return 
    print_recur(node.left)
    print_recur(node.right)
    print node.val, 

# root = Node(1)
# a = Node(2)
# b = Node(3)
# c = Node(4)
# d = Node(5)
# e = Node(6)
# f = Node(7)
# root.left = a; root.right = b
# #a.left = b; #a.right = d
# b.left = c; #b.right = f
# c.left = d
# d.right = e
#e.left = f
#root.print_tree()
# sol(root)
# root.print_tree()

# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root == None:
            return
        upLevel = root
        isLeft = True
        curLevel = None
        if root.left:
            curLevel = root.left
        else:
            curLevel = root.right
            isLeft = False
        while upLevel and curLevel:
            up = upLevel
            cur = curLevel
            while cur:
                newNext = None
                if isLeft:
                    if up.right:
                        newNext = up.right
                        isLeft = False
                while not newNext:
                    up = up.next
                    if up == None:
                        break
                    newNext = up.left
                    isLeft = True
                    if not newNext:
                        newNext = up.right
                        isLeft = False
                cur.next = newNext
                cur = cur.next
            upLevel = curLevel
            nextLevel = None
            while not nextLevel and curLevel:
                if curLevel.left:
                    isLeft = True
                    nextLevel = curLevel.left
                if not nextLevel:
                    isLeft = False
                    nextLevel = curLevel.right
                curLevel = curLevel.next
            curLevel = nextLevel
