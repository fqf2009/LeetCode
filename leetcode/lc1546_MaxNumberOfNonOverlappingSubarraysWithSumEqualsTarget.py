# Given an array nums and an integer target, return the maximum number
# of non-empty non-overlapping subarrays such that the sum of values
# in each subarray is equal to target.
# Constraints:
#   1 <= nums.length <= 10^5
#   -10^4 <= nums[i] <= 10^4
#   0 <= target <= 10^6
from typing import List


# Prefix Sum + Greedy - T/S: O(n), O(n)
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        seen = {0:-1}   # prefix sum encountered before
        csum = 0    # current prefix sum
        res = 0
        prev_pos = -1  # pos of last item of previous subarray
        for i, v in enumerate(nums):
            csum += v
            if seen.get(csum - target, -2) >= prev_pos: # >= (not >) !!!
                res += 1
                prev_pos = i
            seen[csum] = i  # new or old csum, set to latest pos

        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.maxNonOverlapping([1, 1, 1, 1, 1], target=2)
        print(r)
        assert r == 2

        r = sol.maxNonOverlapping([-1, 3, 5, 1, 4, 2, -9], target=6)
        print(r)
        assert r == 2

    unit_test(Solution())
