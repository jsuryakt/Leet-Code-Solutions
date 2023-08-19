class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int expectedTotalSum = n*(n+1)/2;

        int actualTotalSum = 0;
        for(int ele:nums) {
            actualTotalSum += ele;
        }
        return expectedTotalSum-actualTotalSum;
    }
}