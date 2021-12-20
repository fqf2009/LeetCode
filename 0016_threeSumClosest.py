from typing import List

# Given an integer array nums of length n and an integer target, find three 
# integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.


# Two pointers: O(n^2)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        diff = float('inf')
        for i in range(0, len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                delta = target - (nums[i] + nums[j] + nums[k])
                if abs(delta) < abs(diff):
                    diff = delta
                if delta == 0:
                    break
                elif delta > 0:
                    j += 1
                else:
                    k -= 1

        return target - int(diff)


# Brute Force: O(n^3)
class Solution1:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if abs(res - target) > abs(nums[i] + nums[j] + nums[k] - target):
                        res = nums[i] + nums[j] + nums[k]

        return int(res)


if __name__ == '__main__':
    sol = Solution()

    r = sol.threeSumClosest([-1, 2, 1, -4], 1)
    print(r)
    assert(r == 2)
