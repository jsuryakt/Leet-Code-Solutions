class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ignoreList = [0]*len(s)
        
        stack = []
        top = -1
        
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                stack.append(['(',i])
                top += 1
            elif char == ')':
                if top > -1:
                    stack.pop()
                    top -= 1
                else:
                    ignoreList[i] = 1
        while(top != -1):
            pair = stack.pop()
            ignoreList[pair[1]] = 1
            top -= 1
            
        finalAns = ""
        for i in range(len(s)):
            if ignoreList[i] != 1:
                finalAns += s[i]
        return finalAns
        
            
            