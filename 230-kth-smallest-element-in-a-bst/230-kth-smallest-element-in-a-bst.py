# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    lst = []
    def inorder(self, root, k):
        if root == None:
            return
        self.inorder(root.left, k)
        self.lst.append(root.val)
        if len(self.lst) == k:
            return
        self.inorder(root.right, k)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.lst = []
        self.inorder(root, k)
        # print(self.lst)
        return self.lst[k-1]