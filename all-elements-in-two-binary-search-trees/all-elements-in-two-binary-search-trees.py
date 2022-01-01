# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, lst):
        if root == None:
            return []
        self.inorder(root.left, lst)
        lst.append(root.val)
        self.inorder(root.right, lst)
        return lst
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        lst1 = self.inorder(root1, [])
        lst2 = self.inorder(root2, [])
        ans = lst1+lst2
        ans.sort()
        return ans