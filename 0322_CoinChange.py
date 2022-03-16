# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that
# amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.
# Constraints:
#   1 <= coins.length <= 12
#   1 <= coins[i] <= 2^31 - 1
#   0 <= amount <= 10^4
from typing import List
from functools import cache
from itertools import chain
from collections import deque


# LeetCode - faster than 98.60% of Python3 online submissions
# BFS + Iteration (using deque)
# - Time:  Best  O(n*(m/C)), where n = len(coins), m = amount, C = max(coins)
# -        Worst O(n*(m/c)), where c = min(coins)
# - Space: Best  O(n*(m/C))
#          Worst O(n*(m/c)), this is bad only if n is big, and result is -1
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        pending = set()         # very import to reduce duplicate steps
        dq = deque([[0, 0]])    # (amt, step)
        while dq:
            amt, step = dq.popleft()
            for coin in coins:
                amt1 = amt + coin
                if amt1 == amount:
                    return step + 1
                elif amt1 < amount and amt1 not in pending:
                    dq.append([amt1, step + 1])
                    pending.add(amt1)
        return -1


# DP + Iteration - T/S: O(n*m), O(m), where n = len(coins), m = amount
class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = [amount*10] * (amount + 1)
        dp[0] = 0
        for i in range(amount):
            if dp[i] > amount: continue
            for c in coins:
                if i + c <= amount:
                    dp[i + c] = min(dp[i + c], dp[i] + 1)

        return dp[amount] if dp[amount] <= amount else -1


# DP + Recursion + Memo
# !!! RecursionError: maximum recursion depth exceeded
# !!! recursive depth = amount / min(coins)
# - assume dp[amount] is minimum number of coins to make up amount
# - iterate through each coin:
#   dp[amount] = min(dp[amount - coin_value]+1 for each coin in coins)
class Solution2:
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

        r = sol.coinChange(coins=[1, 2, 5], amount=100)
        print(r)
        assert r == 20

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
    unitTest(Solution2())
