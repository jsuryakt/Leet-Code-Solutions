class Solution {
    int dp[] = new int[45];
    public int climbStairs(int n) {
        if (n<=2) {
            return n;
        }
        int ways = dp[n-1];
        if (ways == 0) {
            ways = climbStairs(n-1);
            dp[n-1] = ways;
        }
        return ways + climbStairs(n-2);
    }
}