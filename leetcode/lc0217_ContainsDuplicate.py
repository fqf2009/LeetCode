# Given an integer array nums, return true if any value appears at least
# twice in the array, and return false if every element is distinct.
# Constraints:
#   1 <= nums.length <= 10^5
#   -10^9 <= nums[i] <= 10^9
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for v in nums:
            if v in nums_set:
                return True
            nums_set.add(v)

        return False


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([1,2,3,1], True),
            ([1,2,3,4], False),
            ([1,1,1,3,3,4,3,2,4,2], True),
        ])
        def test_containsDuplicate(self, nums, expected):
            sol = self.solution()       # type:ignore
            r = sol.containsDuplicate(nums)
            self.assertEqual(r, expected)

    main()
