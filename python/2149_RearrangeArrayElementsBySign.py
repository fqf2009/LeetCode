# You are given a 0-indexed integer array nums of even length consisting of an 
# equal number of positive and negative integers.
# You should rearrange the elements of nums such that the modified array follows 
# the given conditions:
#  - Every consecutive pair of integers have opposite signs.
#  - For all integers with the same sign, the order in which they were present in nums is preserved.
#  - The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
from typing import List


# Two Pointers
# Time complexity: O(n), space complexity: O(n)
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pp, pn = 0, 1   # current pos of postive and negative number in res
        for v in nums:
            if v > 0:
                res[pp] = v
                pp += 2
            else:
                res[pn] = v
                pn += 2

        return res


# Time complexity: O(n), space complexity: O(n)
class Solution1:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        for i in range(len(nums) // 2):
            nums[i * 2] = pos[i]
            nums[i * 2 + 1] = neg[i]
            
        return nums

if __name__ == '__main__':
    def unitTest(sol):
        r = sol.rearrangeArray(nums = [3,1,-2,-5,2,-4])
        print(r)
        assert(r == [3,-2,1,-5,2,-4])

        r = sol.rearrangeArray(nums = [-1,1])
        print(r)
        assert(r == [1,-1])

    unitTest(Solution())
    unitTest(Solution1())
