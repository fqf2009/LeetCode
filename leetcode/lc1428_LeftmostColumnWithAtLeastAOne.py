# A row-sorted binary matrix means that all elements are 0 or 1 and each row of 
# the matrix is sorted in non-decreasing order.
# Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of
# the leftmost column with a 1 in it. If such an index does not exist, return -1.
# You can't access the Binary Matrix directly. You may only access the matrix 
# using a BinaryMatrix interface:
# - BinaryMatrix.get(row, col) returns the element of the matrix at index
#   (row, col) (0-indexed).
# - BinaryMatrix.dimensions() returns the dimensions of the matrix as a 
#   list of 2 elements [rows, cols], which means the matrix is rows x cols.
# Submissions making more than 1000 calls to BinaryMatrix.get will be judged 
# Wrong Answer. Also, any solutions that attempt to circumvent the judge will 
# result in disqualification.
# For custom testing purposes, the input will be the entire binary matrix mat. 
# You will not have access to the binary matrix directly.
# Constraints:
#   rows == mat.length
#   cols == mat[i].length
#   1 <= rows, cols <= 100
#   mat[i][j] is either 0 or 1.
#   mat[i] is sorted in non-decreasing order.


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
    def __init__(self, matrix) -> None:
        self.matrix = matrix

    def get(self, row: int, col: int) -> int:
        return self.matrix[row][col]

    def dimensions(self) -> list[int]:
        return [len(self.matrix), len(self.matrix[0])]


# Logic: O(m+n)
# Analysis
# - Because each row is sorted, so 0s are always at the left side, and 
#   1s are at the right side;
# - Starting from top, right corner fo the matrix, if cell value is 1,
#   go left, until hit 0, then go down, until hit 1, then go left.
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        res = -1
        i, j = 0, n-1
        while i < m and j >= 0:
            if binaryMatrix.get(i, j) == 1:
                res = j
                j -= 1
            else:
                i += 1
        
        return res


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([[0,0],[1,1]], 0),
            ([[0,0],[0,1]], 1),
            ([[0,0],[0,0]], -1),
        ])
        def test_leftMostColumnWithOne(self, mat, expected):
            sol = self.solution()       # type:ignore
            matrix = BinaryMatrix(mat)
            r = sol.leftMostColumnWithOne(matrix)
            self.assertEqual(r, expected)

    main()
