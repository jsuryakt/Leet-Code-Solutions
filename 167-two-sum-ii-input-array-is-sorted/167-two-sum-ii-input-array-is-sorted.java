class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int ptr1 = 0;
        int ptr2 = numbers.length-1;
        
        while(true) {
            int sum = numbers[ptr1]+numbers[ptr2];
            if(sum == target) {
                return new int[]{ptr1+1, ptr2+1};
            } else if(sum > target) {
                ptr2--;
            } else {
                ptr1++;
            }
        }
    }
}