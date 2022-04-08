# Given an integer array nums with possible duplicates, randomly output
# the index of a given target number. You can assume that the given target
# number must exist in the array.
# Implement the Solution class:
#  - Solution(int[] nums) Initializes the object with the array nums.
#  - int pick(int target) Picks a random index i from nums where
#    nums[i] == target. If there are multiple valid i's, then each
#    index should have an equal probability of returning.
# Constraints:
#   1 <= nums.length <= 2 * 10^4
#   -2^31 <= nums[i] <= 2^31 - 1
#   target is an integer from nums.
#   At most 10^4 calls will be made to pick.
from collections import defaultdict
from random import randint
from typing import List


# Reservoir Sampling
# https://en.wikipedia.org/wiki/Reservoir_sampling
# https://leetcode.com/problems/linked-list-random-node/discuss/85659/brief-explanation-for-reservoir-sampling
# https://zhuanlan.zhihu.com/p/29178293
# - loop over all items:
#   - if the first time encounter target, pick its index at 1/1 probability.
#   - if the second time encounter it, pick its index at 1/2 probability.
#   - if the k-th time encounter it, pick its index at 1/k probability.
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        idx = 0
        for i, v in enumerate(self.nums):
            if v == target:
                count += 1
                if randint(1, count) == 1:
                    idx = i

        return idx


# HashMap, Random
class Solution1:
    def __init__(self, nums: List[int]):
        self.nums_idx = defaultdict(list)
        for i, v in enumerate(nums):
            self.nums_idx[v].append(i)

    def pick(self, target: int) -> int:
        idx = self.nums_idx[target]
        return idx[randint(0, len(idx) - 1)]


if __name__ == "__main__":

    def unitTest(Sol):
        inputs = [["pick", "pick", "pick"], [[3], [1], [3]]]
        expected = [None, 4, 0, 2]
        outputs = [None]
        obj = Sol([1, 2, 3, 3, 3])  # obj = Solution(nums)
        for method, param in zip(inputs[0], inputs[1]):
            r = getattr(obj, method)(*param)  # obj.pick(target)
            outputs.append(r)
        print(outputs)
        # assert outputs == expected

    unitTest(Solution)
