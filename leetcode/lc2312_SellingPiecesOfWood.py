# You are given two integers m and n that represent the height and width 
# of a rectangular piece of wood. You are also given a 2D integer array 
# prices, where prices[i] = [hi, wi, pricei] indicates you can sell a
# rectangular piece of wood of height hi and width wi for pricei dollars.
# To cut a piece of wood, you must make a vertical or horizontal cut across 
# the entire height or width of the piece to split it into two smaller pieces. 
# After cutting a piece of wood into some number of smaller pieces, you can
# sell pieces according to prices. You may sell multiple pieces of the same 
# shape, and you do not have to sell all the shapes. The grain of the wood 
# makes a difference, so you cannot rotate a piece to swap its height and width.
# Return the maximum money you can earn after cutting an m x n piece of wood.
# Note that you can cut the piece of wood as many times as you want.
# Constraints:
#   1 <= m, n <= 200
#   1 <= prices.length <= 2 * 10^4
#   prices[i].length == 3
#   1 <= hi <= m
#   1 <= wi <= n
#   1 <= pricei <= 106
#   All the shapes of wood (hi, wi) are pairwise distinct.
from collections import defaultdict
from functools import cache
from typing import List


# 2-D DP (Buttom up)
# T/S: O(m*n*(m+n)), O(m*n)
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        value = [[0] * (n + 1) for _ in range(m + 1)]
        for x, y, p in prices:
            value[x][y] = p

        for x in range(1, m + 1):
            for y in range(1, n + 1):
                for i in range(1, x // 2 + 1):
                    value[x][y] = max(value[x][y], value[i][y] + value[x-i][y])
                for j in range(1, y // 2 + 1):
                    value[x][y] = max(value[x][y], value[x][j] + value[x][y-j])

        return value[m][n]


# 2-D DP (Top down) + Memo
# T/S: O(m*n*(m+n)), O(m*n)
class Solution0:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        @cache
        def dp(x, y):
            res = value[x][y]
            for i in range(1, x // 2 + 1):
                res = max(res, dp(i, y) + dp(x - i, y))
            for j in range(1, y // 2 + 1):
                res = max(res, dp(x, j) + dp(x, y - j))

            return res

        value = [[0] * (n + 1) for _ in range(m + 1)]
        for x, y, p in prices:
            value[x][y] = p

        return dp(m, n)


# 2-D DP (Top down) + Memo
# T/S: O(L + m*n*(m+n)), O(L + m*n), where L = len(prices), L <= m*n
#  =>  O(m*n*(m+n)), O(m*n)
# Analysis:
# - each piece of wood has its original value from prices with exact size
# - split wood in all possible way, and get the most value from splits
# - use memo to avoid repeated calculation
class Solution1:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        @cache
        def dp(x, y):
            res = value.get((x, y), 0)
            for i in range(1, x // 2 + 1):
                res = max(res, dp(i, y) + dp(x - i, y))
            for j in range(1, y // 2 + 1):
                res = max(res, dp(x, j) + dp(x, y - j))

            return res

        value =  {(x, y): p for x, y, p in prices}
        return dp(m, n)


# Code during contest, not simplified yet
class Solution2:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        value = [[0] * (n + 1) for _ in range(m + 1)]
        price2 = defaultdict(dict)
        for x, y, p in prices:
            price2[x][y] = p
        for i in range(m + 1):
            for j in range(n + 1):
                a = i
                while a > 0 and a not in price2:
                    a -= 1
                if a == 0:
                    continue
                b = j
                while b > 0 and b not in price2[a]:
                    b -= 1
                if b == 0:
                    continue
                value[a][b] = price2[a][b]

        @cache
        def dp(x, y):
            res = value[x][y]
            for i in range(1, x // 2 + 1):
                res = max(res, dp(i, y) + dp(x - i, y))
            for j in range(1, y // 2 + 1):
                res = max(res, dp(x, j) + dp(x, y - j))

            return res

        return dp(m, n)


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.sellingWood(m=3, n=5, prices=[[1, 4, 2], [2, 2, 7], [2, 1, 3]])
        print(r)
        assert r == 19

        r = sol.sellingWood(m=4, n=6, prices=[[3, 2, 10], [1, 4, 2], [4, 1, 3]])
        print(r)
        assert r == 32

    unit_test(Solution())
    unit_test(Solution0())
    unit_test(Solution1())
    unit_test(Solution2())
