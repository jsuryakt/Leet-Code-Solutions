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
        if length == 1:
            return grid
        k = k%(length)
        ans = [0]*rowLen
        for i in range(rowLen):
            ans[i] = [0]*colLen
            
        singleDim = []
        for row in grid:
            for ele in row:
                singleDim.append(ele)
        rotatedSingleDim = self.rotate(singleDim, k)
        for i in range(rowLen):
            for j in range(colLen):
                ans[i][j] = rotatedSingleDim[(i*colLen)+j]
        return ans
        # 2*4 2
        # 10
        # 1 2 3 4 5 6 7 8 9,  k = 4
        # 9 8 7 6 5 4 3 2 1
        # 5 4 3 2 1 9 8 7 6
        # 6 7 8
        # 9 1 2
        # 3 4 5