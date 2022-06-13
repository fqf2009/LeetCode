# Given a binary array nums and an integer goal, return
# the number of non-empty subarrays with a sum goal.
# A subarray is a contiguous part of the array.
# Constraints:
#   1 <= nums.length <= 3 * 10^4
#   nums[i] is either 0 or 1.
#   0 <= goal <= nums.length
from typing import Counter, List


# Count freq of prefix sum
# - the value in nums could be anything, not just 0 and 1.
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cntr = Counter()
        csum = 0
        cntr[csum] += 1
        res = 0
        for v in nums:
            csum += v
            res += cntr[csum - goal]
            cntr[csum] += 1

        return res


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.numSubarraysWithSum([1, 0, 1, 0, 1], goal=2)
        print(r)
        assert r == 4

        r = sol.numSubarraysWithSum([0, 0, 0, 0, 0], goal=0)
        print(r)
        assert r == 15

    unitTest(Solution())
