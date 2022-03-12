# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
# Constraints:
#   1 <= nums.length <= 6
#   -10 <= nums[i] <= 10
#   All the integers of nums are unique.
from typing import List
from itertools import permutations


# Backtracking + Recursion
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        usedIdx = set()
        perm = []
        def backtrack(pos: int):
            if pos == n:
                res.append(perm.copy())
                return
            for i, v in enumerate(nums):
                if i not in usedIdx:
                    usedIdx.add(i)
                    perm.append(v)
                    backtrack(pos + 1)
                    perm.pop()
                    usedIdx.remove(i)
        
        backtrack(0)
        return res


# Backtracking + Iteration
class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        cmb = [-1] * n          # initial state for all positions
        i = 0                   # next position of backtracking
        while i >= 0:           # exit condition
            cmb[i] += 1         # next state for this pos
            # if the number is already used, skip
            # note if using regular for loop here, continue is not enough
            # to go out to back to while-i-loop, need to add flag
            if any(cmb[j] == cmb[i] for j in range(0, i)):
                continue

            if cmb[i] >= n:     # all possible states is exhaused for this pos
                cmb[i] = -1     # reset state for this pos
                i -= 1          # back track one pos
                continue

            if i == n - 1:      # all positions are in good state
                res.append([nums[j] for j in cmb])
                continue

            i += 1              # forward to next pos

        return res


# using Python supplied library
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(x) for x in permutations(nums)]


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.permute([1, 2, 3])
        print(r)
        assert sorted(r) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

        r = sol.permute([0, 1])
        print(r)
        assert sorted(r) == [[0, 1], [1, 0]]

        r = sol.permute([1])
        print(r)
        assert sorted(r) == [[1]]

    unit_test(Solution())
    unit_test(Solution1())
    unit_test(Solution2())
