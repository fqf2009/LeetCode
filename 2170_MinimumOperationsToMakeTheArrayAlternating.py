# You are given a 0-indexed array nums consisting of n positive integers.
# The array nums is called alternating if:
#   nums[i - 2] == nums[i], where 2 <= i <= n - 1.
#   nums[i - 1] != nums[i], where 1 <= i <= n - 1.
# In one operation, you can choose an index i and change nums[i] 
# into any positive integer.

# Return the minimum number of operations required to make the array 
# alternating.

# Constraints:
#   1 <= nums.length <= 10^5
from typing import List
from collections import Counter

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        c1 = Counter(nums[::2])
        c2 = Counter(nums[1::2])
        freq1 = sorted(c1.items(), key=lambda x: -x[1])
        freq2 = sorted(c2.items(), key=lambda x: -x[1])
        res = n
        for v1, f1 in freq1[:2]:
            for v2, f2 in freq2[:2]:
                if v1 != v2:
                    res = min(res, n - f1 - f2)
                else:
                    res = min(res, n - f1, n - f2)

        return res


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.minimumOperations(nums=[3, 1, 3, 2, 4, 3])
        print(r)
        assert r == 3

        r = sol.minimumOperations(nums=[1, 2, 2, 2, 2])
        print(r)
        assert r == 2

        r = sol.minimumOperations(nums=[1])
        print(r)
        assert r == 0

        r = sol.minimumOperations(nums=[1, 1])
        print(r)
        assert r == 1

        r = sol.minimumOperations(nums=[1, 2])
        print(r)
        assert r == 0

    unitTest(Solution())
