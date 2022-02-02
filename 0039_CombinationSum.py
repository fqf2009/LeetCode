# Given an array of distinct integers candidates and a target integer
# target, return a list of all unique combinations of candidates where
# the chosen numbers sum to target. You may return the combinations in
# any order.

# The same number may be chosen from candidates an unlimited number of
# times. Two combinations are unique if the frequency of at least one
# of the chosen numbers is different.

# It is guaranteed that the number of unique combinations that sum up
# to target is less than 150 combinations for the given input.
from typing import List


# Recursion
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combSumBackward(target, pos) -> List[List[int]]:
            if pos == 0:
                if target % candidates[pos] == 0:
                    return [[candidates[pos]] * (target // candidates[pos])]
                else:
                    return []

            res = []
            for i in range(target // candidates[pos] + 1):
                if target - i*candidates[pos] == 0:
                    res.append([candidates[pos]] * i)
                else:
                    cmb = combSumBackward(target - i*candidates[pos], pos - 1)
                    for x in cmb:
                        if i > 0:
                            x.extend([candidates[pos]] * i)
                        res.append(x)
            return res

        candidates.sort()
        return combSumBackward(target, len(candidates) - 1)


if __name__ == '__main__':
    def unitTest(sol):
        sol = Solution()

        r = sol.combinationSum(candidates=[1, 2], target=4)
        print(r)
        assert r == [[1, 1, 1, 1], [1, 1, 2], [2, 2]]

        r = sol.combinationSum(candidates=[2, 3, 6, 7], target=7)
        print(r)
        assert r == [[2, 2, 3], [7]]

        r = sol.combinationSum(candidates=[2, 3, 5], target=8)
        print(r)
        assert r == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    unitTest(Solution())
