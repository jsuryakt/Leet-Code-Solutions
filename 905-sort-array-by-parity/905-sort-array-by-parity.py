class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length == 1:
            return nums
        i = 0
        j = 1
        while(i<length and j<length):
            if nums[i]%2 != 0:
                if nums[j]%2 == 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                else:
                    j += 1
            else:
                i += 1
                j += 1
        return nums