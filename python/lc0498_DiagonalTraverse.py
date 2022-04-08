# Given an m x n matrix mat, return an array of all the elements of the array
# in a diagonal order. (change direction for each diagonal scan)
# Example 1:
#   Input: mat = [[1,2,3],
#                 [4,5,6],
#                 [7,8,9]]
#   Output: [1,2,4,7,5,3,6,8,9]
# Constraints:
#   m == mat.length
#   n == mat[i].length
#   1 <= m, n <= 10^4
#   1 <= m * n <= 10^4
#   -10^5 <= mat[i][j] <= 10^5
from typing import List


# Find Patterns - T/S: O(m*n), O(m*n)
# - Collect twice
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        diag = [[] for _ in range (m+n-1)]
        for i in range(m):          # the default scanning order is downward,
            for j in range(n):      # i.e. i, j keep increasing
                diag[i+j].append(mat[i][j])
        
        res = []
        for i in range(m+n-1):
            if i % 2 != 0: 
                res.extend(diag[i])         # odd (0-based) row is downward
            else:
                res.extend(diag[i][::-1])   # even (0-based) row is upward

        return res


# Find Patterns - T/S: O(m*(m+n)), O(m*n)
# Analysis:
# - for each grid cell in diagonal, i.e., mat[i, j],
#   the patterns is: i + j is constant for this diagonal.
#   i+j is increasing from 0, 1, ..., m + n -2.
# !!! Super slow in edge cases, e.g.:
#     for a grid size: 10000 x 1
#           O(m*(m+n)) = m^2  = 10^8,
#           O(m*n) = 10^4 * 1 = 10^4
class Solution1:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        upward = True
        for diag in range(m + n - 1):
            if upward:
                row_range = reversed(range(min(diag + 1, m)))
            else:
                row_range = range(min(diag + 1, m))
            for i in row_range:
                j = diag - i
                if 0 <= j < n:
                    res.append(mat[i][j])
            upward = not upward

        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        print(r)
        assert r == [1, 2, 4, 7, 5, 3, 6, 8, 9]

        r = sol.findDiagonalOrder([[1, 2], [3, 4]])
        print(r)
        assert r == [1, 2, 3, 4]

    unit_test(Solution())
    unit_test(Solution1())
