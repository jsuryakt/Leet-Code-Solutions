"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root
        queue = []
        
        queue.append(root)
        while(queue):
            size = len(queue)
            prev = None
            # for ele in queue:
            #     print(ele.val, end=" ")
            # print()
            while(size > 0):
                curr = queue.pop(0)
                
                if curr == None:
                    break
                if queue:
                    curr.next = queue[0]
                if curr.left != None:
                    queue.append(curr.left)
                if curr.right != None:
                    queue.append(curr.right)
                prev = curr        
                size -= 1
                
            prev.next = None
        return root