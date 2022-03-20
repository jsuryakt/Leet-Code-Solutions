class Solution:
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
        map1 = {}
        map2 = {}
        
        for i in range(len(tops)):
            map1[tops[i]] = map1.get(tops[i], 0) + 1
            map2[bottoms[i]] = map2.get(bottoms[i], 0) + 1
        
        maxFreq1 = 0
        maxEle1 = 0
        maxFreq2 = 0
        maxEle2 = 0
        
        for key in map1:
            if map1[key] > maxFreq1:
                maxFreq1 = map1[key]
                maxEle1 = key
        for key in map2:
            if map2[key] > maxFreq2:
                maxFreq2 = map2[key]
                maxEle2 = key
        if maxFreq1 >= maxFreq2:
            ans = self.findSwaps(tops, bottoms, maxFreq1, maxEle1)
        else:
            ans = self.findSwaps(bottoms, tops, maxFreq2, maxEle2)
        return ans
        