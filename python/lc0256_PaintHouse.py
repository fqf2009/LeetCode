# There is a row of n houses, where each house can be painted one of 
# three colors: red, blue, or green. The cost of painting each house 
# with a certain color is different. You have to paint all the houses 
# such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented 
# by an n x 3 cost matrix costs.

# For example, costs[0][0] is the cost of painting house 0 with the 
# color red; costs[1][2] is the cost of painting house 1 with color 
# green, and so on...
# Return the minimum cost to paint all houses.

# Constraints:
#   costs.length == n
#   costs[i].length == 3
#   1 <= n <= 100
#   1 <= costs[i][j] <= 20

from functools import cache
from typing import List

# DP + Iteration: T/S: O(n) / O(1), only need to keep previous dp values
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        prevCost1, prevCost2, prevCost3 = 0, 0, 0
        for cost1, cost2, cost3 in costs:
            curCost1 = cost1 + min(prevCost2, prevCost3)
            curCost2 = cost2 + min(prevCost1, prevCost3)
            curCost3 = cost3 + min(prevCost1, prevCost2)
            prevCost1, prevCost2, prevCost3 = curCost1, curCost2, curCost3

        return min(prevCost1, prevCost2, prevCost3)

    
# DP + Memo + Recursion
# T/S: O(n) / O(n) - due to Memo, each house only calc 3 times, total 3*n
#  - assume dp[i, c] is the minimum cost for up until house i, and 
#    house i muse use color c.
#  - state transition equation:
#    dp[i, c] = cost[i][c] + min(cost[i-1][c1], cost[i-1][c2])
#    where c1, c2 are the other colors than c
#  - min_cost_all_houses = min(dp[i, c1], dp[i, c2], dp[i, c3])
class Solution1:
    def minCost(self, costs: List[List[int]]) -> int:
        @cache
        def dp(i, c) -> int:
            if i == 0:
                return costs[i][c]
            if c == 0:
                c1, c2 = 1, 2
            elif c == 1:
                c1, c2 = 0, 2
            else:
                c1, c2 = 0, 1
            return costs[i][c] + min(dp(i-1, c1), dp(i-1, c2))

        h = len(costs) - 1
        return min(dp(h, 0), dp(h, 1), dp(h, 2))


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.minCost(costs = [[17,2,17],[16,16,5],[14,3,19]])
        print(r)
        assert r == 10

        r = sol.minCost(costs = [[7,6,2]])
        print(r)
        assert r == 2

    unitTest(Solution())
    unitTest(Solution1())
