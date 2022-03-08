# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        if(head != None):
            slow = head.next
        else:
            return False
        if(head.next != None):
            fast = head.next.next
        else:
            return False
        
        while(slow != fast):
            if(fast != None and fast.next != None):
                fast = fast.next.next
            else:
                break
            if(slow != None):
                slow = slow.next
            else:
                break
        
        if(slow == fast and slow != None and fast != None):
            return True
        else:
            return False