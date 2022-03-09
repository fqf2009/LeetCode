# Given a collection of numbers, nums, that might contain duplicates,
# return all possible unique permutations in any order.
# Constraints:
#   1 <= nums.length <= 8
#   -10 <= nums[i] <= 10
from typing import List
from itertools import permutations
from collections import Counter


# Backtracking + Recursion: O(n^n)
# - use Counter to avoid duplicates, instead of using set to deduplicate
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        counter = Counter(nums)
        comb = []
        res = []

        def backtrack():
            if len(comb) == n:
                res.append(comb.copy())     # must copy!!!
                return
            for v in counter:
                if counter[v] > 0:
                    comb.append(v)
                    counter[v] -= 1
                    backtrack()
                    comb.pop()
                    counter[v] += 1

        backtrack()
        return res


# Backtracking + Recursion: O(n^n)
class Solution1:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        usedIdx = set()
        comb = []
        res = set()
        def backtrack():
            if len(comb) == n:
                res.add(tuple(comb))
                return
            for i, v in enumerate(nums):
                if i not in usedIdx:
                    comb.append(v)
                    usedIdx.add(i)
                    backtrack()
                    usedIdx.remove(i)
                    comb.pop()

        backtrack()
        return [list(x) for x in res]


# Using Python library: O(n^n)
class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return [list(x) for x in set(permutations(nums, len(nums)))]


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.permuteUnique([1, 1, 2])
        print(r)
        assert sorted(r) == [[1, 1, 2],
                             [1, 2, 1],
                             [2, 1, 1]]

        r = sol.permuteUnique([1, 2, 3])
        print(r)
        assert sorted(r) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
