# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        
        if root1 == None or root2 == None:
            return False
        
        if root1.val != root2.val:
            return False
        
        left = self.inorder(root1.left, root2.left)
        
        right = self.inorder(root1.right, root2.right)
        
        return left and right
        
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.inorder(p,q)