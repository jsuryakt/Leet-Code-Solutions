class Solution {
    public void rotate(int[] nums, int k) {
        // if k is greater than nums.length then end can be out of bound in reverse, so we mod to reduce the rotation which is the same
        // if k is 3 or 13, and length is 10, we only need to move 3 places, since after 10 moves we'll end up in the same place
        k = k%nums.length;
        reverse(0, nums.length-1, nums);
        reverse(0, k-1, nums);
        reverse(k, nums.length-1, nums);
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
}