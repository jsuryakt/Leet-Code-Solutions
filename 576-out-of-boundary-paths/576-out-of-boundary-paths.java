class Solution {
    private int m, n = 0;
    private int mod = 1000000007;
    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        int[][][] memo = new int[m][n][maxMove+1];
        for (int[][] l : memo) for (int[] sl : l) Arrays.fill(sl, -1);
        this.m = m;
        this.n = n;
        return pathHelper(maxMove, startRow, startColumn, memo);
    }
    
    private int pathHelper(int maxMove, int i, int j, int[][][] memo) {
        if(maxMove < 0) return 0;
        if(i<0 || j<0 || i==m || j==n) return 1;
        if(memo[i][j][maxMove] >= 0) return memo[i][j][maxMove];
        
        int top = pathHelper(maxMove-1, i-1, j, memo);
        int bottom = pathHelper(maxMove-1, i+1, j, memo);
        int left = pathHelper(maxMove-1, i, j-1, memo);
        int right = pathHelper(maxMove-1, i, j+1, memo);    
        
        memo[i][j][maxMove] = ((top+bottom)%mod + (left+right)%mod)%mod;
        return memo[i][j][maxMove];
    }
}