class Solution {
    // max is 37, but we do n-3 so 34, but again we add by 2, 
    // can go to 36, +1 for index 0
    int[] dp = new int[37];
    public int tribonacci(int n) {
        if (n<=0) {
            return 0;
        }
        if (n<=2) {
            return 1;
        }
        n = n-3;
        int ans = dp[n+2];
        if (ans == 0) {
            ans = tribonacci(n+2);
            dp[n+2] = ans;
        }
        return ans + tribonacci(n+1) + tribonacci(n);
    }
}