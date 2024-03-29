class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = ['a']*n
        val = n
        
        for i in range(n-1, -1, -1):    
            if val == k:
                break
            val -= 1
            ans[i] = chr(96 + min(k - val, 26))
            val += ord(ans[i]) - 96
            
        return ''.join(ans) 
        
            