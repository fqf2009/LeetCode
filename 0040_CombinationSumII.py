# Given a collection of candidate numbers (candidates) and a target 
# number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.
from typing import List
from collections import Counter

# Recursion, Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def combSumBackward(target, pos) -> List[List[int]]:
            num, freq = candidates2[pos]
            if pos == 0:
                if target % num == 0 and target // num <= freq:
                    return [[num] * (target // num)]
                else:
                    return []

            res = []
            for i in range(freq + 1):
                if target - i*num == 0:
                    res.append([num] * i)
                elif target - i*num > 0:
                    cmb = combSumBackward(target - i*num, pos - 1)
                    for x in cmb:
                        if i > 0:
                            x.extend([num] * i)
                        res.append(x)
            return res

        candidates2 = sorted(Counter(candidates).items())
        return combSumBackward(target, len(candidates2) - 1)


# Time exceeded!
# Recursion
class Solution1:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def combSumBackward(target, pos) -> List[List[int]]:
            if pos == 0:
                if candidates[0] == target:
                    return [[candidates[0]]]
                else:
                    return []

            res = []
            cmb = combSumBackward(target, pos - 1)
            res.extend(cmb)
            if target == candidates[pos]:
                res.append([candidates[pos]])
            elif target > candidates[pos]:
                cmb = combSumBackward(target - candidates[pos], pos - 1)
                for x in cmb:
                    x.append(candidates[pos])
                    res.append(x)

            return res

        candidates.sort()
        cmb = combSumBackward(target, len(candidates) - 1)
        res = {tuple(x) for x in cmb}
        return [list(x) for x in res]


if __name__ == '__main__':
    def unitTest(sol):
        sol = Solution()

        r = sol.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8)
        print(r)
        assert sorted(r) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

        r = sol.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5)
        print(r)
        assert sorted(r) == [[1, 2, 2], [5]]

    unitTest(Solution())
    unitTest(Solution1())
