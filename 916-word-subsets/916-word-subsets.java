class Solution {
    public List<String> wordSubsets(String[] words1, String[] words2) {
        int[] constantWord2 = new int[26];
        for (String word: words2) {
            int[] bCount = getCharFreqArr(word);
            for (int i = 0; i < 26; ++i)
                constantWord2[i] = Math.max(constantWord2[i], bCount[i]);
        }
        
        List<String> ans = new ArrayList<String>();
        for(String word:words1) {
            int[] variableWord1 = getCharFreqArr(word);
            int count = 0;
            for(int i=0; i<26; i++) {
                if(constantWord2[i]<=variableWord1[i]) {
                    count++;
                }
            }
            if(count==26) {
                ans.add(word);
            }
        }
        return ans;
    }
    
    public int[] getCharFreqArr(String word) {
        int[] charArr = new int[26];
        for(int i=0; i<word.length(); i++) {
            charArr[word.charAt(i)-97]++;
        }
        return charArr;
    }
}