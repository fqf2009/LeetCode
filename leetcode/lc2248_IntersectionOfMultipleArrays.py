# Given a 2D integer array nums where nums[i] is a non-empty array of distinct
# positive integers, return the list of integers that are present in each array
# of nums sorted in ascending order.
# Constraints:
#   1 <= nums.length <= 1000
#   1 <= sum(nums[i].length) <= 1000
#   1 <= nums[i][j] <= 1000
#   All the values of nums[i] are unique.
from functools import reduce
from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        return sorted(reduce(set.intersection, map(set, nums)))


class Solution1:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])
        for s in nums[1:]:
            res.intersection_update(s)
            if len(res) == 0:
                break

        return sorted(list(res))


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.intersection([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]])
        print(r)
        assert r == [3, 4]

        r = sol.intersection([[1, 2, 3], [4, 5, 6]])
        print(r)
        assert r == []

    unit_test(Solution())
    unit_test(Solution1())
