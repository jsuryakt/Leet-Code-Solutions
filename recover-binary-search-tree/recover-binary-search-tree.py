# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkForLimit(self, root, lower, upper):
        if root == None:
            return
        if root.val>lower.val and root.val<upper.val:
            self.checkForLimit(root.left, lower, root)
            self.checkForLimit(root.right, root, upper)
        else:
            if root.val<lower.val:
                root.val, lower.val = lower.val, root.val
            elif root.val>upper.val:
                root.val, upper.val = upper.val, root.val
            self.checkForLimit(root, lower, upper)
            return
    def recoverTree(self, root: Optional[TreeNode]):
        for _ in range(10):
            self.checkForLimit(root, TreeNode(-2**32), TreeNode(2**32))
        
        