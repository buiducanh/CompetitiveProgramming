# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def validleft(self, dic, p, c):
        return dic[p.val] > dic[c.val] #and p.left == None
    def validright(self, dic, p, c):
        return dic[p.val] < dic[c.val] #and p.right == None

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(postorder) <= 0:
            return None
        inor = 0
        post = len(postorder) - 1
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        root = TreeNode(postorder[post])
        s = [root]
        while post > 0:
            post -= 1
            child = TreeNode(postorder[post])
            cur = s[-1]
            if self.validright(dic, cur, child):
                cur.right = child
            else:
                while len(s) >= 2:
                    if self.validleft(dic, s[-1], child) and not self.validleft(dic, s[-2], child):
                        break
                    s.pop()
                cur = s[-1]
                cur.left = child
                s.pop()
            s.append(child)
        return root
