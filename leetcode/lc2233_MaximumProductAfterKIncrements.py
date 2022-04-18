# You are given an array of non-negative integers nums and an integer k.
# In one operation, you may choose any element from nums and increment it by 1.
# Return the maximum product of nums after at most k operations. Since the 
# answer may be very large, return it modulo 10^9 + 7.
# Constraints:
#   1 <= nums.length, k <= 10^5
#   0 <= nums[i] <= 10^6
import bisect
import heapq
from typing import List
from functools import reduce

# Binary Search: O(n*log(n))
# - Sort nums first
# - build a prefix sum for an array, which is top-up each item in
#   sorted nums to make nums[i] = nums[i+1], e.g.:
#     sorted(nums)  : 1, 2, 3, 5, 9
#     top-up process: 2, 2            prefix sum: 1
#                     3, 3, 3                     1, 3
#                     5, 5, 5, 5                  1, 3, 9
#                     9, 9, 9, 9, 9               1, 3, 9, 25
# - if k < prefix_sum[-1], binary search k in prefix_sum,
# - this is the way to solve 2234_MaximumTotalBeautyOfGarden!!!
#   however, too complex and too much edge conditions.
class Solution3:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MODULO = 10**9 + 7
        n = len(nums)
        nums.sort()
        prefix_sum = [0] * n
        for i, v in enumerate(nums[1:], 1):
            prefix_sum[i] = prefix_sum[i-1] + (v - nums[i-1]) * i

        i = bisect.bisect_right(prefix_sum, k) - 1
        k -= prefix_sum[i]
        low_val = nums[i] + k // (i+1)
        k = k % (i+1)
        low_cnt = (i+1) - k
        return ( (low_val**low_cnt) % MODULO * 
                    reduce(lambda x, y: x * y % MODULO, range(low_val+1, low_val+1+k), 1) *
                    reduce(lambda x, y: x * y % MODULO, nums[i+1:], 1) ) % MODULO


# Binary Search: O(n*log(k))
# - binary search a value (v) between 0 ~ k, where:
#   - in each search, scan all n items, if less than k , 
#     top it up to v, reduce k;
#   - if in this search, final_k <= count_of_items_equal_to_v
#     binary search end.
#   - result calculation is the same as the "Sort + Scan" solution
# class Solution2:
#     def maximumProduct(self, nums: List[int], k: int) -> int:
#         pass


# Sort + Scan
# T/S: O(n*log(n) + k), O(1) by reusing nums
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MODULO = 10**9 + 7
        nums.sort()
        res = 1
        break_idx = len(nums) - 1
        for i, v in enumerate(nums[:-1]):
            if k > (nums[i+1] - v) * (i + 1):
                k -= (nums[i+1] - v) * (i + 1)
                nums[i] = nums[i+1]
            else:
                break_idx = i
                break

        lo_val = nums[break_idx] + k // (break_idx + 1)
        mid_val = lo_val + 1
        mid_cnt = k % (break_idx + 1)
        lo_cnt = (break_idx + 1) - mid_cnt
        res = res * (lo_val ** lo_cnt) % MODULO
        res = res * (mid_val ** mid_cnt) % MODULO
        for i in range(break_idx + 1, len(nums)):
            res = res * nums[i] % MODULO

        return res


# PriorityQueue (heapq)
# T/S: O(n + k*log(n)), O(1) by reusing nums
class Solution1:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MODULO = 10**9 + 7
        heapq.heapify(nums)
        for _ in range(k):
            v = nums[0] + 1
            heapq.heapreplace(nums, v)

        res = reduce(lambda x, y: x * y % MODULO, nums, 1)
        return res


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,), (Solution1,), (Solution3,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([0, 4], 5, 20),
            ([6, 3, 3, 2], 2, 216),
        ])
        def test_maximumProduct(self, nums, k, expected):
            sol = self.solution()       # type:ignore
            r = sol.maximumProduct(nums.copy(), k)  # nums is reused between test classes!!!
            self.assertEqual(r, expected)

    main()
