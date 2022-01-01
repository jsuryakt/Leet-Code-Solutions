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
    TreeNode prev;
    TreeNode violation1;
    TreeNode violation2;
    public void inorder(TreeNode root) {
        if(root == null)
            return;
        
        inorder(root.left);
        
        if(prev != null){
            if(prev.val > root.val){
                if(violation1 == null)
                    violation1 = prev;
                violation2 = root;
                }
        }
        
        prev = root;
        inorder(root.right);
    }

    public void recoverTree(TreeNode root) {
        inorder(root);
        int temp = violation1.val;
        
        violation1.val = violation2.val;
        violation2.val = temp;
    }
}