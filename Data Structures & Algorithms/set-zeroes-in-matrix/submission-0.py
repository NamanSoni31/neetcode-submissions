class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = []
        cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i not in rows: 
                        rows.append(i)
                    if j not in cols:
                        cols.append(j)
        
        for i in rows:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
        for j in cols:
            for r in range(len(matrix)):
                matrix[r][j] = 0