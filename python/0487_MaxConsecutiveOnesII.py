# Given a binary array nums, return the maximum number of 
# consecutive 1's in the array if you can flip at most one 0.
# Constraints:
#   1 <= nums.length <= 10^5
#   nums[i] is either 0 or 1.
from typing import List

# DP - T/S: O(n), O(1)
# - keep two states array:
#   dp1[i]: at position i, the number of consecutive 1's without flip.
#   dp2[i]: at position i, the max number of consecutive 1's with one flip.
# - state transition equation:
#   if nums[i] == 1:
#       dp1[i] = dp1[i-1] + 1
#       dp2[i] = dp2[i-1] + 1
#   if nums[i] == 0:
#       dp1[i] = 0
#       dp2[i] = dp1[i-1] + 1, i.e. flip this '0', forget about the previous flip
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        dp1 = dp2 = 0
        res = 0
        for v in nums:
            if v == 1:
                dp1 += 1
                dp2 += 1
            else:
                dp2 = dp1 + 1
                dp1 = 0
            res = max(res, dp2)

        return res


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.findMaxConsecutiveOnes(nums = [1,0,1,1,0])
        print(r)
        assert r == 4

        r = sol.findMaxConsecutiveOnes(nums = [1,0,1,1,0,1])
        print(r)
        assert r == 4

    unitTest(Solution())
