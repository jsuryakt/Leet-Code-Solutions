class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 0^1^2^4
        # 0^1^2^3^4
        res = len(nums)
        
        for i in range(len(nums)):
            # 0^1^2^3^4
            res = res^i
            # 0^1^2^4
            res = res^nums[i]
        return res