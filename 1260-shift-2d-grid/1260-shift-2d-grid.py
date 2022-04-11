class Solution:
    def reverse(self, l, r, arr):
        while(l<r):
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return arr
    
    def rotate(self, lst, k):
        length = len(lst)
        lst = self.reverse(0,length-1, lst)
        lst = self.reverse(0, k-1, lst)
        lst = self.reverse(k, length-1, lst)
        return lst
            
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rowLen, colLen = len(grid), len(grid[0])
        length = rowLen*colLen
        k = k%(length)
            
        singleDim = []
        for row in grid:
            for ele in row:
                singleDim.append(ele)
                
        rotatedSingleDim = self.rotate(singleDim, k)
        
        ans = []
        for i in range(rowLen):
            tmp = []
            for j in range(colLen):
                tmp.append(rotatedSingleDim[(i*colLen)+j])
            ans.append(tmp)
        
        return ans