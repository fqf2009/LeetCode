# Given a sorted integer array arr, two integers k and x, return the k
# closest integers to x in the array. The result should also be sorted
# in ascending order.
# An integer a is closer to x than an integer b if:
#   |a - x| < |b - x|, or
#   |a - x| == |b - x| and a < b
# Constraints:
#   1 <= k <= arr.length
#   1 <= arr.length <= 10^4
#   arr is sorted in ascending order.
#   -10^4 <= arr[i], x <= 10^4
from typing import List


# Binary Search: O(log(n-k)+k)
# - binary seaarch to find the left edge of k-length subarray
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i, j = 0, len(arr) - k
        while i < j:    # exit condition: i == j
            m = (i + j) // 2  # the left edge of k-length subarray
            # x_to_left_item_distance v.s. right_plus_1_item_to_x_distance, i.e.,
            # besides (k-1) shared items, pick either arr[m] or arr[m+k] ?
            if x - arr[m] > arr[m + k] - x:     # do not pick arr[:m]
                i = m + 1
            else:                               # do not pick arr[m+1:]
                j = m

        return arr[i: i + k]


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.findClosestElements([0, 2, 2, 3, 4, 6, 7, 8, 9, 9], k=4, x=5)
        print(r)
        assert r == [3, 4, 6, 7]

        r = sol.findClosestElements([1, 2, 3, 4, 5], k=4, x=3)
        print(r)
        assert r == [1, 2, 3, 4]

        r = sol.findClosestElements([1, 2, 3, 4, 5], k=4, x=-1)
        print(r)
        assert r == [1, 2, 3, 4]

    unit_test(Solution())
