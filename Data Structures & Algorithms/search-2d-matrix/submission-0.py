class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = matrix
        rows = matrix[0]
        for i in range(len(cols)):
            for j in range(len(rows)):
                if target == matrix[i][j]:
                    return True
        return False