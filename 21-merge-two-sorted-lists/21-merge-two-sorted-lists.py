# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        finalList = ListNode(0)
        head = finalList
        
        ptr1 = list1
        ptr2 = list2
        
        while(ptr1 != None and ptr2 != None):
            # print(ptr1.val, ptr2.val, head.val)
            if ptr1.val <= ptr2.val:
                node = ListNode(ptr1.val)
                ptr1 = ptr1.next
            else:
                node = ListNode(ptr2.val)
                ptr2 = ptr2.next
            head.next = node
            head = head.next
            
        while(ptr1 != None):
            node = ListNode(ptr1.val)
            head.next = node
            head = head.next
            ptr1 = ptr1.next
        while(ptr2 != None):
            node = ListNode(ptr2.val)
            head.next = node
            head = head.next
            ptr2 = ptr2.next
            
        return finalList.next