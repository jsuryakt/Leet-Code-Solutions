# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root, lower, upper):
        if root == None:
            return True
        if root.val > lower and root.val < upper:
            left = self.check(root.left, lower, root.val)
            right = self.check(root.right, root.val, upper)
            
            if left != False and right != False:
                return True
            else:
                return False
        else:
            return False
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, -2**32, 2**32)
        