# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchNode(self, root, targetNode, lst):
        if root == None:
            return list()
        lst.append(root)
        if targetNode.val > root.val:
            return self.searchNode(root.right, targetNode, lst)
        elif targetNode.val < root.val:
            return self.searchNode(root.left, targetNode, lst)
        else:
            return lst
    
    # def findAllAncestors(self, root, targetNode):
    #     return self.searchNode(root, targetNode, [])
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pAncestors = self.searchNode(root, p, [])
        qAncestors = self.searchNode(root, q, [])
        
        i = 0
        possibleAns = None
        
        length = min(len(pAncestors), len(qAncestors))
            
        for i in range(length):
            if pAncestors[i].val == qAncestors[i].val:
                possibleAns = pAncestors[i]
            else:
                break
                
        return possibleAns
        

# 3->[6,2,4,3]

# 5->[6,2,4,5]
# 9->[6,8,9]

# 0->[6,2,0]
# 3->[6,2,4,3]

# possibleAns = 4