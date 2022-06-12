class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        int l = 0, r = 0;
        HashSet<Integer> set = new HashSet<>();
        int ans = 0;
        int max = Integer.MIN_VALUE;
        while(r < nums.length) {
            if(!set.contains(nums[r])) {
                ans += nums[r];
                max = Math.max(max, ans);
                set.add(nums[r++]);
            } else {
                while(nums[r]!=nums[l]) {
                    ans -= nums[l];
                    set.remove(nums[l++]);
                }
                l++;
                r++;
            }
        }
        return max;
    }
}