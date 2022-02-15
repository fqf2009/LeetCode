# Given two integers n and k, return all possible combinations
# of k numbers out of the range [1, n].
# You may return the answer in any order.
# Constraints:
#   1 <= n <= 20
#   1 <= k <= n
from typing import List
from itertools import combinations


# Backtracking
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        cmb = [0] * k           # initial state for all positions
        i = 0                   # next position of backtracking
        while i >= 0:           # exit condition
            if cmb[i] == 0:     # next state for this pos
                cmb[i] = cmb[i-1] + 1
            else:
                cmb[i] += 1

            if cmb[i] > n:      # all possible states is exhaused for this pos
                cmb[i] = 0      # reset state for this pos
                i -= 1          # back track one pos
                continue

            if i == k - 1:      # all positions are in good state
                res.append(cmb.copy())  # must copy, list is ref
                continue

            i += 1              # forward to next pos

        return res


# using Python supplied library
class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [list(x) for x in combinations(range(1, n+1), k)]


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.combine(4, 2)
        print(r)
        assert sorted(r) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

        r = sol.combine(1, 1)
        print(r)
        assert r == [[1]]

    unit_test(Solution())
    unit_test(Solution1())
