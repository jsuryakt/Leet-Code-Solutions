class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        mat = []
        
        for i in range(101):
            row = []
            for j in range(i+1):
                row.append(0)
            mat.append(row)
            
        mat[0][0] = poured
        
        for i in range(100):
            for j in range(i+1):
                if mat[i][j] > 1:
                    extra = mat[i][j] - 1
                    mat[i][j] = 1
                    
                    mat[i+1][j] += extra/2.0
                    mat[i+1][j+1] += extra/2.0
        return mat[query_row][query_glass]
                