class Solution {
    public void rotate(int[][] matrix) {
        // 1 4 7 
        // 2 5 8
        // 3 6 9
        int row = matrix.length;
        int col = matrix[0].length;
        for(int i=0; i<row; i++) {
            for(int j=i; j<col; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for(int i=0; i<row; i++) {
            int j = 0;
            int k = col-1;
            while(j<k) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][k];
                matrix[i][k] = temp;
                j++;
                k--;
            }
        }
    }
}