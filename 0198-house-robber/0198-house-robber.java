class Solution {
    int dp[];
    public int rob(int[] nums) {
        dp = new int[nums.length];
        Arrays.fill(dp, -1);
        return recurs(nums, 0);
    }
    public int recurs(int[] nums, int currIndex) {
        if (currIndex >= nums.length) {
            return 0;
        }
        if (dp[currIndex] != -1) {
            return dp[currIndex];
        }
        int takeIt = dp[currIndex] = nums[currIndex] + recurs(nums, currIndex+2);
        int leaveIt = recurs(nums, currIndex+1);
        dp[currIndex] = Math.max(takeIt, leaveIt);
        return dp[currIndex];
    }
}