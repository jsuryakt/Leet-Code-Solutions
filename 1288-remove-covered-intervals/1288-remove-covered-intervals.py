class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        lst = sorted(intervals, key=lambda x:(x[0], -x[1]))
        length = len(lst)
        ans = length
        
        d = lst[0][1]
        
        for i in range(1, length):
            b = lst[i][1]
            
            if b <= d:
                ans -= 1
            else:
                d = b
                
        return ans
#     -------
#       -------------
#       ---
#         -------
#     1 2 3 4 5 6 7 8
    
#     [1,4] [2,8]
#      c d   a b
#     [2,8] [3,6]
#      c d   a b