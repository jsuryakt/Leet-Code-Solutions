class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        top = -1
        
        for char in s:
            if char == '(' or char =='{' or char =='[':
                stack.append(char)
                top += 1
            else:
                if top > -1:
                    topChar = stack[top]
                    
                    if char == ")" and topChar == "(":
                        stack.pop()
                        top -= 1
                    elif char == "}" and topChar == "{":
                        stack.pop()
                        top -= 1
                    elif char == "]" and topChar == "[":
                        stack.pop()
                        top -= 1
                    else:
                        return False
                else:
                    return False
        if top == -1:                    
            return True
        return False
                    