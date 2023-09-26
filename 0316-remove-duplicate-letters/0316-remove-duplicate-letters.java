class Solution {
    /**
     * @see for detailed explaination https://leetcode.com/problems/remove-duplicate-letters/solutions/1859410/java-c-detailed-visually-explained/
     */
    public String removeDuplicateLetters(String s) {
        // to check if the char will appear in future
        int[] lastIndex = new int[26];
        // to check if the char is already in the ans
        int[] seen = new int[26];

        for (int i=0; i<s.length(); i++) {
            lastIndex[getIntVal(s.charAt(i))] = i;
        }

        Stack<Character> stack = new Stack();

        for (int i=0; i<s.length(); i++) {
            char currChar = s.charAt(i);

            // if curr char is already in ans, then skip and go to next char
            if (seen[getIntVal(currChar)] == 1) {
                continue;
            }
            // if curr char is less than stack top and the if stack top char will also appear in future, 
            // then remove it from stack and also from seen, since we removed from stack
            while (stack.size() != 0 && currChar < stack.peek() && lastIndex[getIntVal(stack.peek())] > i) {
                seen[getIntVal(stack.peek())] = 0;
                stack.pop();
            }
            // if stack is empty or we got our smallest char from sequence, we add it to stack and set it as seen
            stack.push(currChar);
            seen[getIntVal(currChar)] = 1;
        }

        String ans = "";
        for(int i = 0; i < stack.size(); i++){
            ans += stack.get(i);
        }
        return ans;
    }

    public static int getIntVal(char ch) {
        return ch-'a';
    }
}