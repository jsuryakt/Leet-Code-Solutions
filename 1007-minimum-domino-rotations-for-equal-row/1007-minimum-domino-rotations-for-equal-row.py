class Solution:
    # O(n)
    def findSwaps(self, arr1, arr2, freq, ele):
        swaps = 0
        count = 0
        for i in range(len(arr1)):
            curr = arr1[i]
            if curr != ele:
                if ele == arr2[i]:
                    swaps += 1
            else:
                count += 1
        if swaps == 0 and count != len(arr1) or swaps+freq != len(arr1):
            return -1
        return swaps
                
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        length = len(tops)
        map1 = [0]*7
        map2 = [0]*7
        
        # O(n)
        for i in range(length):
            map1[tops[i]] = map1[tops[i]] + 1
            map2[bottoms[i]] = map2[bottoms[i]] + 1
        
        maxFreq1 = 0
        maxEle1 = 0
        maxFreq2 = 0
        maxEle2 = 0
        
        # O(7*1) - O(1)
        for i in range(1,7):
            if map1[i] > maxFreq1:
                maxFreq1 = map1[i]
                maxEle1 = i
            if map2[i] > maxFreq2:
                maxFreq2 = map2[i]
                maxEle2 = i

        if maxFreq1 >= maxFreq2:
            ans = self.findSwaps(tops, bottoms, maxFreq1, maxEle1)
        else:
            ans = self.findSwaps(bottoms, tops, maxFreq2, maxEle2)
        return ans
        
        # TC - O(5n) - O(n)
        # SC - O(2n) - O(n)