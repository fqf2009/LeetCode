# Given an integer array nums, return the number of
# longest increasing subsequences.
# Notice that the sequence has to be strictly increasing.

# Constraints:
#   1 <= nums.length <= 2000
from typing import List, Optional
import bisect


# Analysis:
# - This is similar to LeetCode 0300 Longest Increasing Subsequence,
#   however, the difference is to count the number of LIS.
# - The optimized O(n*log(n)) solution is not useful here.
# - So go back to the O(n^2) DP solution
# - Assume: dp[i] is LIS length with ending number of nums[i]
#           cnt[i] is count of LIS with ending number of nums[i]
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        cnt = [1] * n
        lis = 0     # length of LIS during iteration
        res = 0     # count of LIS during iteration
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 == dp[i]:  # another way leads to LIS ending with nums[i]
                        cnt[i] += cnt[j]
                    elif dp[j] >= dp[i]:
                        dp[i] = dp[j] + 1   # new LIS ending with nums[i]
                        cnt[i] = cnt[j]
            if lis < dp[i]:         # new LIS with increased length
                lis = dp[i]
                res = cnt[i]
            elif lis == dp[i]:      # new LIS with same length previous ones
                res += cnt[i]

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.findNumberOfLIS([1, 3, 5, 4, 7])
        print(r)
        assert(r == 2)

        r = sol.findNumberOfLIS([2, 2, 2, 2, 2])
        print(r)
        assert(r == 5)

    unitTest(Solution())
