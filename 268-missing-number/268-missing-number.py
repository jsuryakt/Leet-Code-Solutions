class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0,len(nums)):
            if i != nums[i]:
                return i
        return len(nums)