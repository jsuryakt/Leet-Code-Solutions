class Solution:
    def findMedian(self, arr):
        n = len(arr)
        
        if n == 0:
            return 0
        
        if n == 1:
            return arr[0]
        
        mid = (n-1)//2
        idxAftrMid = mid + 1
        if n%2 == 0:
            return (arr[mid] + arr[idxAftrMid])/2
        else:
            return arr[mid]
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        finalArr = nums1+nums2
        finalArr.sort()
        return self.findMedian(finalArr)
        
#         firstArrMedian = self.findMedian(nums1)
        
#         secArrMedian = self.findMedian(nums2)
        
#         if firstArrMedian > 0:
#             if secArrMedian > 0:
#                 return self.findMedian([firstArrMedian, secArrMedian])
#             else:
#                 return firstArrMedian
#         else:
#             return secArrMedian