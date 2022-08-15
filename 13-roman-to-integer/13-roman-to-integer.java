class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
        int i;
        int num = 0;
        for(i=1; i<s.length(); i++) {
            int prev = map.get(s.charAt(i-1));
            int curr = map.get(s.charAt(i));
            
            if(prev<curr) {
                num -= prev;
            } else {
                num += prev;
            }
        }
        num+=map.get(s.charAt(i-1));
        return num;
    }
}