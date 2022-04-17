# You are given a 2D integer array grid of size m x n, where 
# each cell contains a positive integer.
# A cornered path is defined as a set of adjacent cells with at most one turn. 
# More specifically, the path should exclusively move either horizontally or 
# vertically up to the turn (if there is one), without returning to a previously 
# visited cell. After the turn, the path will then move exclusively in the 
# alternate direction: move vertically if it moved horizontally, and vice versa, 
# also without returning to a previously visited cell.
# The product of a path is defined as the product of all the values in the path.
# Return the maximum number of trailing zeros in the product of a cornered path 
# found in grid.
# Note:
#  - Horizontal movement means moving in either the left or right direction.
#  - Vertical movement means moving in either the up or down direction.
# Constraints:
#   m == grid.length
#   n == grid[i].length
#   1 <= m, n <= 105
#   1 <= m * n <= 105
#   1 <= grid[i][j] <= 1000
from typing import List


# 4-Direction Prefix Sum - T/S: O(m*n), O(m*n)
class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        def count_factor(v, f):
            res = 0
            while v % f == 0:
                v //= f
                res += 1
            return res

        m, n = len(grid), len(grid[0])
        # count the number of factor 2 or 5 in each cell
        # f5 = f2.copy() is wrong, do not copy 2-d array!!!
        f2 = [[0] * n for _ in range(m)]
        f5 = [[0] * n for _ in range(m)]

        # prefix sum of the number of factor 2 or 5
        # left to right, right to left, top to bottom, bottom to top
        s2_lr = [[0] * n for _ in range(m)]
        s2_rl = [[0] * n for _ in range(m)]
        s2_tb = [[0] * n for _ in range(m)]
        s2_bt = [[0] * n for _ in range(m)]
        s5_lr = [[0] * n for _ in range(m)]
        s5_rl = [[0] * n for _ in range(m)]
        s5_tb = [[0] * n for _ in range(m)]
        s5_bt = [[0] * n for _ in range(m)]

        # compute the number of factors
        for i in range(m):
            for j in range(n):
                s2_lr[i][j] = s2_rl[i][j] = s2_tb[i][j] = s2_bt[i][j] = f2[i][j] = count_factor(grid[i][j], 2)

                s5_lr[i][j] = s5_rl[i][j] = s5_tb[i][j] = s5_bt[i][j] = f5[i][j] = count_factor(grid[i][j], 5)

        # compute the prefix sum
        for i in range(0, m):
            for j in range(0, n):
                if j > 0:
                    s2_lr[i][j] += s2_lr[i][j - 1]
                    s5_lr[i][j] += s5_lr[i][j - 1]
                    s2_rl[i][-1 - j] += s2_rl[i][-j]
                    s5_rl[i][-1 - j] += s5_rl[i][-j]
                if i > 0:
                    s2_tb[i][j] += s2_tb[i - 1][j]
                    s5_tb[i][j] += s5_tb[i - 1][j]
                    s2_bt[-1 - i][j] += s2_bt[-i][j]
                    s5_bt[-1 - i][j] += s5_bt[-i][j]

        res = 0
        # at any cell, split into four 90 degree angles (cornered path)
        for i in range(m):
            for j in range(n):  # corner cell is double counted, so subtract f2 and f5
                res = max(
                    res,
                    max(
                        min(s2_lr[i][j] + s2_tb[i][j] - f2[i][j], s5_lr[i][j] + s5_tb[i][j] - f5[i][j]),
                        min(s2_lr[i][j] + s2_bt[i][j] - f2[i][j], s5_lr[i][j] + s5_bt[i][j] - f5[i][j]),
                        min(s2_rl[i][j] + s2_tb[i][j] - f2[i][j], s5_rl[i][j] + s5_tb[i][j] - f5[i][j]),
                        min(s2_rl[i][j] + s2_bt[i][j] - f2[i][j], s5_rl[i][j] + s5_bt[i][j] - f5[i][j]),
                    ),
                )

        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.maxTrailingZeros([[1, 5, 2, 4, 25]])
        print(r)
        assert r == 3

        r = sol.maxTrailingZeros(
            [[23, 17, 15, 3, 20], [8, 1, 20, 27, 11], [9, 4, 6, 2, 21], [40, 9, 1, 10, 6], [22, 7, 4, 5, 3]]
        )
        print(r)
        assert r == 3

        r = sol.maxTrailingZeros([[4, 3, 2], [7, 6, 1], [8, 8, 8]])
        print(r)
        assert r == 0

    unit_test(Solution())
