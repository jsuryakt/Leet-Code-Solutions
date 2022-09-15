class Solution {
    private int count=0;
    public int pseudoPalindromicPaths (TreeNode root) {
        palindromeCheck(root,new HashMap<Integer,Integer>());
        return count;
    }
    public void palindromeCheck(TreeNode root,HashMap<Integer,Integer> map)
    {
        // left-mid-right
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
                sum+=value;
            }
            if(sum==0 || sum==1)
                count++;
            return;
        }
        palindromeCheck(root.left,map);
        
        if(root.left != null)
            map.put(root.left.val,map.get(root.left.val)-1);
        
        palindromeCheck(root.right,map);
        
        if(root.right!=null)
            map.put(root.right.val,map.get(root.right.val)-1);
    }
}