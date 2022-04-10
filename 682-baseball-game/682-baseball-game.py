class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        
        for char in ops:
            if char == '+':
                firstTop = stack[-1]
                secondTop = stack[-2]
                stack.append(firstTop+secondTop)
            elif char == 'C':
                stack.pop()
            elif char == 'D':
                newTop = stack[-1]*2
                stack.append(newTop)
            else:
                stack.append(int(char))
        ans = 0
        for ele in stack:
            ans += ele
        return ans
                