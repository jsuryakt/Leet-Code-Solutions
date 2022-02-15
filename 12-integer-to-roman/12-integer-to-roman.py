class Solution:
    def intToRoman(self, num: int) -> str:
        romanMap = {
            'I':['','I','II','III','IV','V','VI','VII','VIII','IX'],
            'X':['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
            'C':['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
        }
        
        return 'M'*(num//1000) + romanMap['C'][(num//100)%10] + romanMap['X'][(num//10)%10] + romanMap['I'][num%10]
        