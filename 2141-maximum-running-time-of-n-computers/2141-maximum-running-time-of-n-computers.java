class Solution {
    public long maxRunTime(int n, int[] batteries) {
        long min = Integer.MAX_VALUE;
        long sum = 0;
        for(int battery: batteries) {
            min = Math.min(battery, min);
            sum += battery;
        }
        long low = min;
        long high = sum/n;

        while(low<high) {
            // lean towards right if only 2 elements are remaining, 
            // @see Sunil's comment https://leetcode.com/problems/maximum-running-time-of-n-computers/editorial/comments/1989224
            long mid = (low+high+1)/2;
            // if (high-low == 1) {
            //     mid++;
            // }
            if(isFeasible(mid, n, batteries)) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }

    public static boolean isFeasible(long mid, int n, int[] batteries) {
        long totalReqTime = mid*n;

        long totalRuntime = 0;

        for(int battery: batteries) {
            totalRuntime += Math.min(battery, mid);    
        }

        return totalRuntime >= totalReqTime;
    }
}