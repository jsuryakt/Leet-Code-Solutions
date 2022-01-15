# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    finalAns = 0
    
    def binaryToDecimal(self, binary):
        # print("Binary",binary)
        power = len(binary) - 1
        ans = 0
        for num in binary:
            if num == '1':
                ans += 2**power
            power -= 1
        # print("Ans by B2D",ans, binary)
        return ans
    
    def getBinary(self, root, multiplier):
        if root == None:
            return 
        if root.left == None and root.right == None:
            # print("Multiplier",multiplier)
            multiplier = multiplier*10 + root.val
            self.finalAns += self.binaryToDecimal(str(multiplier))
            # print(self.finalAns)
            return
        
        curr = multiplier*10 + root.val
        
        self.getBinary(root.left, curr)
        self.getBinary(root.right, curr)

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.getBinary(root, 0)
        return int(self.finalAns)
        
        