class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Integer, Integer> charMap = new HashMap<>();
        for(int idx=0; idx<magazine.length(); idx++) {
            int currChar = getASCII(magazine.charAt(idx));
            charMap.put(currChar, charMap.getOrDefault(currChar, 0)+1);
        }
        
        for(int idx=0; idx<ransomNote.length();idx++) {
            int currChar = getASCII(ransomNote.charAt(idx));
            int charFreq = charMap.getOrDefault(currChar, 0);
            if(charFreq == 0) {
                return false;
            }
            charMap.put(currChar, --charFreq);
        }
        return true;
    }
    
    public int getASCII(char ch) {
        return ch-97;
    }
}