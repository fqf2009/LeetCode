# You are given a 0-indexed binary array nums of length n. nums can be divided at
# index i (where 0 <= i <= n) into two arrays (possibly empty) numsleft and numsright:

# numsleft has all the elements of nums between index 0 and i - 1 (inclusive), while
# numsright has all the elements of nums between index i and n - 1 (inclusive).
#  - If i == 0, numsleft is empty, while numsright has all the elements of nums.
# -  If i == n, numsleft has all the elements of nums, while numsright is empty.
# The division score of an index i is the sum of the number of 0's in numsleft and
# the number of 1's in numsright.

# Return all distinct indices that have the highest possible division score. You may
# return the answer in any order.
from typing import List


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zeros = 0
        ones = nums.count(1)
        res = [0]
        score = ones
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
                if zeros + ones > score:
                    score = zeros + ones
                    res = [i+1]
                elif zeros + ones == score:
                    res.append(i+1)
            else:
                ones -= 1

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.maxScoreIndices(nums=[0, 0, 1, 0])
        print(r)
        assert(r == [2, 4])

        r = sol.maxScoreIndices(nums=[0, 0, 0])
        print(r)
        assert(r == [3])

        r = sol.maxScoreIndices(nums=[1, 1])
        print(r)
        assert(r == [0])

    unitTest(Solution())
