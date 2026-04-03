# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, (1001, -1001)]
            left_sub, right_sub = dfs(node.left), dfs(node.right)
            if not (left_sub[0] and right_sub[0]):
                return [False, (-1001, 1001)]
            if left_sub[1][1] >= node.val:
                return [False, (-1001, 1001)]
            if right_sub[1][0] <= node.val:
                return [False, (-1001, 1001)]
            return [
                True, 
                (min(node.val,left_sub[1][0]), 
                 max(node.val,right_sub[1][1]))
                    ]
        return dfs(root)[0] 