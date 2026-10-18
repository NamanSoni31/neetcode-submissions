class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row_zero = any(x == 0 for x in matrix[0])
        first_col_zero = any(matrix[i][0] == 0 for i in range(len(matrix)))

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        if first_row_zero == True:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if first_col_zero == True:
            for j in range(len(matrix)):
                matrix[j][0] = 0