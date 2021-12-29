# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, inorderList):
        if root == None:
            return
        self.inorder(root.left, inorderList)
        inorderList.append(root.val)
        self.inorder(root.right, inorderList)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorderList = []
        self.inorder(root, inorderList)
        sortedList = sorted(inorderList)
        
        print(sortedList)
        print(inorderList)
        
        
        for i in range(len(sortedList)):
            if i != 0 and sortedList[i] == sortedList[i-1]:
                return False
            if sortedList[i] != inorderList[i]:
                return False
        return True
        