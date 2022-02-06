# You are given a 0-indexed integer array nums. Rearrange the
# values of nums according to the following rules:
#  - Sort the values at odd indices of nums in non-increasing order.
#    For example, if nums = [4,1,2,3] before this step, it becomes
#    [4,3,2,1] after. The values at odd indices 1 and 3 are sorted
#    in non-increasing order.
#  - Sort the values at even indices of nums in non-decreasing order.
#    For example, if nums = [4,1,2,3] before this step, it becomes
#    [2,1,4,3] after. The values at even indices 0 and 2 are sorted
#    in non-decreasing order.
# Return the array formed after rearranging the values of nums.

from typing import List


# if nums can be reused
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        nums[1::2] = sorted(nums[1::2], reverse=True)
        nums[0::2] = sorted(nums[0::2])

        return nums


class Solution1:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        res[1::2] = sorted(nums[1::2], reverse=True)
        res[0::2] = sorted(nums[0::2])

        return res


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.sortEvenOdd(nums=[5, 39, 33, 5, 12, 27, 20, 45, 14, 25, 32, 33, 30, 30, 9, 14, 44, 15, 21])
        print(r)
        assert r == [5, 45, 9, 39, 12, 33, 14, 30, 20, 27, 21, 25, 30, 15, 32, 14, 33, 5, 44]

        r = sol.sortEvenOdd(nums=[4, 1, 2, 3])
        print(r)
        assert r == [2, 3, 4, 1]

        r = sol.sortEvenOdd([2, 1])
        print(r)
        assert r == [2, 1]

    unit_test(Solution())
    unit_test(Solution1())
