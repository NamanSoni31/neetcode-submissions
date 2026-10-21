class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.rowCheck(board):
            print("ROW CHECK")
            return False
        if not self.colCheck(board):
            print("COL CHECK")
            return False
        if not self.boxCheck(board):
            print("BOX")
            return False
        return True
    
    def rowCheck(self, board):
        for i in range(len(board)):
            d = set()
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if int(board[i][j]) not in d: 
                    d.add(int(board[i][j]))
                else: 
                    return False
        return True
        
    def colCheck(self, board):
        for i in range(len(board[0])):
            d = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                if int(board[j][i]) not in d:
                    d.add(int(board[j][i]))
                else:
                    return False
        return True
    
    def boxCheck(self, board):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):                
                box = set()
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if board[r][c] == ".":
                            continue
                        if board[r][c] in box: 
                            return False
                        box.add(board[r][c])
        
        return True
                        