# You are given an integer array nums. You must perform exactly one
# operation where you can replace one element nums[i] with nums[i] * nums[i].
# Return the maximum possible subarray sum after exactly one operation. The
# subarray must be non-empty.
# Constraints:
#   1 <= nums.length <= 10^5
#   -10^4 <= nums[i] <= 10^4

from typing import List

# DP - O(n)
# Analysis:
# - the dpx[i] below means measurements up until position i.
# - dp1[i] = dp1[i-1] + nums[i]: cumulative sum, without operation.
# - dp2[i] = min(dp1[:i]), minimum of the csum, without operation.
# - dp3[i]: maximum subarray sum after EXACTLY one operation.
#   dp3[i] = max(dp3[i] + nums[i], dp1[i-1] + nums[i]^2 - dp2[i-1])
#   Note x^2 >= x is always true. so we can think dp[3] always contain
#   exactly one operation.
# - the final result will be max(dp3)
class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        csum = 0
        min_csum = 0
        subarr_sum = 0
        res = 0
        for v in nums:
            csum1 = csum + v
            min_csum1 = min(min_csum, csum1)
            subarr_sum1 = max(subarr_sum + v, csum + v*v - min_csum)
            res = max(res, subarr_sum1)
            csum, min_csum, subarr_sum = csum1, min_csum1, subarr_sum1

        return res


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.maxSumAfterOperation(nums=[2, -1, -4, -3])
        print(r)
        assert r == 17

        r = sol.maxSumAfterOperation(nums=[2, -1, -4, 9])
        print(r)
        assert r == 81

        r = sol.maxSumAfterOperation([1, -1, 1, 1, -1, -1, 1])
        print(r)
        assert r == 4

    unitTest(Solution())
