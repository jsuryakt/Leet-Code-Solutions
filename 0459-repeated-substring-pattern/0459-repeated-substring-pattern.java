class Solution {
    public boolean repeatedSubstringPattern(String s) {
        int length = s.length();
        StringBuilder sb = new StringBuilder();

        for(int i=0; i<length/2; i++) {
            // String temp = s;
            sb.append(s.charAt(i));

            // String subStr = sb.toString();
            if (length%(i+1) != 0) {
                continue;
            }
            if (s.replace(sb.toString(), "") == "") {
                return true;
            }
        }
        return false;
    }
}