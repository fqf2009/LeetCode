# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum 
# and return its sum.
# A subarray is a contiguous part of an array.
from typing import List

# DP - T/S: O(n), O(1)
#  - assume dp[i] is cumulative sum of subarray nums[:i]
#  - sum(num[j:i]) == dp[i] - dp[j]
#  - during iteration, if we keep the min(dp[]), then we
#    don't need to keep dp[] array at all
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_csum, csum, res = 0, 0, nums[0]
        for v in nums:
            csum += v
            res = max(csum - min_csum, res)
            min_csum = min(min_csum, csum)

        return res


# DP - T/S: O(n), O(1)
# No need to save dp[], just keep the sum of current_subarray_sum
class Solution1:
    def maxSubArray(self, nums: list[int]) -> int:
        curSum, maxSum = 0, nums[0]
        for v in nums:
            if curSum <= 0:
                curSum = v  # start sum of new subarray
            else:
                curSum = curSum + v
            maxSum = max(maxSum, curSum)

        return maxSum


# DP - T/S: O(n), O(n)
#  - dp[0] starts to record cumulative sum of subarray
#  - if dp[i-1] <= 0, stop recording cumulative sum of previous subarray
#    starts a new subarray from nums[i], because dp[i-1] + nums[i] <= nums[i]
#  - return max(dp[])
class Solution2:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = [-(2**31)] * len(nums)
        for i in range(len(nums)):
            if i == 0 or dp[i-1] <= 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
        
        return max(dp)


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        print(r)
        assert r == 6

        r = sol.maxSubArray([1])
        print(r)
        assert r == 1

        r = sol.maxSubArray([5, 4, -1, 7, 8])
        print(r)
        assert r == 23

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
