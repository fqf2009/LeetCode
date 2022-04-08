# Write an efficient algorithm that searches for a value target in an
# m x n integer matrix matrix. This matrix has the following properties:
#  - Integers in each row are sorted from left to right.
#  - The first integer of each row is greater than the last integer of the previous row.
# Constraints:
#   m == matrix.length
#   n == matrix[i].length
#   1 <= m, n <= 100
#   -10^4 <= matrix[i][j], target <= 10^4
from typing import List
import bisect


# Binary search using Python library
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # key is added in Python version 3.10
        # r = bisect.bisect_right(matrix, target, key = lambda x: x[0])
        r = bisect.bisect_right(matrix, [target, 10**8]) - 1
        if r >= 0:
            c = bisect.bisect_left(matrix[r], target)
            if c < n and matrix[r][c] == target:
                return True

        return False


# Binary search
class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j, r = 0, m-1, -1
        while i <= j:
            k = (i + j) // 2
            if matrix[k][0] <= target <= matrix[k][-1]:
                r = k
                break
            if target < matrix[k][0]:
                j -= 1
            else:
                i += 1
        
        if r != -1:
            i, j = 0, n-1
            while i <= j:
                k = (i + j) // 2
                if matrix[r][k] == target:
                    return True
                if target < matrix[r][k]:
                    j -= 1
                else:
                    i += 1

        return False


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3)
        print(r)
        assert r == True

        r = sol.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=8)
        print(r)
        assert r == False

        r = sol.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=0)
        print(r)
        assert r == False

        r = sol.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=100)
        print(r)
        assert r == False

        r = sol.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13)
        print(r)
        assert r == False

        r = sol.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=1)
        print(r)
        assert r == True

        r = sol.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=23)
        print(r)
        assert r == True

        r = sol.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=60)
        print(r)
        assert r == True

    unitTest(Solution())
    unitTest(Solution1())
