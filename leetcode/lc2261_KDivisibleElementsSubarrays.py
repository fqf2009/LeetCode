# Given an integer array nums and two integers k and p, return the number of distinct 
# subarrays which have at most k elements divisible by p.
# Two arrays nums1 and nums2 are said to be distinct if:
# They are of different lengths, or
# There exists at least one index i where nums1[i] != nums2[i].
# A subarray is defined as a non-empty contiguous sequence of elements in an array.
# Example 1:
#   Input: nums = [2,3,3,2,2], k = 2, p = 2
#   Output: 11
#   Explanation:
#       The elements at indices 0, 3, and 4 are divisible by p = 2.
#       The 11 distinct subarrays which have at most k = 2 elements divisible by 2 are:
#       [2], [2,3], [2,3,3], [2,3,3,2], [3], [3,3], [3,3,2], [3,3,2,2], [3,2], [3,2,2], and [2,2].
#       Note that the subarrays [2] and [3] occur more than once in nums, but they should each be counted only once.
#       The subarray [2,3,3,2,2] should not be counted because it has 3 elements that are divisible by 2.
# Constraints:
#   1 <= nums.length <= 200
#   1 <= nums[i], p <= 200
#   1 <= k <= nums.length
from typing import List


# Sliding Window - T/S: O(n^2), O(n^2)
# Analysis:
# - iterate over nums, and use array pos[] to hold all position of numbers divisible by p;
# - note if a sub-array has zero items divisible by q, it is still valid;
# - always focus on sub-array ending with pos i;
# - all sub-array from the pos after previous last (k+1)-th eligible items to current pos, are valid;
# - if no (k+1) eligible (divisible by q) items, start from beginning;
# - add all sub-array (convert into tuple) to set to de-dup.
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        res = set()
        pos = []
        for i, v in enumerate(nums):
            if v % p == 0:
                pos.append(i)
            start = pos[-k-1] + 1 if len(pos) > k else 0
            for j in range(start, i+1):
                res.add(tuple(nums[j: i+1]))

        return len(res)


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.countDistinct([6,20,5,18], 3, 14)
        print(r)
        assert r == 10

        r = sol.countDistinct([2,3,3,2,2], k = 2, p = 2)
        print(r)
        assert r == 11

        r = sol.countDistinct([1,2,3,4], k = 4, p = 1)
        print(r)
        assert r == 10

    unit_test(Solution())
