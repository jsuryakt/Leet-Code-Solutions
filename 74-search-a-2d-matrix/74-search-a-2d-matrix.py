class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m*n - 1
        
        while(low <= high):
            mid = (low+high)//2
            ele = matrix[mid//n][mid%n]
            
            if ele == target:
                return True
            elif ele < target:
                low = mid + 1
            else:
                high = mid - 1
        return False