# Given an array of integers nums and an integer k. A continuous
# subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.
# Constraints:
#   1 <= nums.length <= 50000
#   1 <= nums[i] <= 10^5
#   1 <= k <= nums.length
from typing import List


# Sliding window: O(n)
# - refer to: 0992_SubarraysWithKDifferentIntegers
# - exactly(K) = atMost(K) - atMost(K-1)
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k: int) -> int:
            # if k == 0:    # wrong result
            #     return 0
            res, j, odds = 0, 0, 0
            for i, v in enumerate(nums):
                if v % 2 == 1:
                    odds += 1
                while odds > k:
                    if nums[j] % 2 == 1:
                        odds -= 1
                    j += 1

                # wrong result if add condition
                # if odds > 0:  # exclude subarrays without a single odd
                res += i - j + 1

            return res

        return atMost(k) - atMost(k - 1)


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.numberOfSubarrays([1, 1, 2, 1, 1], k=3)
        print(r)
        assert r == 2

        r = sol.numberOfSubarrays([2, 4, 6], k=1)
        print(r)
        assert r == 0

        r = sol.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2)
        print(r)
        assert r == 16

        nums = [
            45627,
            50891,
            94884,
            11286,
            35337,
            46414,
            62029,
            20247,
            72789,
            89158,
            54203,
            79628,
            25920,
            16832,
            47469,
            80909,
        ]
        r = sol.numberOfSubarrays(nums, 1)
        print(r)
        assert r == 28

    unitTest(Solution())
