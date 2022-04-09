# Given an array nums which consists of non-negative integers and an integer m, 
# you can split the array into m non-empty continuous subarrays.
# Write an algorithm to minimize the largest sum among these m subarrays.
# Constraints:
#   1 <= nums.length <= 1000
#   0 <= nums[i] <= 106
#   1 <= m <= min(50, nums.length)
from cmath import inf
from typing import List


# Binary Search + Prefix Sum + Sliding Window
# Time: O(n*log(W)), where W = sum(nums) - min(nums)
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        def min_subarray(subsum):
            prev_idx = 0
            res = 0
            for i in range(1, n+1):
                if prefix_sum[i] - prefix_sum[prev_idx] > subsum:
                    res += 1
                    prev_idx = i-1

            return res + 1

        lo, hi = max(nums), prefix_sum[-1]
        while lo < hi:
            mid = (lo+hi) // 2
            cnt = min_subarray(mid)
            if cnt > m:
                lo = mid + 1
            else:
                hi = mid

        return lo


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([7,2,5,10,8], 2, 18),
            ([1,2,3,4,5], 2, 9),
            ([1,4,4], 3, 4),
        ])
        def test_splitArray(self, nums, m, expected):
            sol = self.solution()       # type:ignore
            r = sol.splitArray(nums, m)
            self.assertEqual(r, expected)

    main()
