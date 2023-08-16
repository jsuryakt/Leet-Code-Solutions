class Solution {
    public void moveZeroes(int[] nums) {
        int j = 0;
        // iterate through the elements and if not zero then move to the front
        for (int i=0; i<nums.length; i++) {
            if (nums[i] != 0) {
                nums[j++] = nums[i];
            }
        }
        // once all the non zero elements are done moving forward, we replace the rest with all zeroes
        for (; j<nums.length; j++) {
            nums[j] = 0;
        }
    }
}