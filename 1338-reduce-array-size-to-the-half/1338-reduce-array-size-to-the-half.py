class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        map = {}
        for ele in arr:
            map[ele] = map.get(ele, 0) + 1
        lst = sorted(map.items(), key=lambda x:x[1], reverse=True)
        
        summ = 0
        count = 0
        length = len(arr)//2
        while True:
            # print(summ, count, length)
            if summ >= length:
                return count
            else:
                summ += lst[count][1]
                count += 1
        return 0
#         3 - 4
#         5 - 3
#         2 - 2
#         7 - 1
#         summ = 0
#        summ >= 10//2
# else
#     4+3
#     count++
        