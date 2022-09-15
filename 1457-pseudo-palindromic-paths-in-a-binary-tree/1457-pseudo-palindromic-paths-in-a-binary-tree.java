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
    private int count=0;
    public int pseudoPalindromicPaths (TreeNode root) {
        palindromeCheck(root,new HashMap<Integer,Integer>(),null);
        return count;
    }
    public void palindromeCheck(TreeNode root,HashMap<Integer,Integer> map,TreeNode prev)
    {
        if(root==null)
            return;
        
        int val = map.getOrDefault(root.val,0);
        map.put(root.val,val+1);
        
        if(root.left==null && root.right==null)
        {
            int sum=0;
            for(Integer key:map.keySet())
            {
                int value = map.get(key)%2;
                // map.put(key, value);
                sum+=value;
            }
            if(sum==0 || sum==1)
                count++;
            return;
        }
        palindromeCheck(root.left,map,root);
        if(root.left != null)
            map.put(root.left.val,map.get(root.left.val)-1);
        palindromeCheck(root.right,map,root);
        if(root.right!=null)
            map.put(root.right.val,map.get(root.right.val)-1);
    }
}