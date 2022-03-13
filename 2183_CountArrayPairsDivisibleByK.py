# Given a 0-indexed integer array nums of length n and an integer k, 
# return the number of pairs (i, j) such that:
#   0 <= i < j <= n - 1 and
#   nums[i] * nums[j] is divisible by k.
# Constraints:
#   1 <= nums.length <= 10^5
#   1 <= nums[i], k <= 10^5
from collections import defaultdict
from typing import List
import math


# - T/S: O(n*sqrt(k)), O(sqrt(k)) - actually slower and consume more memory
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        div = []
        i = 1
        while i * i <= k:
            if k % i == 0:
                div.append(i)
            if i * i < k:
                div.append(k // i)
            i += 1

        res = 0
        cnt = defaultdict(int)
        for v in nums:
            res += cnt[k // math.gcd(k, v)]
            for d in div:
                if v % d == 0:
                    cnt[d] += 1
        return res


# Factorization
# - T/S: O(n*sqrt(k)), O(k)
# - Assume gcd(k, v1) is greatest common divisor of k and v1, then
#   for any value v2, if v2 % (k / gcd) == 0, it means v*v2 % k == 0
class Solution1:
    def countPairs(self, nums: List[int], k: int) -> int:
        div = []
        i = 1
        while i * i <= k:
            if k % i == 0:
                div.append(i)
            if i * i < k:
                div.append(k // i)
            i += 1

        res = 0
        cnt = [0] * (k + 1)
        for v in nums:
            res += cnt[k // math.gcd(k, v)]
            for d in div:
                if v % d == 0:
                    cnt[d] += 1

        return res


# - a little bit easier to understand??
# - but why the result is not correct??
class Solution2:
    def countPairs(self, nums: List[int], k: int) -> int:
        div = []
        i = 1
        while i * i <= k:
            if k % i == 0:
                div.append(i)
            if i * i < k:
                div.append(k // i)
            i += 1

        cnt = [0] * (k + 1)     # only use index 1..k
        for v in nums:
            for d in div:
                if v % d == 0:
                    cnt[d] += 1

        res = 0
        for v in nums:
            res += cnt[k // math.gcd(k, v)]

        return res // 2


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.countPairs(nums=[1, 2, 3, 4, 5], k=2)
        print(r)
        assert r == 7

        r = sol.countPairs(nums=[1, 2, 3, 4], k=5)
        print(r)
        assert r == 0

    unitTest(Solution())
    unitTest(Solution1())
    # unitTest(Solution2())
