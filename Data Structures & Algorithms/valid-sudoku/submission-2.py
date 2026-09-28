class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.rowDups(board):
            return False
        if not self.boxDupe(board):
            return False
        if not self.colDupes(board):
            return False
        
        return True
    
    def rowDups(self, board: List[List[str]]):
        for i in range(len(board)):
            filtered = [x for x in board[i] if x != "."]
            if(len(filtered) != len(set(filtered))):
                return False
        return True
    
    def boxDupe(self, board: List[List[str]]):
        for i in range(0, 9, 3):
            for j in range(0,9,3):
                box = []
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        val = board[r][c]
                        if val != ".":
                            box.append(val)
                if(len(box) != len(set(box))):
                    return False
        return True

    def colDupes(self, board: List[List[str]]):
        for j in range(9):
            col = [board[i][j] for i in range(9) if board[i][j] != "."]
            if len(col) != len(set(col)):
                return False
        return True