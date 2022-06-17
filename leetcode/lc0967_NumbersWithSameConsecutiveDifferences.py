# Return all non-negative integers of length n such that the
# absolute difference between every two consecutive digits is k.
# Note that every number in the answer must not have leading
# zeros. For example, 01 has one leading zero and is invalid.
# You may return the answer in any order.
# Constraints:
#   2 <= n <= 9
#   0 <= k <= 9
from typing import List


# - Time: O(9*2^(n-1)), when k = 1
#   if k is bigger, maybe less than O(9*1^(n-1)), i.e. < O(9)
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        digits = [0] * n

        def backtrack(pos):
            if pos == n:
                res.append(int("".join(str(x) for x in digits)))
                return
            if pos == 0:
                for i in range(1, 10):
                    digits[pos] = i
                    backtrack(pos + 1)
            else:
                for v in set([digits[pos-1] - k, digits[pos-1] + k]):
                    if 0 <= v <= 9:
                        digits[pos] = v
                        backtrack(pos + 1)

        backtrack(0)
        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.numsSameConsecDiff(n=3, k=7)
        print(r)
        assert r == [181, 292, 707, 818, 929]

        r = sol.numsSameConsecDiff(n = 2, k = 1)
        print(r)
        assert sorted(r) == sorted([10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98])

    unit_test(Solution())
