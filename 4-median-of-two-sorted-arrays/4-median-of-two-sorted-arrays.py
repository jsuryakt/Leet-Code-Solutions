class Solution:
#     def findMedian(self, arr):
#         n = len(arr)
        
#         if n == 0:
#             return 0
        
#         if n == 1:
#             return arr[0]
        
#         mid = (n-1)//2
#         idxAftrMid = mid + 1
#         if n%2 == 0:
#             return (arr[mid] + arr[idxAftrMid])/2
#         else:
#             return arr[mid]
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)
        
        len1 = len(nums1)
        len2 = len(nums2)
        
        low = 0
        high = len1
        
        while(low <= high):
            cut1 = (low+high)//2
            cut2 = (len1+len2+1)//2 - cut1
            
            if cut1 == 0:
                l1 = -99999999
            else:
                l1 = nums1[cut1-1]
            
            if cut2 == 0:
                l2 = -99999999
            else:
                l2 = nums2[cut2-1]
            
            if cut1 == len1:
                r1 = 99999999
            else:
                r1 = nums1[cut1]
                
            if cut2 == len2:
                r2 = 99999999
            else:
                r2 = nums2[cut2]
                
            if(l1 <= r2 and l2 <= r1):
                if (len1+len2)%2 == 0:
                    ans = (max(l1,l2) + min(r1,r2))/ 2
                    return ans
                else:
                    return max(l1,l2)
            elif(l1 > r2):
                high -= 1
            else:
                low += 1
        