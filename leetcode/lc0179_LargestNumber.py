# Given a list of non-negative integers nums, arrange them such that
# they form the largest number and return it.
# Since the result may be very large, so you need to return a string
# instead of an integer.
# Constraints:
#   1 <= nums.length <= 100
#   0 <= nums[i] <= 10^9
from functools import cmp_to_key
from typing import List


# Sub-class of str
class LargerNumStr(str):
    def __lt__(self, y):
        return self + y > y + self


# Analysis:
# - consider following scenarios:
#   34323, 3432  => 3432 34323
# - the way to compare:
#   '34323' + '3432' v.s. '3432' + '34323', i.e.,
#   '343233432' (smaller)  v.s. '343234323' (larger)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = sorted(map(LargerNumStr, nums))
        return '0' if res[0] == '0' else ''.join(res)


# Analysis: (Wrong)
# - consider following scenarios:
#   3, 30 => 330
#   3, 31 => 331
#   3, 32 => 332
#   3, 33 => 333
#   3, 34 => 343
# - So the comparison should be:
#   3[3333333333] v.s. 30[000000000]    # ignore '[', ']'
#   3[3333333333] v.s. 34[444444444]    # ignore '[', ']'
class Solution1:
    def largestNumber(self, nums: List[int]) -> str:
        return "".join(sorted((str(x) for x in nums), 
                              key=lambda x: x.ljust(11, x[-1]), reverse=True))


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(("solution",), [(Solution,)])
    class TestSolution(TestCase):
        @parameterized.expand(
            [
                ([34323, 3432], "343234323"),
                ([10, 2], '210'),
                ([3, 30, 34, 5, 9], "9534330"),
            ]
        )
        def test_largestNumber(self, nums, expected):
            sol = self.solution()  # type:ignore
            r = sol.largestNumber(nums)
            self.assertEqual(r, expected)

    main()
