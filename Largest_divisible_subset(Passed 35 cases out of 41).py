class Solution:
    def largestDivisibleSubset(self, nums):
        if  nums == []:
            return nums
        else:
            nums.sort()
            final = []
            for ele in nums:
                new = [ele]
                for i in range(1,len(nums)):
                    count = 0
                    for j,ele in enumerate(new):
                        if nums[i]%ele == 0:
                            count += 1
                    if count == j+1:
                        new.append(nums[i])
                final.append(set(new))
                ans = sorted(final,key = len)[-1]
            return sorted(list(ans))
        
        