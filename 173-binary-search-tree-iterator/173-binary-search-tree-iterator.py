# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    arr = []
    i = -1
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.i = -1
        self.inorder(root)

    def next(self) -> int:
        # print(self.arr)
        self.i += 1
        return self.arr[self.i]

    def hasNext(self) -> bool:
        if self.i < len(self.arr)-1:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()