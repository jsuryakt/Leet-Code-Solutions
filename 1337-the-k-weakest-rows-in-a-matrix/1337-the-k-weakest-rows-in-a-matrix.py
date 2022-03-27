class Solution:
    def searchLastOne(self, row):
        low = 0
        high = len(row) - 1
        
        if row[0] == 0:
            return 0
        
        if row[high] == 1:
            return high+1
        
        while(low<high-1):
            mid = (low+high)//2
            
            if row[mid] == 1:
                low = mid
            else:
                high = mid
        
        return low+1
    
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        lst = []
        finalAns = []
        for i in range(len(mat)):
            lastOne = self.searchLastOne(mat[i])
            lst.append([i,lastOne])
        # print(lst)
        ans = sorted(lst, key = lambda x:[x[1],x[0]])[:k]
        # print(ans)
        for ele in ans:
            finalAns.append(ele[0])
        return finalAns
                
        