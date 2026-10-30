class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        size = len(matrix) * len(matrix[0])
        l = 0
        r = size
        
        while l < r:
            mid = (l + r) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            if target == matrix[row][col]:
                return True
            if target < matrix[row][col]:
                r = mid
            else:
                l = mid + 1

        return False