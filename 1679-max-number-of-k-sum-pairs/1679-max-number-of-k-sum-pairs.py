class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = {}
        count = 0
        for ele in nums:
            # print(dic)
            if k-ele in dic and dic[k-ele] != 0:
                dic[k-ele] -= 1
                count += 1
                dic[ele] = dic.get(ele, 0) - 1 
            dic[ele] = dic.get(ele, 0) + 1
        return count