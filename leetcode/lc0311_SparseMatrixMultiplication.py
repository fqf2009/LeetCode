# Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return
# the result of mat1 x mat2. You may assume that multiplication is always possible.
# Constraints:
#   m == mat1.length
#   k == mat1[i].length == mat2.length
#   n == mat2[i].length
#   1 <= m, n, k <= 100
#   -100 <= mat1[i][j], mat2[i][j] <= 100
from typing import List


# Naive Iteration: O(m*n*k)
# - for matrix multiplication: both matrices must be compatible!
#   len(mat1[0]) = len(mat2), i.e.: columns of mat1 = rows of mat2
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, n, k, k2 = len(mat1), len(mat2[0]), len(mat1[0]), len(mat2)
        assert k == k2

        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for p in range(k):
                    res[i][j] += mat1[i][p] * mat2[p][j]
        
        return res


# List of Lists (or Tuple)
# - What if the matrix is too big to store in the memory, but there are only 
#   a few non-zero elements. How to handle huge space waste. How to store the
#   matrix efficiently and do multiplication. assume we will read those matrices 
#   from an external source.
class Solution1:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def compress(matrix: List[List[int]]) -> List[List[int]]:
            res = [[] for _ in range(len(matrix))]
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] != 0:
                        res[i].append([j, matrix[i][j]])
            return res
                    
        m, n, k, k2 = len(mat1), len(mat2[0]), len(mat1[0]), len(mat2)
        assert k == k2

        res = [[0]*n for _ in range(m)]
        A = compress(mat1)
        B = compress(mat2)
        for m1_row in range(m):
            for m1_col, m1_val in A[m1_row]:        # type:ignore
                for m2_col, m2_val in B[m1_col]:    # type:ignore
                    res[m1_row][m2_col] += m1_val * m2_val

        return res


# Yale Format
#  - RSC - Row Sparse Compression
#  - RSC - Column Sparse Compression
# class Solution2:
#     def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
#         pass


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,), (Solution1,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([[1,0,0],
              [-1,0,3]],
             [[7,0,0],
              [0,0,0],
              [0,0,1]],
             [[7,0,0],
              [-7,0,3]]),
            ([[0]], 
             [[0]], 
             [[0]]),
            ([[1,0],
              [0,0],
              [4,0]],
             [[1,0,1],
              [2,0,0]],
             [[1,0,1],
              [0,0,0],
              [4,0,4]])
        ])
        def test_multiply(self, mat1, mat2, expected):
            sol = self.solution()       # type:ignore
            r = sol.multiply(mat1, mat2)
            self.assertEqual(r, expected)

    main()
