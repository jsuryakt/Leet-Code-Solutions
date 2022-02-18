class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = []
        m = len(grid)
        n = len(grid[0])
        for _ in range(m):
            dp.append([0]*n)
        
        dp[0][0] = grid[0][0]
        
        for i in range(1,n):
            dp[0][i] = grid[0][i] + dp[0][i-1]
            
        for i in range(1,m):
            dp[i][0] = grid[i][0] + dp[i-1][0]
            
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])
        
        return dp[m-1][n-1]
            