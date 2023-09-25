class Solution {
    public char findTheDifference(String s, String t) {
        char charSum = 0;
        for (int i=0; i<t.length(); i++) {
            charSum += t.charAt(i);
        }

        for (int i=0; i<s.length(); i++) {
            charSum -= s.charAt(i);
        }

        return charSum;
    }
}