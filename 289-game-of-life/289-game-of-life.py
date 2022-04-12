from copy import copy, deepcopy
class Solution:
    def getOneAndZero(self, i, j, board):
        rowLen = len(board)
        colLen = len(board[0])
        freqArr = [0,0]
        if i>0:
            freqArr[board[i-1][j]] += 1
            if j>0:
                freqArr[board[i-1][j-1]] += 1
            
            if j<colLen-1:
                freqArr[board[i-1][j+1]] += 1
        if j>0:
            freqArr[board[i][j-1]] += 1
        if j<colLen-1:
            freqArr[board[i][j+1]] += 1
            
        if i<rowLen-1:
            freqArr[board[i+1][j]] += 1
            
            if j<colLen-1:
                freqArr[board[i+1][j+1]] += 1
            
            if j>0: 
                freqArr[board[i+1][j-1]] += 1
        # print(i,j, board[i][j], freqArr)
        return freqArr
            
    def liveOrDie(self, i, j, board):
        zero, one = self.getOneAndZero(i, j, board)
        if board[i][j] == 1:
            if one<2 or one>3:
                return 0
        else:
            if one == 3:
                return 1
        return board[i][j]
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowLen = len(board)
        colLen = len(board[0])
        
        temp = deepcopy(board)
        
        for i in range(rowLen):
            for j in range(colLen):
                board[i][j] = self.liveOrDie(i,j, temp)