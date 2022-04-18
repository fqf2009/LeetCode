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
from itertools import accumulate
from typing import List
from copy import deepcopy


# 4-Direction Prefix Sum - T/S: O(m*n), O(m*n)
# - use 3-d array, i.e. each counting cell is list of [nb_factor_2, nb_factor_5]
# - however, the code is not simplified as expected
class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        def count_factor(v, f):
            res = 0
            while v % f == 0:
                v //= f
                res += 1
            return res

        m, n = len(grid), len(grid[0])

        # count the number of factor 2 or 5 in each cell: [nb_factor_2, nb_factor_5]
        factors = [[[count_factor(grid[i][j], 2), count_factor(grid[i][j], 5)]
                        for j in range(n)] for i in range(m)]

        # compute the prefix sum of the number of factor 2 or 5
        LR, RL = deepcopy(factors), deepcopy(factors) # left to right, right to left
        TB, BT = deepcopy(factors), deepcopy(factors) # top to bottom, bottom to top
        for i in range(m):
            for j in range(n):
                if j > 0:
                    LR[i][j][0] += LR[i][j - 1][0]
                    LR[i][j][1] += LR[i][j - 1][1]
                    RL[i][-1-j][0] += RL[i][-j][0]
                    RL[i][-1-j][1] += RL[i][-j][1]
                if i > 0:
                    TB[i][j][0] += TB[i - 1][j][0]
                    TB[i][j][1] += TB[i - 1][j][1]
                    BT[-1-i][j][0] += BT[-i][j][0]
                    BT[-1-i][j][1] += BT[-i][j][1]

        # return the min(the total count of 2's, the total count of 5's)
        def count_zeros(prefix_sum1, prefix_sum12, cell_factors):
            # corner cell is double counted, so subtract this cell's factor count
            return min(ps1 + ps2 - f for ps1, ps2, f in zip(prefix_sum1, prefix_sum12, cell_factors))

        max_zeros = 0
        # at any cell, split into four 90 degree angles (cornered path)
        for i in range(m):
            for j in range(n):  
                max_zeros = max(max_zeros, count_zeros(LR[i][j], TB[i][j], factors[i][j]),
                                           count_zeros(LR[i][j], BT[i][j], factors[i][j]),
                                           count_zeros(RL[i][j], TB[i][j], factors[i][j]),
                                           count_zeros(RL[i][j], BT[i][j], factors[i][j]))

        return max_zeros


# 4-Direction Prefix Sum - T/S: O(m*n), O(m*n)
class Solution1:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        def count_factor(v, f):
            res = 0
            while v % f == 0:
                v //= f
                res += 1
            return res

        m, n = len(grid), len(grid[0])

        # count the number of factor 2 or 5 in each cell
        f2 = [[count_factor(grid[i][j], 2) for j in range(n)] for i in range(m)]
        f5 = [[count_factor(grid[i][j], 5) for j in range(n)] for i in range(m)]

        # prefix sum of the number of factor 2 or 5
        # left to right, right to left, top to bottom, bottom to top
        LR2, RL2, TB2, BT2  = deepcopy(f2), deepcopy(f2), deepcopy(f2), deepcopy(f2)
        LR5, RL5, TB5, BT5  = deepcopy(f5), deepcopy(f5), deepcopy(f5), deepcopy(f5)

        # compute the prefix sum
        for i in range(m):
            for j in range(n):
                if j > 0:
                    LR2[i][j] += LR2[i][j - 1]
                    LR5[i][j] += LR5[i][j - 1]
                    RL2[i][-1 - j] += RL2[i][-j]
                    RL5[i][-1 - j] += RL5[i][-j]
                if i > 0:
                    TB2[i][j] += TB2[i - 1][j]
                    TB5[i][j] += TB5[i - 1][j]
                    BT2[-1 - i][j] += BT2[-i][j]
                    BT5[-1 - i][j] += BT5[-i][j]

        res = 0
        for i in range(m):      # at any cell, split into four 90 degree angles (cornered path)
            for j in range(n):  # corner cell is double counted, so subtract f2 and f5
                res = max(res, min(LR2[i][j] + TB2[i][j] - f2[i][j], LR5[i][j] + TB5[i][j] - f5[i][j]),
                               min(LR2[i][j] + BT2[i][j] - f2[i][j], LR5[i][j] + BT5[i][j] - f5[i][j]),
                               min(RL2[i][j] + TB2[i][j] - f2[i][j], RL5[i][j] + TB5[i][j] - f5[i][j]),
                               min(RL2[i][j] + BT2[i][j] - f2[i][j], RL5[i][j] + BT5[i][j] - f5[i][j]))

        return res


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,), (Solution1,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([[1, 5, 2, 4, 25]], 3),
            ([[23, 17, 15, 3, 20], [8, 1, 20, 27, 11], [9, 4, 6, 2, 21], [40, 9, 1, 10, 6], [22, 7, 4, 5, 3]], 3),
            ([[4, 3, 2], [7, 6, 1], [8, 8, 8]], 0),
        ])
        def test_maxTrailingZeros(self, grid, expected):
            sol = self.solution()       # type:ignore
            r = sol.maxTrailingZeros(grid)
            self.assertEqual(r, expected)

    main()
