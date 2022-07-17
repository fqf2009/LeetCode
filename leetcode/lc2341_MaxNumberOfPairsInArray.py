# You are given a 0-indexed integer array nums. In one operation,
# you may do the following:
#  - Choose two integers in nums that are equal.
#  - Remove both integers from nums, forming a pair.
#  - The operation is done on nums as many times as possible.
# Return a 0-indexed integer array answer of size 2 where
#  - answer[0] is the number of pairs that are formed and
#  - answer[1] is the number of leftover integers in nums after
#    doing the operation as many times as possible.
# Constraints:
#   1 <= nums.length <= 100
#   0 <= nums[i] <= 100
from collections import Counter
from functools import reduce
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cntr = Counter(nums)
        res1, res2 = 0, 0
        for freq in cntr.values():
            res1 += freq // 2
            res2 += freq % 2
        return [res1, res2]


class Solution1:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        return reduce(lambda x, y: [x[0]+y[0], x[1]+y[1]],
                      map(lambda x: [x//2, x%2], Counter(nums).values()))

if __name__ == "__main__":

    def unit_test(sol):
        r = sol.numberOfPairs([1, 3, 2, 1, 3, 2, 2])
        print(r)
        assert r == [3, 1]

        r = sol.numberOfPairs([1, 1])
        print(r)
        assert r == [1, 0]

        r = sol.numberOfPairs([0])
        print(r)
        assert r == [0, 1]

    unit_test(Solution())
    unit_test(Solution1())
