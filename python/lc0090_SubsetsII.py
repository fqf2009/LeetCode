# Given an integer array nums that may contain duplicates, return
# all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the
# solution in any order.
# Constraints:
#   1 <= nums.length <= 10
#   -10 <= nums[i] <= 10
from typing import List


# Recursion
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return [[]]
        ss = self.subsetsWithDup(nums[:-1])
        # sorted() is important for deduplication
        res = set(tuple(sorted(y)) for y in (ss + [x + [nums[-1]] for x in ss]))
        return [list(x) for x in res]


# Iteration
class Solution1:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        for i in range(2**n):
            ss = []
            for j in range(n):
                if i & (1 << j):
                    ss.append(nums[j])
            res.add(tuple(sorted(ss)))

        return [list(x) for x in res]


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.subsetsWithDup(nums=[1, 2, 2])
        r.sort()
        print(r)
        assert r == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

        r = sol.subsetsWithDup(nums=[0])
        r.sort()
        print(r)
        assert r == [[], [0]]

        r = sol.subsetsWithDup(nums=[4, 4, 4, 1, 4])
        r.sort()
        print(r)
        assert r == [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], 
                     [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]

    unitTest(Solution())
    unitTest(Solution1())
