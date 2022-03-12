"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head):
        curr = head
        dic = {None:None}
        while(curr != None):
            dic[curr] = Node(curr.val)
            curr = curr.next
            
        curr = head
        while(curr != None):
            dic[curr].next = dic[curr.next]
            dic[curr].random = dic[curr.random]
            curr = curr.next
        return dic[head]
        