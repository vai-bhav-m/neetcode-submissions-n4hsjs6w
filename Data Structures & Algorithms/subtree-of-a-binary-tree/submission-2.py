class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        # Check if current node is a match, OR continue searching
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both null
        if not p and not q:
            return True
        # One null, other not
        if not p or not q:
            return False
        # Values differ
        if p.val != q.val:
            return False
        # Check both subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)