# You are given an array of non-negative integers nums and an integer k.
# In one operation, you may choose any element from nums and increment it by 1.
# Return the maximum product of nums after at most k operations. Since the 
# answer may be very large, return it modulo 10^9 + 7.
# Constraints:
#   1 <= nums.length, k <= 10^5
#   0 <= nums[i] <= 106
import heapq
from typing import List
from functools import reduce


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MODULO = 10**9 + 7
        heapq.heapify(nums)
        for _ in range(k):
            heapq.heapreplace(nums, nums[0] + 1)

        return reduce(lambda x, y: x * y % MODULO, nums, 1)


if __name__ == "__main__":
    from unittest import TestCase, main
    from unittest.mock import patch
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,)])    # must be tuple!!!
    class TestSolution(TestCase):
        @parameterized.expand([
            ([0, 4], 5, 20),
            ([6, 3, 3, 2], 2, 216),
        ])
        def test_maximumProduct(self, nums, k, expected):

            sol = self.solution()       # type:ignore
            r = sol.maximumProduct(nums, k)
            self.assertEqual(r, expected)

    main()
