class Solution {
    public boolean check(int[] nums) {
        // find the breaking point
        // rotate from that point to the end -> reverse
        // also rotate from 0 to the prev point -> reverse
        int length = nums.length;
        for(int i=1; i<length; i++) {
            if(nums[i]<nums[i-1]) {
                reverse(0, i-1, nums);
                reverse(i, length-1, nums);
                reverse(0, length-1, nums);
            }
        }

        return checkIfSorted(nums);
    }
    
    public static void reverse(int start, int end, int[] arr) {
        while(start<end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }

    public static boolean checkIfSorted(int[] arr) {
        if (arr.length <= 0) {
            return true;
        }
        
        for(int i=1; i<arr.length; i++) {
            if(arr[i]<arr[i-1]) {
                return false;
            }
        }
        return true;
    }
}