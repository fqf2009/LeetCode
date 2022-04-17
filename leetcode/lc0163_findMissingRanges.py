# You are given an inclusive range [lower, upper] and a sorted unique integer 
# array nums, where all elements are in the inclusive range.
# A number x is considered missing if x is in the range [lower, upper] 
# and x is not in nums.
# Return the smallest sorted list of ranges that cover every missing 
# number exactly. That is, no element of nums is in any of the ranges, 
# and each missing number is in one of the ranges.
# Each range [a,b] in the list should be output as:
# "a->b" if a != b
# "a" if a == b
# Constraints:
#   -10^9 <= lower <= upper <= 10^9
#   0 <= nums.length <= 100
#   lower <= nums[i] <= upper
#   All the values of nums are unique.
from itertools import chain
from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        lo = lower - 1
        res = []
        for n in chain(nums, [upper + 1]):
            if lo < n - 2:
                res.append(f'{lo+1}->{n-1}')
            elif lo == n - 2:
                res.append(f'{n-1}')
            lo = n
        return res


if __name__ == "__main__":
    r = Solution().findMissingRanges([0,1,3,50,75], lower = 0, upper = 99)
    print(r)
    assert(r == ["2","4->49","51->74","76->99"])

    r = Solution().findMissingRanges(nums = [], lower = 1, upper = 1)
    print(r)
    assert(r == ["1"])

    r = Solution().findMissingRanges(nums = [], lower = -3, upper = -1)
    print(r)
    assert(r == ["-3->-1"])

    r = Solution().findMissingRanges(nums = [-1], lower = -1, upper = -1)
    print(r)
    assert(r == [])

    r = Solution().findMissingRanges(nums = [-1], lower = -2, upper = -1)
    print(r)
    assert(r == ["-2"])
