# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root, -1*(1 << 31) - 1, 1 << 31)
    def isValid(self, root, lo, hi):
        if root is None:
            return True
        if root.val <= lo or root.val >= hi:
            return False
        return self.isValid(root.left, lo, root.val) and self.isValid(root.right, root.val, hi)