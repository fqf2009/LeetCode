# The distance of a pair of integers a and b is defined as the absolute 
# difference between a and b.
# Given an integer array nums and an integer k, return kth smallest distance
# among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.
#  Constraints:
#   n == nums.length
#   2 <= n <= 10^4
#   0 <= nums[i] <= 10^6
#   1 <= k <= n * (n - 1) / 2
from typing import List


# Binary Search + Sliding Window
# Time: O(n*log(n) + n*log(W)), where W = max(nums) - min(nums)
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def has_k_pairs(distance):
            j = 0
            res = 0
            for i in range(1, len(nums)):
                while nums[i] - nums[j] > distance:
                    j += 1
                res += i - j
            return res >= k

        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo+hi) // 2
            if has_k_pairs(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([1,3,1], 1, 0),
            ([1,1,1], 2, 0),
            ([1,6,1], 3, 5),
        ])
        def test_smallestDistancePair(self, nums, k, expected):
            sol = self.solution()       # type:ignore
            r = sol.smallestDistancePair(nums, k)
            self.assertEqual(r, expected)

    main()
