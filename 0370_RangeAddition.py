# You are given an integer length and an array updates where
# updates[i] = [startIdxi, endIdxi, inci].
# You have an array arr of length length with all zeros, and
# you have some operation to apply on arr. In the ith operation,
# you should increment all the elements arr[startIdxi],
# arr[startIdxi + 1], ..., arr[endIdxi] by inci.
# Return arr after applying all the updates.
# Constraints:
#   1 <= length <= 10^5
#   0 <= updates.length <= 10^4
#   0 <= startIdxi <= endIdxi < length
#   -1000 <= inci <= 1000
from typing import List


# Math? - O(n+m), where m = len(updates)
# - iterate over updates, put inc to res[start], -inc to res[stop-1],
#   to mark the intended change at the start and after stop place.
# - iterate over result array, if the value is this position is zero,
#   set the value to the same as the value of previous pos, if the 
#   value is not zero, add it with the value previous pos, as new value.
#       if res[i] != 0:
#           res[i] = res[i-1] + res[i]
#       else:
#           res[i] = res[i-1]
# - this can be simplified as: res[i] = res[i-1] + res[i]
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * (length+1)      # edge condition
        for start, stop, inc in updates:
            res[start] += inc
            res[stop+1] -= inc      # !!!stop + 1
        
        for i in range(1, length):
            res[i] = res[i-1] + res[i]

        return res[:length]


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.getModifiedArray(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]])
        print(r)
        assert r == [-2, 0, 3, 5, 3]

        r = sol.getModifiedArray(10, [[2, 4, 6], [5, 6, 8], [1, 9, -4]])
        print(r)
        assert r == [0, -4, 2, 2, 2, 4, 4, -4, -4, -4]

    unitTest(Solution())
