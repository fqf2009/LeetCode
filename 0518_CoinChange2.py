# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
# Return the number of combinations that make up that amount. If that
# amount of money cannot be made up by any combination of the coins, return 0.
# You may assume that you have an infinite number of each kind of coin.
# The answer is guaranteed to fit into a signed 32-bit integer.

# Constraints:
#   1 <= coins.length <= 300
#   1 <= coins[i] <= 5000
#   All the values of coins are unique.
#   0 <= amount <= 5000
from functools import cache
from itertools import chain
from typing import List


# DP + Iterate - T/S: O(n*m), O(n+m), where n = len(coins), m = amount
# - avoiding the duplicates, by using different coins in order, i.e.,
#   use coin1, then coin2, ..., never go back to use coin1 again.
# - So this is combination, and solution1 is permutation.
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount+1):
                dp[i] += dp[i - c]
        return dp[amount]
        

# DP + Iterate - T/S: O(n*m), O(n+m), where n = len(coins), m = amount
# !!! Wrong, the combination of coins in this solution is not unique!!!
class Solution1:
    def change(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(amount):
            for c in coins:
                if i + c <= amount:
                    dp[i + c] += dp[i]
        return dp[amount]


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.change(amount=5, coins=[1, 2, 5])
        print(r)
        assert r == 4

        r = sol.change(amount=1055, coins=[1, 2, 5, 10, 100, 200])
        print(r)
        assert r == 10677374

        r = sol.change(amount=3, coins=[2])
        print(r)
        assert r == 0

        r = sol.change(amount=10, coins=[10])
        print(r)
        assert r == 1

    unitTest(Solution())
    # unitTest(Solution1())     # wrong
