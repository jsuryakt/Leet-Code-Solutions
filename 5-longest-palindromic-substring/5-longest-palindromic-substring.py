# class Solution:
#     allPerms = []
#     def getAllPerms(self, string):
        
#     def longestPalindrome(self, s: str) -> str:
#         def checkPalindrome(self, string):
#             start = 0
#             end = len(string) - 1
            
#             while(start<end):
#                 if string[start] != string[end]:
#                     return False
#                 start += 1
#                 end -= 1
#             return True
        
#         maxLen = -1
#         allPerms = self.getAllPerms(s)
#         for word in allPerms:
#             if checkPalindrome(word):
#                 lengthOfPldrm = len(word)
#                 maxLen = max(maxLen, lengthOfPldrm)

class Solution :
    lo = 0
    maxLen = 0
    def  longestPalindrome(self, s) :
        length = len(s)
        if (length < 2) :
            return s
        i = 0
        while (i < length - 1) :
            self.extendPalindrome(s, i, i)
            # assume odd length, try to extend Palindrome as possible
            self.extendPalindrome(s, i, i + 1)
            i += 1
        return s[self.lo:self.lo + self.maxLen]
    def extendPalindrome(self, s,  j,  k) :
        while (j >= 0 and k < len(s) and s[j] == s[k]) :
            j -= 1
            k += 1
        if (self.maxLen < k - j - 1) :
            self.lo = j + 1
            self.maxLen = k - j - 1