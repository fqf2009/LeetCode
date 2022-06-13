# You are given two arrays of integers nums1 and nums2, possibly of
# different lengths. The values in the arrays are between 1 and 6,
# inclusive.

# In one operation, you can change any integer's value in any of the
# arrays to any value between 1 and 6, inclusive.

# Return the minimum number of operations required to make the sum of
# values in nums1 equal to the sum of values in nums2. Return -1​​​​​ if
# it is not possible to make the sum of the two arrays equal.

# Constraints:
#   1 <= nums1.length, nums2.length <= 10^5
#   1 <= nums1[i], nums2[i] <= 6
from typing import Counter, List


# Counter: T/S: O(m+n), O(1), the sort() over 6 items can be ignored
# - one array is to increase, another is to decrease, combine them
#   together and calulate.
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        if not (m <= n <= 6 * m or m <= 6 * n <= 6 * m):
            return -1
        total1, total2 = sum(nums1), sum(nums2)
        if total1 == total2:
            return 0
        elif total1 > total2:
            diff = total1 - total2
            N1, N2 = nums1, nums2
        else:
            N1, N2 = nums2, nums1
            diff = total2 - total1

        res = 0
        cntr = Counter(x - 1 for x in N1) + Counter(6 - x for x in N2)
        for delta, freq in sorted(cntr.items(), reverse=True):
            if delta * freq >= diff:
                res += diff // delta
                if diff % delta > 0:
                    res += 1
                break
            res += freq
            diff -= delta * freq

        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.minOperations([1, 2, 3, 4, 5, 6], [1, 1, 2, 2, 2, 2])
        print(r)
        assert r == 3

        r = sol.minOperations([1, 1, 1, 1, 1, 1, 1], [6])
        print(r)
        assert r == -1

        r = sol.minOperations([6, 6], [1])
        print(r)
        assert r == 3

        nums1 = [1,2,6,4,1,5,4,6,5,4,4,6,6,4,3,3,1,2,1,6,2,2,4,2,5,5,3,1,4,
                 2,2,1,4,4,5,6,1,3,4,1,3,5,3,5,3,4,4,4,3,3,5,1,2,2,4,5,2,1,
                 2,3,3,4,1,3,2,4,1,3,5,1,6,3,3,4,6,5,5,2,6,5,4,5]
        nums2 = [6,3,4,6,4,3,6,4,2,4,5,5,1,1,3,2,1,1,4,2,5,1,5,6,6,2,1,3,4,
                 6,4,6,3,6,1,1,4,4,6,3,3,5,5,4,6,6,1,3,4,1,3,5,1,1,1,5,2,1,
                 1,1,2,3,6,6,2,5,4,2,1,5,3,1,2,3,6,4,2,5,4,6,6,6,6,6,3,2,2,
                 2,1,6,4,5,6,1,5,1,5,6,6,4,6,5,3,4,1,3,2,1,5,1,1,1,2,3,6,6,
                 6,4,6,3,6,4,4,6,3,6,3,6,2,6,5,1,1,6,4,3,4,2,5,3,3,5,2,3,1,
                 3,2,6,5,1,2,4,4,6,2,1,4,3,3,3,3,5,6,1,6,4,2,3,5,4,6,1,3,6,
                 1,2,2,1,3,5,6,2,3,6,5,3,4,1,3,1,2,3,5,4,2,1,2,1,2,5,2,4,4,
                 4,2,5,2,4,3,2,1,5,1,3,3,1,1,1,1,6,1,3,6,2,3,6,3,3,4,5,2,1,
                 3,3,4,1,4,3,4,4,3,2,1,4,5,2,1,2,5,6,1,5,2,4,5,1,6,2,6,1,3,
                 6,2,3,6,6,3,2,2,3,1,6,1,5,6,4,2,3,5,2,6,3,5,4,2,6,6,6,5,5,
                 4,2,3,1,1,4,4,4,5,2,4,3,6,4,3,3,2,3,4,6,1,1,6,1,6,2,4,5,4,
                 2,4,4,4,1,1,1,1,3,4,1,2,5,1,2,1,4,5,6,4,6,4,3,1,6,5,5,2,1,
                 1,1,1,6,5,5,3,2,2,2,2,6,2,3,3,5,1,6,5,6,2,2,1,6,1,6,5,2,5,
                 4,4,1,5,5,6,4,4,1,3,1,6,4,4,3,1,6,6,6,4,6,5,3,6,4,3,6,2,3,
                 3,3,2,4,2,2,2,3,5,2,6,5,4,5,4,2,5,1,3,6,4,1,2,1,3,3,3,3,1]
        r = sol.minOperations(nums1, nums2)
        print(r)
        assert r == 368

    unit_test(Solution())
