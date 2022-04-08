# 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W.
#  - W      capacity of the bag, i.e., total weight the bag can carry
#  - wt[n]  weight of each item
#  - val[n] value of each item

# DP (Dynamic Programming)
# Time complexity: O(n*W), space complexity: O(n*W), or O(W) when optimized
# Analysis:
# - dp[n, W]: for the first n items, max value can be put in the bag of capacity W
# - if wt[n] >  W, then item n cannot be put into bag, so:
#       dp[n, W] = dp[n-1, W]
# - if wt[n] <= W, then item n can either be put into bag (previous dp will have
#   less capacity), or cannot (previous dp has the same capacity),
#   so state transition equation is:
#       dp[n, W] = max(dp[n-1, W], dp[n-1, W-wt[n]] + val[n])
# - dp[n, W] only relies on dp[n-1, W'], so only two 2*W number of space is required
# - if loop W from high to low, then only 1*W of space is required, i.e., before
#   calculation dp[w] is dp[n-1, w], after calculation dp[w] is dp[n, w]. So the 
#   new state transition equation is:
#       dp[w] = max(dp[w], dp[w-wt[n]] + val[n])

from typing import List


def knapSack(W: int, wt: List[int], val: List[int]) -> int:
    n = len(val)
    dp = [0] * (W+1)                # Making the dp array (W+1 space, 0..W)
    for i in range(1, n+1):         # taking first i elements
        for w in range(W, 0, -1):   # starting from back, note wt is 0 based, and
            if wt[i-1] <= w:        # dp is 1 based, dp[0] is always 0
                dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1])

    return dp[W]  # returning the maximum value of knapsack


if __name__ == '__main__':
    def unitTest():
        val = [60, 100, 120]
        wt = [10, 20, 30]
        W = 50
        r = knapSack(W, wt, val)
        print(r)
        assert r == 220

        val = [5, 4, 3, 2]
        wt = [4, 3, 2, 1]
        W = 6
        r = knapSack(W, wt, val)
        print(r)
        assert r == 9

    unitTest()
