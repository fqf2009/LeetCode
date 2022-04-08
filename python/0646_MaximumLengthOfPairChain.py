# You are given an array of n pairs pairs where
# pairs[i] = [lefti, righti] and lefti < righti.
# A pair p2 = [c, d] follows a pair p1 = [a, b]
# if b < c. A chain of pairs can be formed in this fashion.
# Return the length longest chain which can be formed.
# You do not need to use up all the given intervals.
# You can select pairs in any order.
# Constraints:
#   n == pairs.length
#   1 <= n <= 1000
#   -1000 <= lefti < righti <= 1000
from typing import List
from operator import itemgetter


# Greedy: O(n*log(n) is from sort. The iteration part is O(n)
# - sort on end point, and then iterate through all chains.
# - remember the end point of the current chain.
# - each time if a chain is chainable, use it, remember new end point.
#   at least it will not be worse than the next one.
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        curEnd = -2**31
        res = 0
        for start, end in sorted(pairs, key=itemgetter(1)): # Sorted on end point
            if curEnd < start:
                curEnd = end
                res += 1

        return res


# DP (Dynamic Programming): O(n^2), plus O(n*log(n) from sort
# - similar to Longest Increasing Subsequence.
# - the difference is items in LIS problem can not be sorted.
class Solution1:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()        # Sorted on start point
        dp = [1] * len(pairs)
        res = 1
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[j] + 1, dp[i])
                    res = max(res, dp[i])
        
        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.findLongestChain([[1, 2]])
        print(r)
        assert r == 1

        r = sol.findLongestChain([[1, 2], [7, 8], [4, 5]])
        print(r)
        assert r == 3

        r = sol.findLongestChain([[1, 2], [7, 8], [4, 5]])
        print(r)
        assert r == 3

    unitTest(Solution())
    unitTest(Solution1())
