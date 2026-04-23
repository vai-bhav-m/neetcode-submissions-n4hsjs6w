# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]
            
            left_bal = dfs(root.left)
            right_bal = dfs(root.right)
            if not (left_bal[0] and right_bal[0]):
                return [False, 0]
            
            height = 1 + max(left_bal[1], right_bal[1])
            isBalanced = abs(left_bal[1] - right_bal[1]) < 2
            return [isBalanced, height]
        
        return dfs(root)[0]