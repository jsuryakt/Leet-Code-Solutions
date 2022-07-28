class Solution {
    public boolean isAnagram(String s, String t) {
        int[] charArr = new int[26];
        for(int i=0; i<s.length(); i++) {
            charArr[s.charAt(i)-'a']++;
        }
        for(int i=0; i<t.length(); i++) {
            charArr[t.charAt(i)-'a']--;
        }
        for(int ele:charArr) {
            if(ele != 0) {
                return false;
            }
        }
        return true;
    }
}