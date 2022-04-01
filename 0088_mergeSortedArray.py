# You are given two integer arrays nums1 and nums2, sorted in non-decreasing
# order, and two integers m and n, representing the number of elements in
# nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead
# be stored inside the array nums1. To accommodate this, nums1 has a length
# of m + n, where the first m elements denote the elements that should be
# merged, and the last n elements are set to 0 and should be ignored.
# nums2 has a length of n.
# Constraints:
#   nums1.length == m + n
#   nums2.length == n
#   0 <= m, n <= 200
#   1 <= m + n <= 200
#   -10^9 <= nums1[i], nums2[j] <= 10^9
from typing import List


# Array + Three Pointers: O(n+n)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        for i in reversed(range(m + n)):
            if p1 < 0 or p2 < 0:
                nums1[: p2 + 1] = nums2[: p2 + 1]
                return

            if nums1[p1] <= nums2[p2]:
                nums1[i] = nums2[p2]
                p2 -= 1
            else:
                nums1[i] = nums1[p1]
                p1 -= 1


if __name__ == "__main__":

    def unit_test(sol):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        Solution().merge(nums1, m, nums2, n)
        print(nums1)
        assert nums1 == [1, 2, 2, 3, 5, 6]

        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        Solution().merge(nums1, m, nums2, n)
        print(nums1)
        assert nums1 == [1]

        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        Solution().merge(nums1, m, nums2, n)
        print(nums1)
        assert nums1 == [1]

    unit_test(Solution())
