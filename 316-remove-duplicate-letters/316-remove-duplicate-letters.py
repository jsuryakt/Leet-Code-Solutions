class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = [0]*26
        lastIndex = [0]*26
        
        stack = []
        top = -1
        
        for i in range(len(s)):
            lastIndex[ord(s[i])-97] = i
            
        stack.append(s[0])
        top += 1
        seen[ord(s[0])-97] = 1

        for i in range(1,len(s)):
            curr = ord(s[i])-97
            
            if seen[curr] == 1:
                continue
                
            while top > -1 and s[i] < stack[top] and lastIndex[ord(stack[top])-97] > i:
                seen[ord(stack[top])-97] = 0
                stack.pop()
                top -= 1
            stack.append(s[i])
            top += 1
            seen[curr] = 1
            

        return "".join(stack)
                