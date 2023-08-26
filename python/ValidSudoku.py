#leetcode #36
def checkRow(board: List[List[str]], row : int) -> bool: 
    freq = [0] * 10
    for i in range(0, 9, 1):
        if board[row][i] == ".": 
            continue  
        freq[int(board[row][i])] += 1
        if freq[int(board[row][i])] == 2: 
            return False
    return True 

def checkCol(board: List[List[str]], col : int) -> bool: 
    freq = [0] * 10
    for i in range(0, 9, 1):
        if board[i][col] == ".": 
            continue  
        freq[int(board[i][col])] += 1
        if freq[int(board[i][col])] == 2: 
            return False
    return True 

def checkBox(board: List[List[str]], row: int, col: int) -> bool: 
    freq = [0] * 10
    for i in range(0, 3, 1): 
        for j in range(0, 3, 1): 
            if board[row + i][col + j] == ".": 
                continue 
            freq[int(board[row + i][col + j])] += 1 
            if freq[int(board[row + i][col + j])] == 2: 
                return False 
    return True 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row 
        for i in range(0, 9, 1): 
            if not checkRow(board, i): 
                return False 
        
        #check col 
        for i in range(0, 9, 1): 
            if not checkCol(board, i): 
                return False 

        #check "box"
        for i in range(0, 9, 3): 
            for j in range(0, 9, 3): 
                if not checkBox(board, i, j): 
                    return False 

        return True 