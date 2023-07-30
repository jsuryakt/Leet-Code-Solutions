class Solution {
    public int removeDuplicates(int[] nums) {
        // go though the array and if ele is not a duplicate then add to sorted section
        // to maintain sorted index and replace with elements
        int sortedIdx = 0;
        // iterate over all and only place into sorted sections if not equal to previous
        for(int i=1; i<nums.length; i++) {
            if(nums[i] != nums[i-1]) {
                nums[sortedIdx++] = nums[i-1];
            }
        }
        // the last element will be left over unique (4) or duplicate (4 4 4), so we add it at the end
        nums[sortedIdx++] = nums[nums.length - 1];
        return sortedIdx;
    }
}