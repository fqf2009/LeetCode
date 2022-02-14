# Given an integer array nums, return the length of the longest strictly
# increasing subsequence. A subsequence is a sequence that can be derived
# from an array by deleting some or no elements without changing the order
# of the remaining elements. For example, [3,6,2,7] is a subsequence of
# the array [0,3,1,6,2,2,7].
from typing import List, Optional
import bisect


# use bisect to do binary search
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for v in nums[1:]:
            if v > dp[-1]:
                dp.append(v)
                continue
            p = bisect.bisect_left(dp, v)
            if v < dp[p]:
                dp[p] = v

        return len(dp)


# DP - T/S: O(n*log(n)), O(n)
# - for a Longest Increasing Subsequence (LIS) with length of m,
#   dp[m-1] records minimum ending value of this LIS
# - during scan, longest increasing subsequence is len(dp), and
#   dp[-1] is the minimum possible ending value for this LIS by far.
# - if next number is larger than dp[-1], then it represents another
#   LIS (length is len(dp) + 1) is found, so just append it to dp.
# - if next number is small than dp[-1], use the binary search to find
#   the inserting place for it in dp, and replace the existing dp value,
#   meaning new minimum ending value for this lenth of LIS.
# - e.g.: nums = [3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]
#   values in dp over time:
#       [3]
#       [3, 5]
#       [3, 5, 6]
#       [2, 5, 6]
#       [2, 4, 6]
#       [2, 4, 6, 19]      
#       [2, 4, 5, 19]      
#       [2, 4, 5, 6]       
#       [2, 4, 5, 6, 7]    
#       [2, 4, 5, 6, 7, 12]     # so dp is actually LIS at any moment
class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for v in nums[1:]:
            if v > dp[-1]:
                dp.append(v)
                continue
            i, j = 0, len(dp) - 1
            while i <= j:
                k = (i + j) // 2
                if v == dp[k]:
                    break
                if v > dp[k]:
                    i = k + 1
                else:
                    j = k - 1
            else:   # safe because n <= dp[-1] and n != dp[k]
                dp[i] = v

        return len(dp)


# DP (Dynamic Porgramming) - T/S: O(n^2), O(n)
# - dp[i] is LIS length with ending number of nums[i]
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.lengthOfLIS([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12])
        print(r)
        assert(r == 6)

        r = sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
        print(r)
        assert(r == 4)

        r = sol.lengthOfLIS([0, 1, 0, 3, 2, 3])
        print(r)
        assert(r == 4)

        r = sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7])
        print(r)
        assert(r == 1)

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
