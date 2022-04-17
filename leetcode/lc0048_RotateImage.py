# You are given an n x n 2D matrix representing an image, rotate the image 
# by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 
# 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
# Constraints:
#   n == matrix.length == matrix[i].length
#   1 <= n <= 20
#   -1000 <= matrix[i][j] <= 1000
from typing import List
from copy import deepcopy


# Matrix Rotate: O(n^2)
# - rotate groups of 4 cells:
#   [ 0,  1,  2,  3,  4,  5,  6]    [( *,  ?,  ?,)  3,  4,  5,  *]
#   [ 7,  8,  9, 10, 11, 12, 13]    [( 7,  8,  9,) 10, 11, 12,  ?]
#   [14, 15, 16, 17, 18, 19, 20]    [(14, 15, 16,) 17, 18, 19,  ?]
#   [21, 22, 23, 24, 25, 26, 27] => [(21, 22, 23,) 24, 25, 26, 27]
#   [28, 29, 30, 31, 32, 33, 34]    [  ?, 29, 30,  31, 32, 33, 34]
#   [35, 36, 37, 38, 39, 40, 41]    [  ?, 36, 37,  38, 39, 40, 41]
#   [42, 43, 44, 45, 46, 47, 48]    [  *, 43, 44,  45,  ?,  ?,  *]
# - identify 4 corners: (rotate 90 or -90 degree, similar)
#   (i, j)     ...       (j, -1-i)
#   ...        ...             ...
#   (-1-j, i)  ...    (-1-i, -1-j)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range((n+1) // 2):
            for j in  range(n // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[-1-j][i]
                matrix[-1-j][i] = matrix[-1-i][-1-j]
                matrix[-1-i][-1-j] = matrix[j][-1-i]
                matrix[j][-1-i] = tmp


# Transpose and Reverse: O(n^2)
class Solution1:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Transpose around diagonal
        for i in range(1, n):
            for j in  range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse left to right for each row
        for i in range(n):
            for j in  range(n // 2):
                matrix[i][j], matrix[i][-1-j] = matrix[i][-1-j], matrix[i][j]


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(("solution",), [(Solution,), (Solution1,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([[1,2,3],
              [4,5,6],
              [7,8,9]],
             [[7,4,1],
              [8,5,2],
              [9,6,3]]),
            ([[5, 1,  9, 11],
              [2, 4,  8, 10],
              [13,3,  6,  7],
              [15,14, 12, 16]],
             [[15, 13, 2,  5],
              [14, 3,  4,  1],
              [12, 6,  8,  9],
              [16, 7, 10, 11]]),
        ])
        def test_rotate(self, matrix, expected):
            sol = self.solution()  # type:ignore
            matrix2 = deepcopy(matrix)
            sol.rotate(matrix2)
            self.assertEqual(matrix2, expected)

    main()
