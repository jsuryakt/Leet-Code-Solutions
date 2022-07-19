class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1],[1,1]]
        
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return res
        
        idx = 2
        
        for i in range(1, numRows-1):
            curr = [1]
            for j in range(1, i+1):
                curr.append(res[idx-1][j-1] + res[idx-1][j])
            idx += 1
            curr.append(1)
            res.append(curr)
        
        return res
            
            