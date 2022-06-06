# Given an integer n, return any array containing n unique integers
# such that they add up to 0.
# Constraints:
#   1 <= n <= 1000
from typing import List


# Pattern
# 0
# -1, 1
# -1, 0, 1
# -2, -1, 1, 2
# -2, -1, 0, 1, 2
class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [i for i in range(-(n // 2), n // 2 + 1) if i != 0 or n % 2 == 1]


# Pattern
# 0
# -1, 1
# -2, 0, 2
# -3, -1, 1, 3
# -4, -2, 0, 2, 4
class Solution1:
    def sumZero(self, n: int) -> List[int]:
        return list(range(-n + 1, n, 2))


if __name__ == "__main__":

    def unitTest(sol):
        for i in range(6):
            r = sol.sumZero(i)
            print(r)
            assert sum(r) == 0

    unitTest(Solution())
    unitTest(Solution1())
