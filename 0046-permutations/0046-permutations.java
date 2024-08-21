class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        recurs(nums, 0, ans);
        return ans;
    }

    public void recurs(int[] nums, int index, List<List<Integer>> ans) {
        if (index == nums.length) {
            List <Integer> curr = new ArrayList<>();
            for (int i = 0; i < nums.length; i++) {
                curr.add(nums[i]);
            }
            ans.add(curr);
            return;
        }
        for (int i=index; i<nums.length; i++) {
            swap(i, index, nums);
            recurs(nums, index + 1, ans);
            swap(i, index, nums);
        }
    }

    private void swap(int i, int j, int[] nums) {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }
}