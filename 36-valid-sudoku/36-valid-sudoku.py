class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            sett = set()
            for ch in row:
                if ch != '.':
                    if ch not in sett:
                        sett.add(ch)
                    else:
                        return False
                    
        for i in range(9):
            sett = set()
            for j in range(9):
                colVar = board[j][i]
                if colVar != '.':
                    if colVar not in sett:
                        sett.add(colVar)
                    else:
                        return False
        
        rowStart = 0
        rowEnd = 3
        colStart = 0
        colEnd = 3
        for _ in range(9):
            sett = set()
            for i in range(rowStart, rowEnd):
                for j in range(colStart, colEnd):
                    currBoxEle = board[i][j]
                    if currBoxEle != '.':
                        if currBoxEle not in sett:
                            sett.add(currBoxEle)
                        else:
                            return False
            colStart += 3
            colEnd += 3
            
            if colStart == 9:
                rowStart += 3
                rowEnd += 3
                colStart = 0
                colEnd = 3
        return True
                