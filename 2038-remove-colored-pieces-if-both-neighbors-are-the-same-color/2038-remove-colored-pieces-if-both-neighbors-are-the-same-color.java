class Solution {
    public boolean winnerOfGame(String colors) {
        int ans1=0, ans2=0;
        int count1=0, count2=0;

        for (int i=0; i<colors.length(); i++) {
            char ch = colors.charAt(i);

            if (ch == 'A') {
                count1++;

                if (count2 >= 3) {
                    count2 -= 2;
                    ans2 += count2;
                }
                count2 = 0;
            } else {
                count2++;

                if (count1 >= 3) {
                    count1 -= 2;
                    ans1 += count1;
                }
                count1 = 0;
            }
        }

        if (count1 >= 3) {
            count1 -= 2;
            ans1 += count1;
        }
        if (count2 >= 3) {
            count2 -= 2;
            ans2 += count2;
        }
        return ans1 > ans2;
    }
}