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
    public String tree2str(TreeNode root) {
        return preorder(root, new StringBuilder()).toString();
    }
    public StringBuilder preorder(TreeNode root, StringBuilder sb) {
        if(root == null) {
            return sb;
        }
        sb.append(root.val);
        boolean flag = false;
        if(root.left == null) {
            if(root.right == null) {
                return sb;
            } else {
                sb.append("()");
                flag = true;
            }
        }
        if(!flag) {
            sb.append("(");
            preorder(root.left, sb);
            sb.append(")");
        }
        if(root.right != null) {
            sb.append("(");
            preorder(root.right, sb);
            sb.append(")");
        }
        return sb;
    }
}