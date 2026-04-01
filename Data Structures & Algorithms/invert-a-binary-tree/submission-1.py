# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        sol = TreeNode(root.val, root.right, root.left)
        sol.left = self.invertTree(sol.left)
        sol.right = self.invertTree(sol.right)
        return sol