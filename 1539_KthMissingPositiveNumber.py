# Given an array arr of positive integers sorted in a strictly 
# increasing order, and an integer k.
# Find the kth positive integer that is missing from this array.
# Constraints:
#   1 <= arr.length <= 1000
#   1 <= arr[i] <= 1000
#   1 <= k <= 1000
#   arr[i] < arr[j] for 1 <= i < j <= arr.length
from typing import List


# Array
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        prev = 0
        missing = k
        for val in arr:
            if missing <= val - prev - 1:
                break
            else:
                missing -= (val - prev - 1)
            prev = val

        return prev + missing


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.findKthPositive([2,3,4,7,11], k = 5)
        print(r)
        assert r == 9

        r = sol.findKthPositive([1,2,3,4], k = 2)
        print(r)
        assert r == 6

    unit_test(Solution())
