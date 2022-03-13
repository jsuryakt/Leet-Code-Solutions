class Solution:
    def rob(self, nums: List[int]) -> int:
        take = 0
        skip = 0
        
        for i in range(len(nums)):
            takeIt = nums[i] + skip
            skipIt = max(take, skip)
            
            take = takeIt
            skip = skipIt
        return max(take, skip)
        