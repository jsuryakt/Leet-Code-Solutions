class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        i = 0
        chainStart = nums[0]
        chainEnd = nums[0]
        ans = []
        
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                chainEnd = nums[i+1]
            else:
                if chainStart != chainEnd:
                    ans.append(str(chainStart)+"->"+str(chainEnd))
                else:
                    ans.append(str(chainStart))
                chainStart = nums[i+1]
                chainEnd = nums[i+1]
        if chainStart != chainEnd:
            ans.append(str(chainStart)+"->"+str(chainEnd))
        else:
            ans.append(str(chainStart))
        return ans