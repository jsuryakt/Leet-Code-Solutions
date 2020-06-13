class Solution:
    def searchInsert(self, nums, target) -> int:
        l,r = 0,len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
                break
            elif target > nums[mid]:
                l = mid+1
            elif target < nums[mid]:
                r = mid-1
        return l   