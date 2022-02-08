# You are given an array prices where prices[i] is the price of 
# a given stock on the ith day.

# You want to maximize your profit by choosing a single day to 
# buy one stock and choosing a different day in the future to 
# sell that stock.

# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0
        for p in prices[1:]:
            minPrice = min(minPrice, p)
            profit = max(profit, p - minPrice)

        return profit


if __name__ == '__main__':
    def unitTest(sol):
        sol = Solution()

        r = sol.maxProfit([7, 1, 5, 3, 6, 4])
        print(r)
        assert r == 5

        r = sol.maxProfit([7, 6, 4, 3, 1])
        print(r)
        assert r == 0

    unitTest(Solution())
