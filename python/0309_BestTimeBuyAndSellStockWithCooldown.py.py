# You are given an array prices where prices[i] is the price
# of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as
# many transactions as you like (i.e., buy one and sell one share
# of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next
# day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously
# (i.e., you must sell the stock before you buy again).

# Constraints:
#   1 <= prices.length <= 5000
#   0 <= prices[i] <= 1000

from typing import List


# DP + State Machine, Time: O(n)
# - finite state machine, 3 states:
#   reset - ready to buy stock, 'buy' action leads to 'hold' state
#   hold  - hold stock right now, 'sell' action leads to 'sold' state
#   sold  - just sold stock, next state will be 'reset' automatically
# - assume reset[i], hold[i], sold[i] are the cash balance in each 
#   state at i-th day.
# - the goal is to maximize the balance at each state along the way
# - state transition equation (formula):
#   reset[i] = max(reset[i-1], sold[i-1])
#   hold[i]  = max(hold[i-1], reset[i-1] - price[i])
#   sold[i]  = hold[i-1] + price(i)
# - each state's i-th dp value only relies on (i-1)-th value, so 
#   no need to keep them, and the space complexity can be O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        reset, hold, sold = 0, -prices[0], 0
        for price in prices[1:]:
            reset1 = max(reset, sold)
            hold1  = max(hold, reset-price)
            sold1  = hold + price
            reset, hold, sold = reset1, hold1, sold1

        return max(reset, sold)


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.maxProfit(prices=[1, 2, 3, 0, 2])
        print(r)
        assert r == 3

        r = sol.maxProfit(prices=[1])
        print(r)
        assert r == 0

    unitTest(Solution())
