# Given an array of positive integers arr, calculate
# the sum of all possible odd-length subarrays.
# A subarray is a contiguous subsequence of the array.
# Return the sum of all odd-length subarrays of arr.

# Example 1:
#  Input: arr = [1,4,2,5,3]
#  Output: 58
#  Explanation: The odd-length subarrays of arr and their sums are:
#  [1] = 1
#  [4] = 4
#  [2] = 2
#  [5] = 5
#  [3] = 3
#  [1,4,2] = 7
#  [4,2,5] = 11
#  [2,5,3] = 10
#  [1,4,2,5,3] = 15
#  If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

from typing import List


# Time complexity O(n^2)
# Analysis:
# - Assume lenth of array is n, and length of subarray is m.
# - when m == 1, every item is used 1 time
# - when m == 3, the 1st item is used 1 time, the 2nd is used 2 times,
#   the 3rd and 4th,..., are used 3 times. Note for nth, (n-1)th, (n-2)th, ...
#   items, they do the opposite, i.e., are used 1, 2, 3, 3, ... times.
# - when m is getting big, there is only (n-m+1) subarrays.
# - Therefore for all subarrays with length m, the i-th item will be used:
#   min(m, n-m, min(i+1, n-i)) times, where i is 0-based index.
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)
        for i in range(n):
            for m in range(1, n+1, 2):
                res += arr[i] * min(m, n-m+1, min(i+1, n-i))

        return res


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.sumOddLengthSubarrays([1, 4, 2, 5, 3])
        print(r)
        assert r == 58

        r = sol.sumOddLengthSubarrays([1, 2])
        print(r)
        assert r == 3

        r = sol.sumOddLengthSubarrays([10, 11, 12])
        print(r)
        assert r == 66

    unit_test(Solution())
