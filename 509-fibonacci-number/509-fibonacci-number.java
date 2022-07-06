class Solution {
    public int fib(int n) {
        if(n<2) {
            return n;
        }
        // return fib(n-1)+fib(n-2);
        int first = 0;
        int second = 1;
        int temp;
        for(int i=2; i<=n; i++) {
            temp = second;
            second = first+second;
            first = temp;
        }
        return second;
    }
}