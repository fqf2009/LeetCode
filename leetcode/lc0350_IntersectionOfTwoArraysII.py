from collections import Counter
from functools import reduce
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((Counter(nums1) & Counter(nums2)).elements())
        # return reduce(lambda x, y: x + y, ([v] * freq for v, freq
        #             in (Counter(nums1) & Counter(nums2)).items()))


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,),])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([1,2,2,1], [2,2], [2,2]),
            ([4,9,5], [9,4,9,8,4], [9,4]),
        ])
        def test_intersect(self, nums1, nums2, expected):
            sol = self.solution()       # type:ignore
            r = sol.intersect(nums1, nums2)
            self.assertEqual(sorted(r), sorted(expected))

    main()
