class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        lengthOfFreq = 10001
        freq = [0]*lengthOfFreq
        
        for ele in nums:
            freq[ele] += ele
            
        take = 0
        skip = 0
        
        for i in range(lengthOfFreq):
            takeIt = freq[i] + skip
            skipIt = max(take,skip)
            
            take = takeIt
            skip = skipIt
        return max(take, skip)
            
            
            