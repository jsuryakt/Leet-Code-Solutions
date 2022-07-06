class Solution {
    public int fib(int n) {
        if(n<2) {
            return n;
        }
        // return fib(n-1)+fib(n-2);
        int first = 0;
        int second = 1;
        int temp;
        for(int i=0; i<=n-2; i++) {
            temp = second;
            second = first+second;
            first = temp;
        }
        return second;
    }
}