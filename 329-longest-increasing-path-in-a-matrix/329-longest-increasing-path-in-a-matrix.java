class Solution {
    public int longestIncreasingPath(int[][] matrix) {
        int max=0;
        boolean[][] visited=new boolean[matrix.length][matrix[0].length];
        int[][] memo=new int[matrix.length][matrix[0].length];
        for(int i=0;i<matrix.length;i++)
            for(int j=0;j<matrix[0].length;j++)
            {
                if(memo[i][j]==0)
                    max=Math.max(max, increase(matrix,visited,i,j,-1,memo));
            }   
        return max;
    }
    
    private int increase(int[][] matrix,boolean[][] visited,int i,int j,int prev,int[][] memo)
    {
        int m=matrix.length;
        int n=matrix[0].length;
        
        int ans=0;
        
        if(i<0 || j<0 || i>=m || j>=n)
            return 0;
        if(matrix[i][j]<=prev)
            return 0;
        
        if(memo[i][j]>0)
            return memo[i][j];
        
        if(!visited[i][j])
        {
        visited[i][j]=true;
        ans=Math.max(ans,1+increase(matrix,visited,i+1,j,matrix[i][j],memo));
        ans=Math.max(ans,1+increase(matrix,visited,i-1,j,matrix[i][j],memo));
        ans=Math.max(ans,1+increase(matrix,visited,i,j+1,matrix[i][j],memo));
        ans=Math.max(ans,1+increase(matrix,visited,i,j-1,matrix[i][j],memo));
        visited[i][j]=false;
        }
        memo[i][j]=ans;
        return ans;
    }
}