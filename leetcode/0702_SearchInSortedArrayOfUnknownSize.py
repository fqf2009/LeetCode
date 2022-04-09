# This is an interactive problem.
# You have a sorted array of unique elements and an unknown size. You do not 
# have an access to the array but you can use the ArrayReader interface to 
# access it. You can call ArrayReader.get(i) that:
# returns the value at the ith index (0-indexed) of the secret array (i.e., secret[i]), or
# returns 231 - 1 if the i is out of the boundary of the array.
# You are also given an integer target.
# Return the index k of the hidden array where secret[k] == target or return -1 otherwise.
# You must write an algorithm with O(log n) runtime complexity.
# Constraints:
#   1 <= secret.length <= 10^4
#   -10^4 <= secret[i], target <= 10^4
#   secret is sorted in a strictly increasing order.

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
class ArrayReader:
    def get(self, index: int) -> int:
        pass

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        lo, hi = 0, 10000
        while lo <= hi:
            mid = (lo+hi) // 2
            val = reader.get(mid)
            if val == 2**31-1 or val > target:
                hi = mid - 1
            elif val < target:
                lo = mid + 1
            else:
                return mid
        
        return -1
