class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> charMap = new HashMap<>();
        for(int idx=0; idx<magazine.length(); idx++) {
            char currChar = magazine.charAt(idx);
            charMap.put(currChar, charMap.getOrDefault(currChar, 0)+1);
        }
        
        for(int idx=0; idx<ransomNote.length();idx++) {
            char currChar = ransomNote.charAt(idx);
            int charFreq = charMap.getOrDefault(currChar, 0);
            if(charFreq == 0) {
                return false;
            }
            charMap.put(currChar, --charFreq);
        }
        return true;
    }
}