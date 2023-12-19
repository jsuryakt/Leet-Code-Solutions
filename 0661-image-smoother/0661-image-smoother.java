class Solution {
    public int[][] imageSmoother(int[][] img) {
        int row = img.length;
        int col = img[0].length;
        int[][] ans = new int[row][col];

        for (int i=0; i<row; i++) {
            for (int j=0; j<col; j++) {
                int sum = 0;
                int count = 0;
                if (i-1 >= 0) {
                    // top left
                    if (j-1 >= 0) {
                        sum += img[i-1][j-1];
                        count++;
                    }
                    // top
                    if (j >= 0) {
                        sum += img[i-1][j];
                        count++;
                    }
                    // top right
                    if (j+1 < col) {
                        sum += img[i-1][j+1];
                        count++;
                    }
                }
                // current left
                if (j-1 >= 0) {
                    sum += img[i][j-1];
                    count++;
                }
                // current
                sum += img[i][j];
                count++;
                // current right
                if (j+1 < col) {
                    sum += img[i][j+1];
                    count++;
                }

                if (i+1 < row) {
                    // bottom left
                    if (j-1 >= 0) {
                        sum += img[i+1][j-1];
                        count++;
                    }
                    // bottom
                    if (j >= 0) {
                        sum += img[i+1][j];
                        count++;
                    }
                    // bottom right
                    if (j+1 < col) {
                        sum += img[i+1][j+1];
                        count++;
                    }
                }
                ans[i][j] = sum/count;
            }
        }
        return ans;
    }
}