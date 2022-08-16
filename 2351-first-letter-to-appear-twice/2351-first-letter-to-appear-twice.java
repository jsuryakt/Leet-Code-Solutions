class Solution {
    public char repeatedCharacter(String s) {
        int[] charFreq = new int[26];
        int length = s.length();
        int temp = 0;
        for(int i=0; i<length; i++) {
            // 97 ascii for 'a'
            temp = ++charFreq[s.charAt(i)-97];
            if(temp == 2) {
                return s.charAt(i);
            }
        }
        return ' ';
    }
}