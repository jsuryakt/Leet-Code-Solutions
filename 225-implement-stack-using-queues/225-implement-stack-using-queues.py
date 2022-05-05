class MyStack:

    def __init__(self):
        self.queue = []
        self.topPtr = -1
        
    def push(self, x: int) -> None:
        self.queue.append(x)
        self.topPtr += 1

    def pop(self) -> int:
        self.topPtr -= 1 
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[self.topPtr]

    def empty(self) -> bool:
        if self.topPtr == -1:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()