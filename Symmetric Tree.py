# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        def dfs(r1,r2):
            if r1 == r2:
                return True
            if r1 is None or r2 is None or r1.val != r2.val:
                return False
            return dfs(r1.left,r2.right) and dfs(r1.right,r2.left)
        return dfs(root.left,root.right)