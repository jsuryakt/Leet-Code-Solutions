# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotate(self, curr, k):
        prev = None
        while(curr != None and k>0):
            temp = curr.next
            curr.next = prev
            
            prev = curr
            curr = temp
            k -= 1
        return [prev, curr]
    
    def lengthOfList(self, head):
        length = 0
        curr = head
        while(curr != None):
            length += 1
            curr = curr.next
        return length
            
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = self.lengthOfList(head)
        if k == 0 or length == 0 or length == 1:
            return head
        k = k%length
        if k == 0:
            return head
        prev, curr = self.rotate(head, length+2)
        connect = prev
        # connect = prev.next
        
        # 1 2 3 4 5
        # 5 -> 4 -> 3 -> 2 -> 1
        # 0 1 2
        # 1
        # 0
        # prev will have 5 and curr is none
        prev, curr = self.rotate(prev, k)
        head = prev
        # 5 <- 4 <- 3  2 -> 1
        # prev will have 4 and curr will have 3
        # connect will have 5
        prev, curr = self.rotate(curr, length+2)
        # 5 <- 4 <- 3  1 -> 2
        # prev will have 1 and curr is none
        connect.next = prev
        # 4 -> 5 -> 1 -> 2 -> 3
        # 5 will be connected to 1
        return head

# [2,1,0]
# [0,1,2]
# 0 -> 1 -> 2
# null<-0  null<- 1 <- 2
        