# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSymmetry(self, left, right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        
        if left.val != right.val:
            return False
        else:
            out = self.checkSymmetry(left.left, right.right)
            inn = self.checkSymmetry(left.right, right.left)
            return out and inn
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.checkSymmetry(root.left, root.right)