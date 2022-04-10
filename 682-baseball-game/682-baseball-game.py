class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        top = -1
        
        for char in ops:
            if char == '+':
                firstTop = stack[-1]
                secondTop = stack[-2]
                stack.append(firstTop+secondTop)
                top -= 1
            elif char == 'C':
                stack.pop()
                top -= 1
            elif char == 'D':
                newTop = stack[-1]*2
                stack.append(newTop)
                top += 1
            else:
                stack.append(int(char))
                top += 1
            # print(stack)
        ans = 0
        for ele in stack:
            ans += ele
        return ans
                