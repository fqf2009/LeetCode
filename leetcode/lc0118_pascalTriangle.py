# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers 
# directly above it as shown:
# Constraints:
#   1 <= numRows <= 30
from typing import List


# Iteration
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]*(i+1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]

        return res


# Recursion
class Solution1:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        if n == 1: return [[1]]

        res = self.generate(n - 1)
        prev_row = res[-1]
        curr_row = [1] * n
        for i in range(1, n-1):
            curr_row[i] = prev_row[i-1] + prev_row[i]
        res.append(curr_row)
        return res


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,), (Solution1,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
            (1, [[1]]),
        ])
        def test_generate(self, numRows, expected):
            sol = self.solution()       # type:ignore
            r = sol.generate(numRows)
            self.assertEqual(r, expected)

    main()
