class Solution {
    public int countGoodRectangles(int[][] rectangles) {
        int row = rectangles.length;
        int[] maxLen = new int[row];
        int maxi = 0;
        int count = 0;

        for (int i=0; i<row; i++) {
            maxLen[i] = Math.min(rectangles[i][0], rectangles[i][1]);
            if (maxLen[i] > maxi) {
                maxi = maxLen[i];
                count = 1;
            } else if (maxLen[i] == maxi) {
                count++;
            }
        }
        return count;
    }
}