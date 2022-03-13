class Solution:
    def rob(self, nums: List[int]) -> int:
#         take = 0
#         skip = 0
        
#         for i in range(len(nums)):
#             takeIt = nums[i] + skip
#             skipIt = max(take, skip)
            
#             take = takeIt
#             skip = skipIt
#         return max(take, skip)
        length = len(nums)
        if length == 1:
            return nums[0]
        dp = [0]*length
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, length):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return dp[length-1]
        