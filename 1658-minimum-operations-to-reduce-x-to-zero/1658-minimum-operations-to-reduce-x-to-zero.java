class Solution {
    public int minOperations(int[] nums, int x) {
	int sum = 0;
	for (int num: nums) 
        sum += num;
    sum -= x;

	int maxLength = -1, currSum = 0;
	for (int l=0, r=0; r<nums.length; r++) {
		currSum += nums[r];
		while (l <= r && currSum > sum) 
            currSum -= nums[l++];
		if (currSum == sum) 
            maxLength = Math.max(maxLength, r-l+1);
	}

	return maxLength == -1 ? -1 : nums.length - maxLength;
}
}