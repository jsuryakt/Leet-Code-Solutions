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
    public boolean isValidBST(TreeNode root) {
        long lowerBound = Integer.MIN_VALUE-1L;
        // System.out.println(Integer.MIN_VALUE +" " +lowerBound+" "+Integer.MAX_VALUE);
        long upperBound = Integer.MAX_VALUE+1L;
        return isValid(lowerBound, upperBound, root);
    }
    public boolean isValid(long lowerBound, long upperBound, TreeNode root) {
        if(root == null) {
            return true;
        }
        
        if(root.val>lowerBound && root.val<upperBound) {
            boolean left = isValid(lowerBound, root.val, root.left);
            boolean right = isValid(root.val, upperBound, root.right);
            
            if(left && right) {
                return true;
            }
        }
        return false;
    }
}