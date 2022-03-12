from typing import List

# Given an integer array nums of length n and an integer target, find three 
# integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
# Constraints:
#   3 <= nums.length <= 1000
#   -1000 <= nums[i] <= 1000
#   -10^4 <= target <= 10^4
from collections import Counter


# - to improve performance in case of lots of duplicates
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        freq = Counter(nums)
        N = []
        for v, cnt in sorted(freq.items()):
            N.extend([v] * min(cnt, 3))
        N.sort()

        res = N[0] + N[1] + N[2]
        for i in range(0, len(N)-2):
            j, k = i + 1, len(N) - 1
            while j < k:
                sum3 = N[i] + N[j] + N[k]
                if abs(res - target) > abs(sum3 - target):
                    res = sum3
                if sum3 < target:
                    j += 1
                elif sum3 > target:
                    k -= 1
                else:
                    return target

        return res


# Two pointers: O(n^2)
class Solution1:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums)-2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                if abs(res - target) > abs(sum3 - target):
                    res = sum3
                if sum3 < target:
                    j += 1
                elif sum3 > target:
                    k -= 1
                else:
                    return target

        return res


# Brute Force: O(n^3)
class Solution2:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if abs(res - target) > abs(nums[i] + nums[j] + nums[k] - target):
                        res = nums[i] + nums[j] + nums[k]

        return int(res)


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.threeSumClosest([-1, 2, 1, -4], 1)
        print(r)
        assert(r == 2)

        r = sol.threeSumClosest([0, 0, 0], 1)
        print(r)
        assert(r == 0)

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
