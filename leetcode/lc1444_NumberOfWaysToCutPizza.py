# Given a rectangular pizza represented as a rows x cols matrix containing
# the following characters: 'A' (an apple) and '.' (empty cell) and given
# the integer k. You have to cut the pizza into k pieces using k-1 cuts.
# For each cut you choose the direction: vertical or horizontal, then you
# choose a cut position at the cell boundary and cut the pizza into two
# pieces. If you cut the pizza vertically, give the left part of the pizza
# to a person. If you cut the pizza horizontally, give the upper part of
# the pizza to a person. Give the last piece of pizza to the last person.
# Return the number of ways of cutting the pizza such that each piece
# contains at least one apple. Since the answer can be a huge number,
# return this modulo 10^9 + 7.
# Constraints:
#   1 <= rows, cols <= 50
#   rows == pizza.length
#   cols == pizza[i].length
#   1 <= k <= 10
#   pizza consists of characters 'A' and '.' only.
from functools import cache
from typing import List


# 2-D, prefix(actually postfix) Sum + DP
# T/S: O(m*n*(m+n)*k), O(m*n*k)
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n, modulo = len(pizza), len(pizza[0]), 10**9 + 7
        apples = [[0] * (n + 1) for _ in range(m + 1)]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                apples[i][j] = (
                    (1 if pizza[i][j] == "A" else 0) + 
                    apples[i + 1][j] + apples[i][j + 1] - apples[i + 1][j + 1]
                )

        @cache
        def dp(x, y, k) -> int:
            """
            Parameter:
                x, y: top-left position of the remaining pizza
                k:    to cut remaining pizza into k pieces
            Returns:
                the number of ways to cut
            """
            if k == 1:
                return 1 if apples[x][y] > 0 else 0
            res = 0
            for i in range(x + 1, m):
                if apples[x][y] - apples[i][y] > 0:
                    res += dp(i, y, k - 1)
            for j in range(y + 1, n):
                if apples[x][y] - apples[x][j] > 0:
                    res += dp(x, j, k - 1)
            return res % modulo

        return dp(0, 0, k)


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.ways(["A..", "AAA", "..."], k=3)
        print(r)
        assert r == 3

        r = sol.ways(["A..", "AA.", "..."], k=3)
        print(r)
        assert r == 1

        r = sol.ways(["A..", "A..", "..."], k=1)
        print(r)
        assert r == 1

        r = sol.ways([".A..A", "A.A..", "A.AA.", "AAAA.", "A.AA."], k=5)
        print(r)
        assert r == 153

    unit_test(Solution())
