# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below.
# More formally, if you are on index i on the current row, you may move
# to either index i or index i + 1 on the next row.

# Constraints:
#   1 <= triangle.length <= 200
#   triangle[0].length == 1
#   triangle[i].length == triangle[i - 1].length + 1
#   -104 <= triangle[i][j] <= 104

from typing import List
from functools import cache


# DP + Iteration
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        trg = triangle
        n = len(trg)
        cost = [[2**31] * (i+1) for i in range(n)]
        cost[0][0] = trg[0][0]
        for i in range(n-1):
            for j in range(i + 2):
                if j == 0:
                    cost[i+1][j] = cost[i][j] + trg[i+1][j]
                elif j == i + 1:
                    cost[i+1][j] = cost[i][j-1] + trg[i+1][j]
                else:
                    cost[i+1][j] = min(cost[i][j-1], cost[i][j]) + trg[i+1][j]

        return min(cost[-1])


# DP + Recursion + Memo
class Solution1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if i == 0: return triangle[0][0]
            if i == 1: return dp(0, 0) + triangle[i][j]
            return min(dp(i-1, k) for k in (j-1, j)
                if k >= 0 and k < len(triangle[i-1])) + triangle[i][j]

        return min(dp(len(triangle)-1, j) for j in range(len(triangle[-1])))


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.minimumTotal([[-1],
                              [2,3],
                              [1,-1,-3]])
        print(r)
        assert r == -1

        r = sol.minimumTotal([[2], 
                              [3, 4], 
                              [6, 5, 7], 
                              [4, 1, 8, 3]])
        print(r)
        assert r == 11

        r = sol.minimumTotal([[-10]])
        print(r)
        assert r == -10

    unitTest(Solution())
    unitTest(Solution1())
