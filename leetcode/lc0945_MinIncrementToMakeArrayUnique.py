# You are given an integer array nums. In one move, you can pick an
# index i where 0 <= i < nums.length and increment nums[i] by 1.
# Return the minimum number of moves to make every value in nums unique.
# The test cases are generated so that the answer fits in a 32-bit integer.
# Constraints:
#   1 <= nums.length <= 10^5
#   0 <= nums[i] <= 10^5
from typing import List


# T/S: O(n*log(n)), O(n) due to sort
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        dup, prev, res = 0, -1, 0
        for v in sorted(nums):
            if v == prev:
                dup += 1
            else:
                n = min(dup, v - prev - 1)  # fill in the gap
                res += (1 + n) * n // 2
                dup -= n
                res += dup * (n + 1)    # remainig items, one more step for each
                prev = v

        return res + (1 + dup) * dup // 2


# much simpler and easier to understand
class Solution1:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        next, res = -1, 0
        for v in nums:
            if v < next:
                res += next - v     # steps to move v to next
                next += 1
            else:
                next = v + 1

        return res


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.minIncrementForUnique([7,2,7,2,1,4,3,1,4,8])
        print(r)
        assert r == 16

        r = sol.minIncrementForUnique([1, 2, 2])
        print(r)
        assert r == 1

        r = sol.minIncrementForUnique([3, 2, 1, 2, 1, 7])
        print(r)
        assert r == 6

        r = sol.minIncrementForUnique([1, 2, 3])
        print(r)
        assert r == 0

    unitTest(Solution())
    unitTest(Solution1())
