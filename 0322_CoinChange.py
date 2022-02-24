# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that
# amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.
# Constraints:
#   1 <= coins.length <= 12
#   1 <= coins[i] <= 2^31 - 1
#   0 <= amount <= 10^4
from functools import cache
from itertools import chain
from typing import List


# DP + Iteration - T/S: O(n*m), O(n), where n = len(coins), m = amount
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(amount):
            if dp[i] == -1: continue
            for c in coins:
                if i + c <= amount:
                    if dp[i + c] == -1:
                        dp[i + c] = dp[i] + 1
                    else:
                        dp[i + c] = min(dp[i + c], dp[i] + 1)
        return dp[amount]


# DP + Recursion + Memo
# !!! RecursionError: maximum recursion depth exceeded
# !!! recursive depth = amount / min(coins)
# - assume dp[amount] is minimum number of coins to make up amount
# - iterate through each coin:
#   dp[amount] = min(dp[amount - coin_value]+1 for each coin in coins)
class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(n) -> int:
            if n == 0:
                return 0
            return min(chain((dp(n-c)+1 for c in coins if n-c >= 0), (2**31,)))

        res = dp(amount)
        # print(dp.cache_info())
        return res if res != 2**31 else -1


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.coinChange(coins=[2147483647], amount=2)
        print(r)
        assert r == -1


        r = sol.coinChange(coins=[1, 2, 5], amount=11)
        print(r)
        assert r == 3

        r = sol.coinChange(coins=[5, 10, 100, 200], amount=1055)
        print(r)
        assert r == 11

        r = sol.coinChange(coins=[2], amount=3)
        print(r)
        assert r == -1

        r = sol.coinChange(coins=[1], amount=0)
        print(r)
        assert r == 0

    unitTest(Solution())
    unitTest(Solution1())
