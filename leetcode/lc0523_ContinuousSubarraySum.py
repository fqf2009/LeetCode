# Given an integer array nums and an integer k, return true if nums has a
# continuous subarray of size at least two whose elements sum up to a
# multiple of k, or false otherwise.
# An integer x is a multiple of k if there exists an integer n such
# that x = n * k. 0 is always a multiple of k.
# Constraints:
#   1 <= nums.length <= 10^5
#   0 <= nums[i] <= 10^9
#   0 <= sum(nums[i]) <= 2^31 - 1
#   1 <= k <= 2^31 - 1
from typing import List


# Prefix Sum + Modulo - T/S: O(n), O(k)
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_pos = {0: -1}   # !!! otherwise, subarray like nums[:i] will not be included
        total = 0
        for i, v in enumerate(nums):
            total += v
            m = total % k
            if m in mod_pos:
                if i - mod_pos[m] > 1:
                    return True
            else:
                mod_pos[m] = i

        return False


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.checkSubarraySum([23, 2, 4, 6, 6], k=7)
        print(r)
        assert r == True

        r = sol.checkSubarraySum([23, 2, 4, 6, 7], k=6)
        print(r)
        assert r == True

        r = sol.checkSubarraySum([23, 2, 6, 4, 7], k=6)
        print(r)
        assert r == True

        r = sol.checkSubarraySum([23, 2, 6, 4, 7], k=13)
        print(r)
        assert r == False

    unit_test(Solution())
