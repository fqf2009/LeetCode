# You are given two positive integer arrays nums and numsDivide. You can delete
# any number of elements from nums.
# Return the minimum number of deletions such that the smallest element in
# nums divides all the elements of numsDivide. If this is not possible, return -1.
# Note that an integer x divides y if y % x == 0.
# Constraints:
#   1 <= nums.length, numsDivide.length <= 10^5
#   1 <= nums[i], numsDivide[i] <= 10^9
from functools import reduce
from typing import List
from math import gcd


# Math - T/S: O(m + n + n*(log(n))), n = len(nums), m = len(numsDivide)
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g = numsDivide[0]
        for v in numsDivide[1:]:
            g = gcd(g, v)
            if g == 1:
                break

        res = 0
        noWay = True
        for v in sorted(nums):
            if g % v == 0:
                noWay = False
                break
            if v > g:
                break
            res += 1

        return -1 if noWay else res


# Oneliner: O(m + n + n*(log(n)))
class Solution1:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g = gcd(*numsDivide)  # since Python 3.9: math.gcd(*integers)
        return next((i for i, v in enumerate(sorted(nums)) if g % v == 0), -1)


# O(log(m) + n + n*(log(n)))
# Merge every 2 items when doing gcd:
# - T/S: O(log(m)), O(m), use space for performance
class Solution2:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        D = numsDivide.copy()
        while len(D) > 1:
            D1 = [gcd(D[i * 2], D[i * 2 + 1]) for i in range(len(D) // 2)]
            if len(D) % 2 != 0:
                D1.append(D[-1])
            D = D1

        g = D[0]
        for i, v in enumerate(sorted(nums)):
            if g % v == 0:
                return i
            if v > g:
                break

        return -1


# O(m + n)
class Solution3:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g = gcd(*numsDivide)
        smallest = min((v for v in nums if g % v == 0), default=0)
        return -1 if smallest == 0 else sum(int(v < smallest) for v in nums)


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.minOperations([2, 3, 2, 4, 3], numsDivide=[9, 6, 9, 3, 15])
        print(r)
        assert r == 2

        r = sol.minOperations([4, 3, 6], numsDivide=[8, 2, 6, 10])
        print(r)
        assert r == -1

    unit_test(Solution())
    unit_test(Solution1())
    unit_test(Solution2())
    unit_test(Solution3())
