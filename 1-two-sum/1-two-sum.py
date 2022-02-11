class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for i in range(len(nums)):
            search_ele = target - nums[i]
            
            if search_ele in dic:
                return [dic[search_ele], i]
            dic[nums[i]] = i