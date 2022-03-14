class Solution:
    def simplifyPath(self, path: str) -> str:
        length = len(path)
        
        afterSplit = path.split('/')
        print(afterSplit)
        top = -1
        stack = []
        
        for ele in afterSplit:
            if ele == "..":
                if top > -1:
                    stack.pop()
                    top -= 1
            elif ele != '' and ele != '.':
                stack.append("/"+ele)
                top += 1
        if stack == []:
            return "/"
        return "".join(stack)