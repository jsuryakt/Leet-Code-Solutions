class Solution:
    def binaryToDecimal(self, num):
        return int(num, 2)
    
    def decimalToBinary(self, num):
        return bin(num).replace("0b", "")
            
    def addBinary(self, a: str, b: str) -> str:
        aInDecimal = self.binaryToDecimal(a)
        bInDecimal = self.binaryToDecimal(b)
        
        return self.decimalToBinary(aInDecimal+bInDecimal)
        