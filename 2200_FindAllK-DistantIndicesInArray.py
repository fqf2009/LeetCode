# You are given a 0-indexed integer array nums and two integers key and k.
# A k-distant index is an index i of nums for which there exists at least 
# one index j such that |i - j| <= k and nums[j] == key.
# Return a list of all k-distant indices sorted in increasing order.
# Constraints:
#   1 <= nums.length <= 1000
#   1 <= nums[i] <= 1000
#   key is an integer from the array nums.
#   1 <= k <= nums.length
from typing import List


# Array: O(n)
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        right = -1
        res = []
        for i, v in enumerate(nums):
            if v == key:
                left = max(right + 1, i - k)
                right = min(i + k, n - 1)
                res.extend(range(left, right + 1))

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.findKDistantIndices(nums=[3, 4, 9, 1, 3, 9, 5], key=9, k=1)
        print(r)
        assert r == [1, 2, 3, 4, 5, 6]

        r = sol.findKDistantIndices(nums=[2, 2, 2, 2, 2], key=2, k=2)
        print(r)
        assert r == [0, 1, 2, 3, 4]

    unitTest(Solution())
