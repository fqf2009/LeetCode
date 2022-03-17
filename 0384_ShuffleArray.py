# Given an integer array nums, design an algorithm to randomly shuffle
# the array. All permutations of the array should be equally likely as
# a result of the shuffling.
# Implement the Solution class:
# - Solution(int[] nums) Initializes the object with the integer array nums.
# - int[] reset() Resets the array to its original configuration and returns it.
# - int[] shuffle() Returns a random shuffling of the array.
# Constraints:
#   1 <= nums.length <= 200
#   -106 <= nums[i] <= 106
#   All the elements of nums are unique.
#   At most 5 * 104 calls in total will be made to reset and shuffle.
from typing import List
from math import floor
import random


# - from Python ramdom.shuffle():
# for i in reversed(range(1, len(x))):
#     # pick an element in x[:i+1] with which to exchange x[i]
#     j = floor(random() * (i + 1))
#     x[i], x[j] = x[j], x[i]


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        nums2 = self.nums.copy()
        for i in reversed(range(1, len(nums2))):
            j = floor(random.random() * (i + 1))
            nums2[i], nums2[j] = nums2[j], nums2[i]

        return nums2


class Solution1:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        return random.sample(self.nums, len(self.nums))


if __name__ == '__main__':
    def unitTest(sol):
        obj = sol([1, 2, 3, 4, 5])
        for _ in range(5):
            r = obj.shuffle()
            print(r)
            assert sum(r) == sum(range(1, 6))

        r = obj.reset()
        print(r)
        assert r == [1, 2, 3, 4, 5]

    unitTest(Solution)
    unitTest(Solution1)
