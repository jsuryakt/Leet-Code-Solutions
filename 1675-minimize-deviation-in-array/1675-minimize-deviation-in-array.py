import heapq
class Solution:
    def findMinMaxIdx(self, nums):
        minnIdx = 0
        maxxIdx = 0
        for i in range(len(nums)):
            ele = nums[i]
            if ele > nums[maxxIdx]:
                maxxIdx = i
            if ele < nums[minnIdx]:
                minnIdx = i
        return [minnIdx, maxxIdx]
    
    def isEven(self, num):
        return num%2 == 0
    
    def isOdd(self, num):
        return num%2 != 0
    
    def minimumDeviation(self, nums: List[int]) -> int:
        minEle, maxEle, ans = 9999999999, -999999999, 999999999
        
        for i in range(len(nums)):
            if self.isOdd(nums[i]):
                nums[i] = nums[i] * 2
            if nums[i] < minEle:
                minEle = nums[i]
            nums[i] = nums[i] * -1
        
        heapq.heapify(nums)
    
        while(self.isEven(nums[0])):
            heapMax = heapq.heappop(nums) * -1
            
            ans = min(ans, heapMax - minEle)
                
            heapMax = heapMax//2
            
            if heapMax < minEle:
                minEle = heapMax

            heapq.heappush(nums, -1*heapMax)
                
        heapMax = heapq.heappop(nums) * -1
        ans = min(ans, heapMax - minEle)
        return ans