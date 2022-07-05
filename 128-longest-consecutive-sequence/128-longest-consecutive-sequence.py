class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        max_count = 0
        
        for ele in nums_set:
            if (ele-1 not in nums_set):
                curr_ele = ele
                count = 1
                
                while curr_ele+1 in nums_set:
                    count += 1
                    curr_ele += 1
                    
                max_count = max(count, max_count)
                
        return max_count
                    