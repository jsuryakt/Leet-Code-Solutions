class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        length = len(digits)
        
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        lst = []
        if length == 0:
            return lst
        
        if length == 1:
            for ele in dic[digits[0]]:
                lst.append(ele)
            return lst
        
        if length == 2:
            for i in dic[digits[0]]:
                for j in dic[digits[1]]:
                    lst.append(i+j)
            return lst
        
        if length == 3:
            for i in dic[digits[0]]:
                for j in dic[digits[1]]:
                    for k in dic[digits[2]]:
                        lst.append(i+j+k) 
            return lst
        
        if length == 4:
            for i in dic[digits[0]]:
                for j in dic[digits[1]]:
                    for k in dic[digits[2]]:
                        for l in dic[digits[3]]:
                            lst.append(i+j+k+l)
            return lst
                
            