# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must be unique and you may 
# return the result in any order.
# Constraints:
#   1 <= nums1.length, nums2.length <= 1000
#   0 <= nums1[i], nums2[i] <= 1000
from typing import List


# for extra conditions:
# - no extra space (so no set operation)
# - can sort the array, or they are already sorted
# - can have duplicates, single value lists, 0's, empty lists
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        res = []
        while i < m and j < n:
            v1, v2 = nums1[i], nums2[j]
            if v1 is None:
                i += 1
            elif v2 is None:
                j += 1
            elif v1 < v2:
                i += 1
            elif v1 > v2:
                j += 1
            else:
                i += 1
                j += 1
                if not res or res[-1] != v1:
                    res.append(v1)

        return res


class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        return list(set(x for x in nums2 if x in set(nums1)))


class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,), (Solution1,), (Solution2,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([1,2,2,1], [2,2], [2]),
            ([4,9,5], [9,4,9,8,4], [9,4]),
        ])
        def test_intersection(self, nums1, nums2, expected):
            sol = self.solution()       # type:ignore
            r = sol.intersection(nums1, nums2)
            self.assertEqual(sorted(r), sorted(expected))

    main()
