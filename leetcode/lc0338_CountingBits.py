# Given an integer n, return an array ans of length n + 1 such that for
# each i (0 <= i <= n), ans[i] is the number of 1's in the binary
# representation of i.
# Constraints:
#   0 <= n <= 10^5
# Follow up:
#   It is very easy to come up with a solution with a runtime
#   of O(n log n). Can you do it in linear time O(n) and possibly
#   in a single pass?
#   Can you do it without using any built-in function (i.e.,
#   like __builtin_popcount in C++)?
from typing import List


# O(n*log(n))
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        stack = []
        for _ in range(n):
            j = 0
            while stack and stack[-1] == j:
                stack.pop()
                j += 1
            stack.append(j)
            res.append(len(stack))

        return res


# O(n)
# - right shift and check least siganificant bit
# - bits(0x1101) = bits(0x110) + (0x1101 & 0x1)
class Solution1:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)

        return res


# O(n)
# - Note: i & (i-1) means clear one bit each time,
#         i has one more bit than i & (i-1).
class Solution2:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i & (i - 1)] + 1

        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.countBits(2)
        print(r)
        assert r == [0, 1, 1]

        r = sol.countBits(5)
        print(r)
        assert r == [0, 1, 1, 2, 1, 2]

    unit_test(Solution())
    unit_test(Solution1())
    unit_test(Solution2())
