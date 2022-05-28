# Given an array nums with n objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red,
# white, and blue, respectively.
# You must solve this problem without using the library's sort function.
# Constraints:
#   n == nums.length
#   1 <= n <= 300
#   nums[i] is either 0, 1, or 2.
from itertools import chain, repeat
from typing import Counter, List


# Counter
class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        cnt = Counter(nums)
        nums[:] = chain(repeat(0, cnt[0]), repeat(1, cnt[1]), repeat(2, cnt[2]))


# Three pointers
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] == 0:
                i += 1
            elif nums[j] == 2:
                j -= 1
            elif nums[i] == 2:
                nums[i], nums[j] = nums[j], nums[i]
            elif nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                k = i + 1
                while k < j and nums[k] == 1:
                    k += 1
                if k == j: break
                if nums[k] == 0:
                    nums[i], nums[k] = nums[k], nums[i]
                else:
                    nums[j], nums[k] = nums[k], nums[j]


if __name__ == "__main__":

    def unit_test(sol):
        nums = [2, 0, 2, 1, 1, 0]
        sol.sortColors(nums)
        print(nums)
        assert nums == [0, 0, 1, 1, 2, 2]

        nums = [2, 0, 1]
        sol.sortColors(nums)
        print(nums)
        assert nums == [0, 1, 2]

    unit_test(Solution())
    unit_test(Solution1())
