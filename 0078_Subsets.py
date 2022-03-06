# Given an integer array nums of unique elements, return all
# possible subsets (the power set).
# The solution set must not contain duplicate subsets.
# Return the solution in any order.
# Constraints:
#   1 <= nums.length <= 10
#   -10 <= nums[i] <= 10
#   All the numbers of nums are unique.
from typing import List
from itertools import chain, combinations


# Powerset, Combination
class Solution:
    # itertools functions return iterators, which are objects
    # that produce results lazily, on demand.
    def powerset(self, iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [list(x) for x in self.powerset(nums)]


# Backtracking
class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = set()
        i = 0
        pos = [0] * len(nums)
        while i >= 0:
            if pos[i] == 0:
                pos[i] += 1
                i += 1
            elif pos[i] == 1:
                pos[i] += 1
                subset.add(nums[i])
                i += 1
            else:  # pos[i] > 1
                subset.remove(nums[i])
                pos[i] = 0
                i -= 1
            if i == len(nums):
                res.append(sorted(list(subset)))
                i -= 1

        return res


# Recursion
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0: return [nums]
        ss = self.subsets(nums[:-1])
        return ss + [x + [nums[-1]] for x in ss]


# Iteration
class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(2**n):
            ss = []
            for j in range(n):
                if i & (1 << j):
                    ss.append(nums[j])
            res.append(ss)

        return res  


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.subsets(nums=[1, 2, 3])
        r.sort()
        print(r)
        assert(r == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])

        r = sol.subsets(nums=[0])
        print(r)
        r.sort()
        assert(r == [[], [0]])

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
    unitTest(Solution3())
