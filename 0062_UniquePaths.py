# There is a robot on an m x n grid. The robot is initially located 
# at the top-left corner (i.e., grid[0][0]). The robot tries to move 
# to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot  
# can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique 
# paths that the robot can take to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than or 
# equal to 2 * 10^9.
# Constraints:
#   1 <= m, n <= 100
from math import comb
import numpy as np
from functools import cache


# DP + Recursion + Memo
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0: return 0
            if i == 0 and j == 0: return 1
            return dp(i-1, j) + dp(i, j-1)

        if m*n == 1: return 1
        return dp(m-1, n-1)


# BFS Search - Utilize NumPy's fast mathematical operations over arrays
# - T/S: O((m+n)*(m*n), O(m*n)
# - keep moving every cell to the right or down, until all out of board
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        if m*n == 1: return 1
        grid = np.zeros((m, n), np.int64)
        # grid = np.zeros((m, n), object)   # when int64 is not big enough 
        grid[0, 0] = 1
        res = 0
        while True:
            prev = grid.copy()
            grid = prev - prev
            grid[1:] += prev[:-1]
            grid[:, 1:] += prev[:, :-1]
            res += grid[m - 1, n - 1]
            if np.sum(grid) == 0:
                return res


# Math: O(min(m,n))
# Analysis:
# - in (m-1) down steps and (n-1) right steps, to pick either down or right step;
# - total unique pathes are Combination(m+n-2, n-1)
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n: m, n = n, m
        p, q, v1, v2 = 1, 1, m - 1 + n - 1, n - 1
        for _ in range(n - 1):
            p *= v1
            q *= v2
            v1 -= 1
            v2 -= 1

        return p // q


class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m+n-2, n-1)


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.uniquePaths(m=3, n=7)
        print(r)
        assert (r == 28)

        r = sol.uniquePaths(m=1, n=1)
        print(r)
        assert (r == 1)

        r = sol.uniquePaths(m=3, n=2)
        print(r)
        assert (r == 3)

        r = sol.uniquePaths(m=7, n=3)
        print(r)
        assert (r == 28)

        r = sol.uniquePaths(m=3, n=3)
        print(r)
        assert (r == 6)

        r = sol.uniquePaths(m=20, n=18)
        print(r)
        assert (r == 8597496600)

        r = sol.uniquePaths(m=33, n=33)
        print(r)
        assert (r == 1832624140942590534)

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
    unitTest(Solution3())
