/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return sortHeight(0, nums.length-1, nums);
    }
    
    public TreeNode sortHeight(int l, int r, int[] nums) {
        if(l>r) {
            return null;
        }
        int mid = (l+r)/2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = sortHeight(l, mid-1, nums);
        root.right = sortHeight(mid+1, r, nums);
        return root;
    }
}