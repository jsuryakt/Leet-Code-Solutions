class Solution:
    def binarySearch(self, nums, low, high, target):
        while(low<=high):
            mid = (low+high)//2
            
            if nums[mid] == target:
                return True
            elif nums[mid]<target:
                low = mid+1
            else:
                high = mid-1
        return False
    def search(self, nums: List[int], target: int) -> bool:
        if nums[0] == target:
            return True
        for i in range(1,len(nums)):
            if nums[i] == target:
                return True
            if nums[i-1]>nums[i]:
                self.binarySearch(nums, i, len(nums)-1, target)
        return False