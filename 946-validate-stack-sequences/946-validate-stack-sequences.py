class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        ptr1 = 0
        ptr2 = 0
        stack = []
        top = -1
        
        while(True):
            if ptr2<len(popped):
                if top > -1 and stack[top] == popped[ptr2]:
                        stack.pop()
                        top -= 1
                        ptr2 += 1
                else:
                    if ptr1<len(pushed):
                        stack.append(pushed[ptr1])
                        top += 1
                        ptr1 += 1
                    else:
                        break
            else:
                break
                
        if top == -1:
            return True
        return False
                