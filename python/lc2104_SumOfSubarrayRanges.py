# You are given an integer array nums. The range of a subarray of nums is
# the difference between the largest and smallest element in the subarray.
# Return the sum of all subarray ranges of nums.
# A subarray is a contiguous non-empty sequence of elements within an array.
# Constraints:
#   1 <= nums.length <= 1000
#   -109 <= nums[i] <= 10^9
# Follow-up: Could you find a solution with O(n) time complexity?
from itertools import chain
from typing import List


# Monotonic Stack - T/S: O(n), O(n)
# - Instead of iterating over all subarray, just calculate the number of
#   contributions of each value as the maximum or minimum.
# - Use a decreasing monotonic stack:
#   - if new value (v2) is smaller than stack top item, keep push value
#     (or its index) into stack
#   - otherwise, pop one item from stack, it is v1, new stack top is v0,
#     obviously: v0 > v1, and v1 <= v2; so v1 is maximum value in subarray
#     (v0, ..., v1, ... v2) non-inclusive!!!
#   - the contributions of v1 as maximum is as below:
#     assume: p0, p1, p2 is the pos or index of each value
#     nLeft = (p1-p0-1), nRight = (p2-p1-1), i.e. how many items at the
#     left or right side of v1 which are smaller than v1:
#     contributions = nLeft + nRight + (nLeft - 1) * (nRight - 1) + 1
#     e.g.: for a subarray: a, b, M, c, d, e, where M is max(a, b, ..., e)
#       nLeft = 2, nRight = 3
#       contributions:
#                                    (a, b, M), (b, M), i.e. nLeft
#                      (M, c), (M, c, d), (M, c, d, e), i.e. nRight
#             (b, M, c), (b, M, c, d), (b, M, c, d, e), i.e. nLeft*nRight
#    (a, b, M, c), (a, b, M, c, d), (a, b, M, c, d, e),
#                                            (M), i.e., 1 (can be omitted)
#   - note that to count v2's contribution as maximum, need to wait next
#     value bigger than v2, so append a big int at the end of nums to
#     simulate this.
# - Use a increasing monotonic stack to calculate contributions as minimum
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        stk = []
        for i, v in enumerate(chain(nums, [2**63-1])):
            while stk and v >= nums[stk[-1]]:
                mid = stk.pop()
                left = stk[-1] if stk else -1
                nLeft = (mid-left-1)
                nRight = (i-mid-1)
                res += nums[mid] * (nLeft + nRight + nLeft * nRight)
            stk.append(i)

        stk = []
        for i, v in enumerate(chain(nums, [-2**63])):
            while stk and v <= nums[stk[-1]]:
                mid = stk.pop()
                left = stk[-1] if stk else -1
                nLeft = (mid-left-1)
                nRight = (i-mid-1)
                res -= nums[mid] * (nLeft + nRight + nLeft * nRight)
            stk.append(i)

        return res


# DP - T/S: O(n^2), O(n)
# - iterate over nums, for each nums[i]
#   minVal[j] is minimum value in subarray nums[j:i+1)
#   maxVal[j] is maximum value in subarray nums[j:i+1)
class Solution1:
    def subArrayRanges(self, nums: List[int]) -> int:
        minVal = nums.copy()
        maxVal = nums.copy()
        res = 0
        for i in range(1, len(nums)):
            for j in range(0, i):
                minVal[j] = min(minVal[j], nums[i])
                maxVal[j] = max(maxVal[j], nums[i])
                res += (maxVal[j] - minVal[j])

        return res


if __name__ == '__main__':
    def unitTest(sol):
        nums = [-561, 644]
        r = sol.subArrayRanges(nums)
        print(r)
        assert r == 1205

        nums = [-561, 644, -637, 786, -32, 771, -22, 419, -837, 947, -359, -874, 489, 195]
        r = sol.subArrayRanges(nums)
        print(r)
        assert r == 139349

        r = sol.subArrayRanges([1, 2, 3])
        print(r)
        assert r == 4

        r = sol.subArrayRanges([1, 3, 3])
        print(r)
        assert r == 4

        r = sol.subArrayRanges([4, -2, -3, 4, 1])
        print(r)
        assert r == 59

        r = sol.subArrayRanges([4, -2, -3, 4, 1, 5, 8, 7, 6])
        print(r)
        assert r == 245

        print('')


    unitTest(Solution())
    unitTest(Solution1())
