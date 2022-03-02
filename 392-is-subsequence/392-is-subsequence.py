class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        for i in range(len(t)):
            if ptr < len(s):
                if t[i] == s[ptr]:
                    ptr += 1
            else:
                break
        if ptr == len(s):
            return True
        return False