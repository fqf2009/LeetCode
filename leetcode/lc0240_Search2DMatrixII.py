# Write an efficient algorithm that searches for a value target in 
# an m x n integer matrix matrix. This matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Constraints:
#   m == matrix.length
#   n == matrix[i].length
#   1 <= n, m <= 300
#   -10^9 <= matrix[i][j] <= 10^9
#   All the integers in each row are sorted in ascending order.
#   All the integers in each column are sorted in ascending order.
#   -10^9 <= target <= 10^9
from bisect import bisect_left
from typing import List


# Brute force: O(m*n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(y == target for x in matrix for y in x)


# Binary Search: O(x*log(x)), where x = max(m, n)
# Analysis:
# - Iterate over diagonally: 0,0 -> 1,1 -> ... -> x-1,x-1 ; where x = min(m, n)
# - Binary search row:    matrix[i, 0] ~ matrix[i, i] and,
#                 column: matrix[0, i] ~ matrix[i, i]
#   [1,  4, 7,11, | 15]
#   [2,  5, 8,12, | 19]
#   [3,  6, 9,16, | 22]
#   [10,13,14,17, v 24]
#   ---------->  
#   [18,21,23,26,   30]
# - if not found, binary search remaining rows (m>n) or column (m<n)
class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(min(m, n)):
            if matrix[i][i] == target: return True
            if i > 0:
                j = bisect_left(matrix[i], target, 0, i)
                if j < i and matrix[i][j] == target: return True
                j = bisect_left([matrix[k][i] for k in range(i-1)], target)
                if j < i and matrix[j][i] == target: return True

        if m < n:
            for i in range(m, n):
                j = bisect_left([matrix[k][i] for k in range(m)], target)
                if j < m and matrix[j][i] == target: return True
        elif m > n:
            for i in range(n, m):
                j = bisect_left(matrix[i], target)
                if j < n and matrix[i][j] == target: return True

        return False


if __name__ == '__main__':
    def unitTest(sol):
        matrix = [[1,  4, 7,11,15],
                  [2,  5, 8,12,19],
                  [3,  6, 9,16,22],
                  [10,13,14,17,24],
                  [18,21,23,26,30]]

        r = sol.searchMatrix(matrix, 5)
        print(r)
        assert r == True

        r = sol.searchMatrix(matrix, 20)
        print(r)
        assert r == False

        matrix = [[1,  4, 7,11,15],
                  [2,  5, 8,12,19],
                  [3,  6, 9,16,22],
                  [10,13,14,17,24],
                  [18,21,23,26,30],
                  [19,22,25,28,33]]
        r = sol.searchMatrix(matrix, 25)
        print(r)
        assert r == True

    unitTest(Solution())
    unitTest(Solution1())
