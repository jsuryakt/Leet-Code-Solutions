# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        ans = []
        queue = []
        
        queue.append(root)
        ans.append([root.val])
        
        while(queue):
            size = len(queue)
            temp = []
            while(size>0):
                currNode = queue.pop(0)
                leftChild = currNode.left
                rightChild = currNode.right

                if leftChild:
                    queue.append(leftChild)
                    temp.append(leftChild.val)
                if rightChild:
                    queue.append(rightChild)
                    temp.append(rightChild.val)
                size -= 1

            if temp:
                ans.append(temp)

        return ans
        
        