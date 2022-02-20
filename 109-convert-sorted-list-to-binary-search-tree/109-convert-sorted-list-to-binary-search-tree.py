# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    lst = []
    def convertToList(self, head):
        lst = []
        
        while(head != None):
            lst.append(head.val)
            head = head.next
        
        return lst
    
    def fillTree(self, i, j):
        global lst
        if i > j:
            return None
        mid = (i+j)//2
        root = TreeNode(lst[mid])
        root.left = self.fillTree(i, mid-1)
        root.right = self.fillTree(mid+1, j)
        
        return root
        
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        global lst
        lst = self.convertToList(head)
        root = self.fillTree(0, len(lst)-1)
        return root