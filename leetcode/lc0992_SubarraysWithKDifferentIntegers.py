# Given an integer array nums and an integer k, return
# the number of good subarrays of nums.
# A good array is an array where the number of different
# integers in that array is exactly k.
# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.
# Constraints:
#   1 <= nums.length <= 2 * 10^4
#   1 <= nums[i], k <= nums.length
from typing import Counter, List


# Sliding window: T/S: O(n), O(1)
# - refer to: 0340_LongestSubstringWithAtMostKDistinctCharacters
# - exactly(K) = atMost(K) - atMost(K-1)
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostKDistinct(k: int) -> int:
            if k == 0: return 0
            cntr = Counter()
            j, nDistinct, res = 0, 0, 0
            for i, v in enumerate(nums):
                if cntr[v] == 0:
                    nDistinct += 1
                cntr[v] += 1
                while nDistinct > k:
                    cntr[nums[j]] -= 1
                    if cntr[nums[j]] == 0:
                        nDistinct -= 1
                    j += 1
                res += i - j + 1

            return res

        return atMostKDistinct(k) - atMostKDistinct(k-1)


# Worse case: O(n*k)
# TLE (Time Limit Exceeded) - when k is very big, like 1000
class Solution1:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostKDistinct(k: int) -> int:
            if k == 0: return 0
            seen = {}
            left, res = -1, 0
            for i, v in enumerate(nums):
                seen[v] = i
                if len(seen) > k:
                    left, v1 = min((j, v) for v, j in seen.items())
                    del seen[v1]
                res += i - left
            return res

        return atMostKDistinct(k) - atMostKDistinct(k-1)


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.subarraysWithKDistinct([1, 2, 1, 2, 3], k=2)
        print(r)
        assert r == 7

        r = sol.subarraysWithKDistinct([1, 2, 1, 3, 4], k=3)
        print(r)
        assert r == 3

        r = sol.subarraysWithKDistinct([1, 2, 1, 3, 4], k=1)
        print(r)
        assert r == 5

        r = sol.subarraysWithKDistinct(list(range(2*10**4)), k=1000)
        print(r)
        assert r == 19001

    unitTest(Solution())
    unitTest(Solution1())
