# There are a row of n houses, each house can be painted with one of
# the k colors. The cost of painting each house with a certain color
# is different. You have to paint all the houses such that no two
# adjacent houses have the same color.

# The cost of painting each house with a certain color is represented
# by an n x k cost matrix costs.

# For example, costs[0][0] is the cost of painting house 0 with color 0;
# costs[1][2] is the cost of painting house 1 with color 2, and so on...
# Return the minimum cost to paint all houses.

# Constraints:
#   costs.length == n
#   costs[i].length == k
#   1 <= n <= 100
#   2 <= k <= 20
#   1 <= costs[i][j] <= 20
from functools import cache
from typing import List


# DP + Iteration: T/S: O(n) / O(k), only need to keep previous dp values
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        k = len(costs[0])
        prevCost = costs[0]
        for cost in costs[1:]:
            minIdx1 = 0                 # index for minimum cost in prevCost[]
            for i in range(1, k):
                if prevCost[i] < prevCost[minIdx1]:
                    minIdx1 = i
            minIdx2 = (minIdx1+1) % k   # index for 2nd minimum cost, pick one other than minIdx1
            for i in range(k):          # note there are duplicate values in prevCost[]
                if i != minIdx1 and prevCost[i] < prevCost[minIdx2]:
                    minIdx2 = i
            # very easy to make mistake below, note the () around if... else...
            curCost = [cost[i] + (prevCost[minIdx1] if i != minIdx1 else prevCost[minIdx2])
                       for i in range(k)]
            prevCost = curCost

        return min(prevCost)


# DP + Memo + Recursion
# T/S: O(n*k) / O(n*k) - due to Memo, each house only calc k times, total k*n
#  - assume dp[i, c] is the minimum cost for up until house i, and
#    house i muse use color c.
#  - state transition equation:
#    dp[i, c] = cost[i][c] + min(cost[i-1][c1], ..., cost[i-1][cn])
#    where c1, ..., cn are all the other colors than c
#  - min_cost_all_houses = min(dp[i, c1], dp[i, c2], ..., dp[i, cn])
class Solution1:
    def minCostII(self, costs: List[List[int]]) -> int:
        @cache
        def dp(i, c) -> int:
            if i == 0:
                return costs[i][c]
            return costs[i][c] + min([dp(i-1, j) for j in range(len(costs[0])) if j != c])

        h = len(costs) - 1
        return min([dp(h, j) for j in range(len(costs[0]))])


if __name__ == '__main__':
    def unitTest(sol):
        costs = [[2,18,7],[3,12,3],[1,11,1],[2,8,16],[1,18,14],[11,20,8],[4,12,16],[12,16,14],
                 [1,7,10],[14,11,5],[18,11,4],[12,14,12],[9,1,20],[4,20,17],[2,1,14],[18,19,4] ,
                 [18,7,1],[11,11,6],[13,8,10],[9,7,9],[19,15,15],[5,4,11],[10,3,18],[13,13,4]]
        r = sol.minCostII(costs)
        print(r)
        assert r == 136

        costs = [[8,16,12,18,9],[19,18,8,2,8],[8,5,5,13,4],[15,9,3,19,2],[8,7,1,8,17],
                 [8,2,8,15,5],[8,17,1,15,3],[8,8,5,5,16],[2,2,18,2,9]]
        r = sol.minCostII(costs)
        print(r)
        assert r == 28

        r = sol.minCostII(costs=[[17, 2, 17], [16, 16, 5], [14, 3, 19]])
        print(r)
        assert r == 10

        r = sol.minCostII(costs=[[7, 6, 2]])
        print(r)
        assert r == 2

        r = sol.minCostII(costs=[[1, 5, 3], [2, 9, 4]])
        print(r)
        assert r == 5

        r = sol.minCostII(costs=[[1, 3], [2, 4]])
        print(r)
        assert r == 5

    unitTest(Solution())
    unitTest(Solution1())
