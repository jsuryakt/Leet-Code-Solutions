class Solution {
    List<List<Integer>> ans;
    public List<List<Integer>> subsets(int[] nums) {
        ans = new ArrayList<>();
        recurs(nums, 0, new ArrayList<>());
        return ans;
    }

    public void recurs(int[] nums, int index, List<Integer> temp) {
        if (index >= nums.length) {
            ans.add(new ArrayList<>(temp));
            return;
        }
        temp.add(nums[index]);
        recurs(nums, index+1, temp);
        // System.out.println(temp);
        temp.remove(temp.size()-1);
        recurs(nums, index+1, temp);  
    }
}