# A peak element is an element that is strictly greater than its neighbors.
# Given an integer array nums, find a peak element, and return its index.
# If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞.
# You must write an algorithm that runs in O(log n) time.
from typing import List
import numpy as np


# Binary Search to find any peak
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            k = (i+j) // 2
            if nums[k] < nums[k+1]:
                i = k + 1
            else:
                j = k
        return i


# Below are all to find highest peak, this problem only need any one of the peaks

# Oneliner - O(n) 
# https://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
# -   max_index, max_value = max([(j, i) for i, j in enumerate(values)])
# -   max_index, max_value = max(enumerate(values), key=operator.itemgetter(1))
class Solution1:
    def findPeakElement(self, nums: List[int]) -> int:
        return max(range(len(nums)), key=nums.__getitem__)


class Solution2:
    def findPeakElement(self, nums: List[int]) -> int:
        return int(np.argmax(nums))


# O(n)
class Solution3:
    def findPeakElement(self, nums: List[int]) -> int:
        peak = nums[0]
        res = 0
        for i in range(1, len(nums)):
            if peak < nums[i]:
                peak = nums[i]
                res = i

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.findPeakElement(nums=[1, 2, 3, 1])
        print(r)
        assert r == 2

        r = sol.findPeakElement(nums=[1, 2, 3])
        print(r)
        assert r == 2

        r = sol.findPeakElement(nums=[4, 2, 3, 1])
        print(r)
        assert r == 0 or r == 2

        r = sol.findPeakElement(nums=[1, 2, 1, 3, 5, 6, 4])
        print(r)
        assert r == 5 or r == 1

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
    unitTest(Solution3())
