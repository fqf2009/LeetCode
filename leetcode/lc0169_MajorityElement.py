# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.
# Constraints:
#   n == nums.length
#   1 <= n <= 5 * 10^4
#   -10^9 <= nums[i] <= 10^9
# Follow-up: Could you solve the problem in linear time and in O(1) space?

from typing import Counter, List
from webbrowser import get


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max((f, v) for v, f in Counter(nums).items())[1]


class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return max(counter.keys(), key = counter.get)     # type: ignore


# Boyer-Moore Voting Algorithm - T/S: O(n), O(1)
# - intuition:
#   - only remember the most frequent one
#   - count against different one (+1 for candidate, -1 non-candidate)
#   - when count is 0, start over
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        candidate = nums[0]
        for v in nums[1:]:
            if count == 0:
                candidate = v
            count += 1 if v == candidate else -1

        return candidate


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(("solution",), [(Solution,), (Solution1,), (Solution2,)])
    class TestSolution(TestCase):
        @parameterized.expand(
            [
                ([3,2,3], 3),
                ([2,2,1,1,1,2,2], 2),
            ]
        )
        def test_majorityElement(self, nums, expected):
            sol = self.solution()  # type:ignore
            r = sol.majorityElement(nums)
            self.assertEqual(r, expected)

    main()
