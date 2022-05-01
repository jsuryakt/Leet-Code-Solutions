class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        lenStr1 = len(s)
        lenStr2 = len(t)
        
        i = lenStr1-1
        j = lenStr2-1
        hash1 = 0
        hash2 = 0
        
        while(i >= 0 or j >= 0):
            while(i>=0):
                if s[i] == '#':
                    hash1 += 1
                    i -= 1
                elif hash1 >= 1:
                    i -= 1
                    hash1 -= 1
                else:
                    break
            while(j>=0):
                if t[j] == '#':
                    hash2 += 1
                    j -= 1
                elif hash2 >= 1:
                    j -= 1
                    hash2 -= 1
                else:
                    break
            if(i>=0 and j>=0 and s[i] != t[j]):
                return False
            i -= 1
            j -= 1
        if i != j:
            return False
        return True