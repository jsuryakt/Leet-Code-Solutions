class Solution {
    public boolean isAnagram(String s, String t) {
        int[] charArr = new int[26];
        String smallest = t;
        String other = s;
        if(s.length()<t.length()) {
            smallest = s;
            other = t;
        }
        for(int i=0; i<smallest.length(); i++) {
            charArr[smallest.charAt(i)-'a']++;
        }
        for(int i=0; i<other.length(); i++) {
            charArr[other.charAt(i)-'a']--;
        }
        for(int ele:charArr) {
            if(ele != 0) {
                return false;
            }
        }
        return true;
    }
}