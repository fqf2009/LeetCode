# Given an m x n integer matrix matrix, if an element is 0, set its 
# entire row and column to 0's.
# You must do it in place.
# Constraints:
#   m == matrix.length
#   n == matrix[0].length
#   1 <= m, n <= 200
#   -2^31 <= matrix[i][j] <= 2^31 - 1
# Follow up:
#   A straightforward solution using O(mn) space is probably a bad idea.
#   A simple improvement uses O(m + n) space, but still not the best solution.
#   Could you devise a constant space solution?
from typing import List


# T/S: O(m*n), O(m+n)
# - code is cleaner
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        rows, cols = [False] * m, [False] * n   # to clear
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for i in range(m):
            for j in range(n):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0


# T/S: O(m*n), O(1)
# use first row and column to indicate this entire column and row need to fill 0;
# however, must the entire first row and entire first column need special marks.
class Solution1:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row, first_col = False, False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][i] = 0
                    if i == 0: first_row = True
                    if j == 0: first_col = True
            
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row:
            for j in range(1, n):
                matrix[0][j] = 0

        if first_col:
            for i in range(1, m):
                matrix[i][0] = 0


if __name__ == '__main__':
    def unitTest(sol):
        matrix = [[1,1,1],[1,0,1],[1,1,1]]
        expected = [[1,0,1],[0,0,0],[1,0,1]]
        sol.setZeroes(matrix)
        print(matrix)
        assert matrix == expected

        matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        expected = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        sol.setZeroes(matrix)
        print(matrix)
        assert matrix == expected

    unitTest(Solution())
    unitTest(Solution1())
