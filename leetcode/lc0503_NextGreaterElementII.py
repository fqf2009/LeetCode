# Given a circular integer array nums (i.e., the next element of
# nums[nums.length - 1] is nums[0]), return the next greater number
# for every element in nums.
# The next greater number of a number x is the first greater number
# to its traversing-order next in the array, which means you could
# search circularly to find its next greater number. If it doesn't
# exist, return -1 for this number.
# Constraints:
#   1 <= nums.length <= 10^4
#   -10^9 <= nums[i] <= 10^9
from itertools import chain
from typing import List


# Monotonic Stack: T/S: O(n), O(n)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        start = (max((v, i) for i, v in enumerate(nums))[1] + 1) % n
        stack = []      # Monotonic decreasing, because we want next greater
        res = [-1] * n
        for i, v in enumerate(chain(nums[start:], nums[:start])):
            j = (i + start) % n
            while stack and nums[stack[-1]] < v:
                res[stack.pop()] = v
            stack.append(j)

        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.nextGreaterElements([1, 2, 1])
        print(r)
        assert r == [2, -1, 2]

        r = sol.nextGreaterElements([1, 2, 3, 4, 3])
        print(r)
        assert r == [2, 3, 4, -1, 4]

    unit_test(Solution())
