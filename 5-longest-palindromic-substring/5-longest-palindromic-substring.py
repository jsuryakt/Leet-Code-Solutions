class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            currChar = s[i]
            
            left = i
            right = i
            
            while(left >= 0 and right<len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            
            oddLen = right - left - 1
            
            left = i
            right = i+1
            
            while(left >= 0 and right<len(s) and s[left] == s[right]):
                left -= 1
                right += 1
                
            evenLen = right - left - 1
            
            maxLen = max(evenLen, oddLen)
            
            if maxLen > end-start:
                start = i - (maxLen-1)//2
                end = i + maxLen//2
        return s[start:end+1]
            
                