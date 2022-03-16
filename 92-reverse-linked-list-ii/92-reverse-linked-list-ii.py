# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateK(self, head, k):
        tail = head
        prev = None
        while(head != None and k>0):
            temp = head.next
            head.next = prev
            prev = head
            head = temp
            k -= 1
        newHead = prev
        return [newHead, tail, head]
    
    def lengthOfList(self, head):
        length = 0
        
        while(head != None):
            head = head.next
            length += 1
        return length
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        oldHead = head
        k = right-left+1
        tempLeft = left
        length = self.lengthOfList(head)
        
        while(head != None and left>1):
            tempHead = head
            head = head.next
            left -= 1
        newHead, tail, oldTail = self.rotateK(head, k)
        
        tail.next = oldTail
        if k == length or tempLeft == 1:
            return newHead
        else:
            tempHead.next = newHead
        return oldHead
        