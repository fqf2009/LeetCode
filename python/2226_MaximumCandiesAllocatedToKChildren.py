# You are given a 0-indexed integer array candies. Each element in the 
# array denotes a pile of candies of size candies[i]. You can divide 
# each pile into any number of sub piles, but you cannot merge two 
# piles together.
# You are also given an integer k. You should allocate piles of candies 
# to k children such that each child gets the same number of candies. 
# Each child can take at most one pile of candies and some piles of 
# candies may go unused.
# Return the maximum number of candies each child can get.
# Constraints:
#   1 <= candies.length <= 10^5
#   1 <= candies[i] <= 10^7
#   1 <= k <= 10^12
from typing import List


# Binary Search - T/S: O(n*log(m)), O(1), n = len(candies), m = max(candies)
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        i, j = 1, max(candies)
        res = 0
        while i <= j:
            m = (i + j) // 2
            piles = sum(c // m for c in candies)
            if piles >= k:
                res = m
                i = m + 1
            else:
                j = m - 1

        return res


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.maximumCandies(candies = [10000000], k = 1)
        print(r)
        assert r == 10000000

        r = sol.maximumCandies(candies = [5,8,6], k = 3)
        print(r)
        assert r == 5

        r = sol.maximumCandies(candies = [2,5], k = 11)
        print(r)
        assert r == 0

    unit_test(Solution())
