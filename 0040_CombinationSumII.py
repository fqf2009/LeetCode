# Given a collection of candidate numbers (candidates) and a target 
# number (target), find all unique combinations in candidates where 
# the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.
# Constraints:
#   1 <= candidates.length <= 100
#   1 <= candidates[i] <= 50
#   1 <= target <= 30
from typing import List
from collections import Counter


# Backtracking, Counter
# - Combination, not permutation
# - more like template for backtracking
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        counter = Counter(candidates)
        nums = sorted(counter.keys())   # not necessary to sort, just for testing

        def backtrack(remain, start):
            if remain == 0:
                res.append(comb.copy())
                return
            if remain < 0:
                return

            for i in range(start, len(nums)):
                v = nums[i]
                if counter[v] > 0:
                    comb.append(v)
                    counter[v] -= 1
                    backtrack(remain - v, i)
                    comb.pop()
                    counter[v] += 1

        backtrack(target, 0)
        return res


# Backtracking, Counter
# - this is permutation, then use set to dedup into combination,
#   so the performance is not optimal
class Solution1:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        comb = []
        counter = Counter(candidates)

        def backtrack(remain):
            if remain == 0:
                res.add(tuple(sorted(comb)))
                return
            if remain < 0:
                return

            for v in counter.keys():
                if counter[v] > 0:
                    comb.append(v)
                    counter[v] -= 1
                    backtrack(remain - v)
                    comb.pop()
                    counter[v] += 1

        backtrack(target)
        return [list(x) for x in res]


# Backtracking, Counter
# - better performance
class Solution2:
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
class Solution3:
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
        print(sorted(r))
        assert sorted(r) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

        r = sol.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5)
        print(sorted(r))
        assert sorted(r) == [[1, 2, 2], [5]]

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
    unitTest(Solution3())
