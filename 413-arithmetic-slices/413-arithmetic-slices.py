class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        curr = 0
        total = 0
        
        for i in range(2,len(nums)):
            if(nums[i]-nums[i-1] == nums[i-1]-nums[i-2]):
                curr += 1
                total += curr
            else:
                curr = 0
        return total