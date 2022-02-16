# Given a set of distinct positive integers nums, return the largest
# subset answer such that every pair (answer[i], answer[j]) of
# elements in this subset satisfies:
#   answer[i] % answer[j] == 0, or
#   answer[j] % answer[i] == 0
# If there are multiple solutions, return any of them.

# Constraints:
#   1 <= nums.length <= 1000
#   1 <= nums[i] <= 2 * 109
#   All the integers in nums are unique.
from typing import List


# DP (Dynamic Programming): O(n^2), plus O(n*log(n) from sort
# - similar to Longest Increasing Subsequence.
# - the difference is:
#   - you cannot sort items in LIS problem.
#   - this one need return subset, not just length of the longest subset.
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1] * n
        dp2 = [[nums[i]] for i in range(n)]
        res = 1
        res2 = [nums[0]]
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        dp2[i] = dp2[j].copy()
                        dp2[i].append(nums[i])
                        if res < dp[i]:
                            res = dp[i]
                            res2 = dp2[i]

        return res2


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.largestDivisibleSubset([1, 2, 3])
        print(r)
        assert r == [1, 2] or r == [1, 3]

        r = sol.largestDivisibleSubset([1, 2, 4, 8])
        print(r)
        assert r == [1, 2, 4, 8]

    unitTest(Solution())
