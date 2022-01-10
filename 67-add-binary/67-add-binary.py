class Solution:
    def binaryToDecimal(self, num):
        p = 0
        ans = 0
        for i in range(len(num)-1,-1,-1):
            if num[i] == '1':
                ans += 2**p
            p += 1
        return ans
    
    def decimalToBinary(self, num):
        return bin(num).replace("0b", "")
            
    def addBinary(self, a: str, b: str) -> str:
        aInDecimal = self.binaryToDecimal(a)
        bInDecimal = self.binaryToDecimal(b)
        
        return self.decimalToBinary(aInDecimal+bInDecimal)
        