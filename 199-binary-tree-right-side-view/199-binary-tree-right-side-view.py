# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxx = -1
    def rightCheck(self, root, lst, level):
        if root == None:
            return
        if(level>self.maxx):
            lst.append(root.val)
            self.maxx = level
            
        self.rightCheck(root.right, lst, level+1)            
        self.rightCheck(root.left,lst, level+1)

    def rightSideView(self, root):
        lst = []
        level = 0
        self.rightCheck(root, lst, level)
        return lst
        