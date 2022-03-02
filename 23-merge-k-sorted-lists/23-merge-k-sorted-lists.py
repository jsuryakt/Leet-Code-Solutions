# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import *

class Pair:
    def __init__(self, li, di, val):
        self.li = li
        self.di = di
        self.val = val
        
    def __lt__(self, other):
        return self.val < other.val
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        heap = []
        for i in range(len(lists)):
            if(lists[i] != None):
                p = Pair(i, lists[i], lists[i].val)
                heap.append(p)  
        
        heapify(heap)
        
        while(heap):
            pair = heappop(heap)
            tail.next = ListNode(pair.val)
            tail = tail.next
            if(pair.di.next != None):
                pair.di = pair.di.next
                pair.val = pair.di.val
                heappush(heap, pair)
        return dummy.next
            