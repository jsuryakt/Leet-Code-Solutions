class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int ptr1 = m-1;
        int ptr2 = n-1;
        int sortPtr = m+n-1;
        while(ptr1 >= 0 && ptr2 >= 0) {
            if(nums1[ptr1] > nums2[ptr2]) {
                nums1[sortPtr] = nums1[ptr1];
                ptr1--;
            } else {
                nums1[sortPtr] = nums2[ptr2];
                ptr2--;
            }
            sortPtr--;
        }
        while(ptr2 >= 0){
            nums1[sortPtr] = nums2[ptr2];
            ptr2--;
            sortPtr--;
        }
    }
}