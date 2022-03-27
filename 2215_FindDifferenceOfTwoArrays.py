# Given two 0-indexed integer arrays nums1 and nums2, return a list answer
# of size 2 where:
# - answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# - answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.
# Constraints:
#   1 <= nums1.length, nums2.length <= 1000
#   -1000 <= nums1[i], nums2[i] <= 1000
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        res = [list(set1 - set2), list(set2 - set1)]
        return res


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6])
        print(r)
        assert r == [[1, 3], [4, 6]]

        r = sol.findDifference(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2])
        print(r)
        assert r == [[3], []]

    unitTest(Solution())
