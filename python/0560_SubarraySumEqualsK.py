from typing import List, Optional

# Given an array of integers nums and an integer k, return the total number 
# of continuous subarrays whose sum equals to k.

# csum is a dict, in which key is the cumulative sum of nums when visiting
# each item, and value is how many times this cumulative sum ever happened.
# The 'total' is the cumulative_sum when visiting each int. Any time
# (total - k) is also in csum dict, it means that the sum between two csum
# is k, and csum(total - k) is count of the distinct continous subarrays.
from collections import defaultdict

# use defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        csum = defaultdict(int)
        csum[0] = 1
        res, total = 0, 0
        for v in nums:
            total += v
            if total - k in csum:
                res += csum[total - k]
            csum[total] = csum[total] + 1
            
        return res


# Time complexity: O(n), Space complexity: O(n)
class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        csum = {0: 1}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total - k in csum:
                res += csum[total - k]
            csum[total] = csum.setdefault(total, 0) + 1

        return res


# Brute Force: O(n^2)
class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total == k:
                    res += 1

        return res


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.subarraySum([1, -3, -2, 9, -8, 6, 2, 7, 4, 3, 1, 1], 2)
        print(r)
        assert(r == 3)

        r = sol.subarraySum([1, 1, 1], 2)
        print(r)
        assert(r == 2)

        r = sol.subarraySum([1, 2, 3], 3)
        print(r)
        assert(r == 2)

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
