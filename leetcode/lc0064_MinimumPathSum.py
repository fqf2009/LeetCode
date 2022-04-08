# Given a m x n grid filled with non-negative numbers, find a path
# from top left to bottom right, which minimizes the sum of all
# numbers along its path.
# Note: You can only move either down or right at any point in time.

# Constraints:
#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 200
#     0 <= grid[i][j] <= 100
from functools import cache
from typing import List


# DP + Recursion + Memo
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            res = grid[i][j]
            if i < m-1 and j < n-1:
                res += min(dp(i+1, j), dp(i, j+1))
            elif i < m-1:
                res += dp(i+1, j)
            elif j < n-1:
                res += dp(i, j+1)
            return res

        m, n = len(grid), len(grid[0])
        return dp(0, 0)


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
        print(r)
        assert r == 7

        r = sol.minPathSum([[1, 2, 3], [4, 5, 6]])
        print(r)
        assert r == 12

    unitTest(Solution())
