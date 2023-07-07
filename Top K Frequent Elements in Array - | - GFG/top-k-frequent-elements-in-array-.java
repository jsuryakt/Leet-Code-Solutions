//{ Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;
class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while (T-- > 0) {
            String[] s = br.readLine().trim().split(" ");
            int n = Integer.parseInt(s[0]);
            int[] nums = new int[n];
            for (int i = 0; i < n; i++) {
                nums[i] = Integer.parseInt(s[i + 1]);
            }
            int k = Integer.parseInt(br.readLine().trim());
            Solution obj = new Solution();
            int[] ans = obj.topK(nums, k);
            for (int i = 0; i < ans.length; i++) System.out.print(ans[i] + " ");
            System.out.println();
        }
    }
}

// } Driver Code Ends


class Solution {
    public int[] topK(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int firstHighestVal = -1;
        int firstHighestKey = -1;
        int secondHighestVal = -1;
        int secondHighestKey = -1;
        for (int ele : nums) {
            int currEleFreq = map.getOrDefault(ele, 0)+1;
            map.put(ele, currEleFreq);
            // if (currEleFreq > firstHighestVal) {
            //     firstHighestVal = currEleFreq;
            //     firstHighestKey = ele;
            // } else if (currEleFreq > secondHighestVal) {
            //     secondHighestVal = currEleFreq;
            //     secondHighestKey = ele;
            // }
        }
        int i = 0;
        int[] ans = new int[k];
        List<Map.Entry<Integer, Integer>> entryList = new ArrayList<>(map.entrySet());
        Collections.sort(entryList, (entry1, entry2) -> {
            if (entry2.getValue().equals(entry1.getValue())) {
                return entry2.getKey().compareTo(entry1.getKey()); // Compare keys when values are equal
            }
            return entry2.getValue().compareTo(entry1.getValue()); // Compare values
        });

        for (Map.Entry<Integer, Integer> entry : entryList) {
            ans[i] = entry.getKey();
            i++;
            if (i >= k) {
                break;
            }
        }
        return ans;
    }
}