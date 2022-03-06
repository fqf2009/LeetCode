# You are given an array of integers nums. Perform the following steps:
#  - Find any two adjacent numbers in nums that are non-coprime.
#  - If no such numbers are found, stop the process.
#  - Otherwise, delete the two numbers and replace them with their LCM
#    (Least Common Multiple).
#  - Repeat this process as long as you keep finding two adjacent non-coprime
#    numbers.
# Return the final modified array. It can be shown that replacing adjacent
# non-coprime numbers in any arbitrary order will lead to the same result.
# The test cases are generated such that the values in the final array are 
# less than or equal to 10^8.
# Two values x and y are non-coprime if GCD(x, y) > 1 where GCD(x, y) is
# the Greatest Common Divisor of x and y.
# Constraints:
#   1 <= nums.length <= 105
#   1 <= nums[i] <= 105
#   The test cases are generated such that the values in the final array are 
#   less than or equal to 108.
from typing import List
import math


# Math + Stack
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stk = []
        for v in nums:
            while stk:
                g = math.gcd(stk[-1], v)
                if g == 1: break
                v = stk.pop() * v // g
            stk.append(v)

        return stk


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.replaceNonCoprimes(nums=[6, 4, 3, 2, 7, 6, 2])
        print(r)
        assert r == [12, 7, 6]

        r = sol.replaceNonCoprimes([2, 2, 1, 1, 3, 3, 3])
        print(r)
        assert r == [2, 1, 1, 3]

    unitTest(Solution())
