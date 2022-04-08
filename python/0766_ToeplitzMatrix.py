# Given an m x n matrix, return true if the matrix is Toeplitz.
# Otherwise, return false.
# A matrix is Toeplitz if every diagonal from top-left to
# bottom-right has the same elements.
# Constraints:
#   m == matrix.length
#   n == matrix[i].length
#   1 <= m, n <= 20
#   0 <= matrix[i][j] <= 99
from typing import List


# Find Patterns: O(m*n)
# - diagonal from top-left to bottom-right, which means:
#   - every cell need to the same as its upper-left one.
#   - cells in the first row or the first column, does not need to check.
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False

        return True


if __name__ == "__main__":

    def unit_test(sol):
        matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
        r = sol.isToeplitzMatrix(matrix)
        print(r)
        assert r == True

        matrix = [[1, 2], [2, 1]]
        r = sol.isToeplitzMatrix(matrix)
        print(r)
        assert r == True

    unit_test(Solution())
    