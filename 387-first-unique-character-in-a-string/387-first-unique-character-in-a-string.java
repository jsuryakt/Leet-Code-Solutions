class Solution {
    public int firstUniqChar(String s) {
        int[] charFreq = new int[26];
        for(int i=0; i<s.length(); i++) {
            // 97 ascii for 'a'
            charFreq[s.charAt(i)-97]++;
        }
        for(int i=0; i<s.length(); i++) {
            if(charFreq[s.charAt(i)-97] == 1) {
                return i;
            }
        }
        return -1;
    }
}

// 1 0 1 1 3 0 0 0 0 0 0 1
// a b c d e f g h i j k l