class Solution {
    public int countVowelStrings(int n) {
        int[] ans = {0};
        helper(n, 0, ans);
        return ans[0];
    }
    
    public static void helper(int n, int start, int[] ans) {
        if(n==0) {
            ans[0]++;
            return;
        }
        for(int i=start;i<5;i++) {
            helper(n-1, i, ans);
        }
    }
}