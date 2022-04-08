# You are given a 0-indexed integer array nums. An index i is part of a hill 
# in nums if the closest non-equal neighbors of i are smaller than nums[i]. 
# Similarly, an index i is part of a valley in nums if the closest non-equal 
# neighbors of i are larger than nums[i]. Adjacent indices i and j are part of 
# the same hill or valley if nums[i] == nums[j].
# Note that for an index to be part of a hill or valley, it must have a non-equal 
# neighbor on both the left and right of the index.
# Return the number of hills and valleys in nums.
# Constraints:
#   3 <= nums.length <= 100
#   1 <= nums[i] <= 100
from typing import List


# T/S: O(n), O(1)
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0
        v1 = v2 = v3 = -1
        for v in nums:
            if v == v3: continue
            v1, v2, v3 = v2, v3, v
            if v1 == -1: continue
            if v2 < min(v1, v3) or v2 > max(v1, v3):
                res += 1

        return res


# T/S: O(n), O(n)
# get unique array first, then ...
class Solution1:
    def countHillValley(self, nums: List[int]) -> int:
        nums2 = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            nums2.append(nums[i])

        res = 0
        for i in range(2, len(nums2)):
            v1, v2, v3 = nums2[i-2:i+1]
            if (v1 < v2 and v3 < v2) or (v1 > v2 and v3 > v2):
                res += 1

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.countHillValley([2, 4, 1, 1, 6, 5])
        print(r)
        assert r == 3

        r = sol.countHillValley([6, 6, 5, 5, 4, 1])
        print(r)
        assert r == 0

    unitTest(Solution())
    unitTest(Solution1())
