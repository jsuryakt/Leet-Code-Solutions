class Solution {
    public boolean reorderedPowerOf2(int n) {
        //   1  1    2
        // 0 1 2 3 4 5 6 7 8 9
        int[] intFreq = getFreqArr(n);
        StringBuilder temp = new StringBuilder();
        for(int i=9; i>=0; i--) {
            int freq = intFreq[i];
            while(freq-->0) {
                temp.append(i);
            }
        }
        int maxNum = Integer.parseInt(temp.toString());
        int pow = 1;
        while(pow<=maxNum) {
            int[] freq1 = getFreqArr(pow);
            if(compare2Freqs(freq1, intFreq)) {
                return true;
            }
            pow = pow*2;
        }
        return false;
    }
    public int[] getFreqArr(int n) {
        int ans = 0;
        int[] freq = new int[10];
        while(n>0) {
            int rem = n%10;
            ++freq[rem];
            n = n/10;
        }
        return freq;
    }
    public boolean compare2Freqs(int[] freq1, int[] freq2) {
        for(int i=0; i<10; i++) {
            if(freq1[i]!=freq2[i]) {
                return false;
            }
        }
        return true;
    }
}