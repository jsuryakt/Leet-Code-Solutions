# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    newRoot = None
    tail = None
    def traverseInorder(self, root):
        if root == None:
            return
        self.traverseInorder(root.left)
        if self.newRoot == None:
            self.newRoot = TreeNode(root.val)
            self.tail = self.newRoot
        else:
            self.tail.right = TreeNode(root.val)
            self.tail = self.tail.right
        self.traverseInorder(root.right)
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.newRoot = None
        self.traverseInorder(root)
        return self.newRoot