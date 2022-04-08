# You are given an array prices where prices[i] is the price of a
# given stock on the ith day, and an integer fee representing a
# transaction fee.

# Find the maximum profit you can achieve. You may complete as many
# transactions as you like, but you need to pay the transaction fee
# for each transaction.

# Note: You may not engage in multiple transactions simultaneously
# (i.e., you must sell the stock before you buy again).
from typing import List


# DP (Dynamic Programming)
# - assume: sell[i]: at i-th day, the cash balance without holding stock
#           buy[i]:  at i-th day, the cash balance after holding 1 share
# - The goal is to get maximum sell[i] amount at the end.
# - The state transition equation:
#     sell[i+1] = max(sell[i-1], buy[i-1] + price[i] - fee)
#     buy[i+1]  = max(buy[i-1],  sell[i] - price[i])
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sell = 0
        buy = -prices[0]
        for price in prices[1:]:
            sell = max(sell, buy + price -fee)
            buy = max(buy, sell - price)

        return sell


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2)
        print(r)
        assert r == 8

        r = sol.maxProfit(prices=[1, 3, 7, 5, 10, 3], fee=3)
        print(r)
        assert r == 6

    unitTest(Solution())
