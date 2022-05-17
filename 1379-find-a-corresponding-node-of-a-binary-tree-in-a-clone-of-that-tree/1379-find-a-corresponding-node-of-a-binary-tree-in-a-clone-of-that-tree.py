# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorder(self, root, target):
        if root == None:
            return
        if root.val == target:
            return root
        root1 = self.preorder(root.left, target)
        root2 = self.preorder(root.right, target)
        
        if root1 != None:
            return root1
        return root2
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        val = target.val
        cloneTarget = self.preorder(cloned, val)
        return cloneTarget