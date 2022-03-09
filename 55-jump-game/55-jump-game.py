class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        maxReach = 0
        
        for i in range(len(nums)-1):
            maxReach = max(maxReach, i+nums[i])
            
            if maxReach == i:
                return False
        if maxReach >= len(nums)-1:
            return True
        return False