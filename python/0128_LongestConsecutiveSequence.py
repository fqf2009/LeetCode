# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
from typing import List

# Set (hash set): O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in numSet:
            if num - 1 not in numSet:   # possible start of consecutive sequency
                streak = 1
                v = num + 1
                while v in numSet:
                    streak += 1
                    v = v + 1
                res = max(res, streak)

        return res


# Sort: O(n*log(n))
class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        res = streak = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] + 1:
                streak += 1
                res = max(res, streak)
            else:
                streak = 1

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.longestConsecutive(nums=[])
        print(r)
        assert r == 0

        r = sol.longestConsecutive(nums=[100, 4, 200, 1, 3, 2])
        print(r)
        assert r == 4

        r = sol.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
        print(r)
        assert r == 9

    unitTest(Solution())
    unitTest(Solution1())
