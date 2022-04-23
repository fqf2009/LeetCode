# You are given an integer array prices where prices[i] is the price 
# of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can 
# only hold at most one share of the stock at any time. However, you 
# can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.
# Constraints:
#   1 <= prices.length <= 3 * 10^4
#   0 <= prices[i] <= 10^4
from typing import List


# T/S: O(n), O(1)
# - take all profit in up-trend
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(p2-p1 for p1, p2 in zip(prices, prices[1:]) if p2 > p1)


# T/S: O(n), O(1)
# analysis:
# - keep lowest price at down-trend (valley)
# - keep profit at up-trend (peak)
# - do nothing when price does not change
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        profit = total_profit = 0
        low_price = p0 = prices[0]
        for p in prices[1:]:
            if p < p0:
                low_price = p
                total_profit += profit
                profit = 0
                p0 = p
            elif p > p0:
                profit = p - low_price
                p0 = p
        
        return total_profit + profit


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(("solution",), [(Solution,), (Solution1,)])
    class TestSolution(TestCase):
        @parameterized.expand(
            [
                ([7,1,5,3,6,4], 7),
                ([1,2,3,4,5], 4),
                ([7,6,4,3,1], 0),
            ]
        )
        def test_maxProfit(self, prices, expected):
            sol = self.solution()  # type:ignore
            r = sol.maxProfit(prices )
            self.assertEqual(r, expected)

    main()
