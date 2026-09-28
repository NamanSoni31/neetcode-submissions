class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        d = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def dfs(r, c):
            d.add((r,c))
            for dr, dc in directions: 
                rn = r + dr
                cn = c + dc
                if r in range(rows) and c in range(cols) and board[r][c] == 'O' and (rn,cn) not in d: 
                    d.add((rn,cn))
                    dfs(rn,cn)
            return

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r + 1 == rows or c + 1 == cols or c == 0 or r == 0):
                    dfs(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r,c) not in d: 
                    board[r][c] = 'X'