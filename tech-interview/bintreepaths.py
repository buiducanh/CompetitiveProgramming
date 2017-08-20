# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root is None:
            return []
        ans = []
        self.drawPaths(root, [], ans)
        return ans
    def drawPaths(self, root, path, ans):
        if root.left is None and root.right is None:
            ans.append("".join(path + [str(root.val)]))
            return
        path.append(str(root.val))
        if root.left:
            self.drawPaths(root.left, path + ["->"], ans)
        if root.right:
            self.drawPaths(root.right, path + ["->"], ans)

            