# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        def dfs(n1, n2):
            if n1 is None and n2 is None:
                return True
            
            if n1 is None or n2 is None or n1.val != n2.val:
                return False
            
            return dfs(n1.left, n2.right) and dfs(n1.right, n2.left)           
            
        return dfs(root.left, root.right)