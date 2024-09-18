class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        int longestLength = 0;
        int start = 0, end = 0;
        while(end < s.length()) {
            char curr = s.charAt(end);
            map.put(curr, map.getOrDefault(curr, 0) + 1);
            while(map.get(curr) > 1) {
                char startCh = s.charAt(start);
                map.put(startCh, map.get(startCh)-1);
                start++;
            }
            longestLength = Math.max(longestLength, end-start+1);
            end++;
        }
        return longestLength;
    }
}