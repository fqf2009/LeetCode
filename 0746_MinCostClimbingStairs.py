# You are given an integer array cost where cost[i] is the cost of ith
# step on a staircase. Once you pay the cost, you can either climb one
# or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

# Example 1:
#   Input: cost = [10,15,20]
#   Output: 15
#   Explanation: You will start at index 1.
#   - Pay 15 and climb two steps to reach the top.
#   The total cost is 15.

# Example 2:
#   Input: cost = [1,100,1,1,1,100,1,1,100,1]
#   Output: 6
#   Explanation: You will start at index 0.
#   - Pay 1 and climb two steps to reach index 2.
#   - Pay 1 and climb two steps to reach index 4.
#   - Pay 1 and climb two steps to reach index 6.
#   - Pay 1 and climb one step to reach index 7.
#   - Pay 1 and climb two steps to reach index 9.
#   - Pay 1 and climb one step to reach the top.
#   The total cost is 6.
from typing import List
from functools import cache

# DP, Memo
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def costTillStep(p: int) -> int:
            if p < 0:
                return 0
            if p <= 1:
                return cost[p]

            return cost[p] + min(costTillStep(p-1), costTillStep(p-2))

        n = len(cost)
        return min(costTillStep(n-1), costTillStep(n-2))


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.minCostClimbingStairs(cost=[10, 15, 20])
        print(r)
        assert r == 15

        r = sol.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
        print(r)
        assert r == 6

    unitTest(Solution())
