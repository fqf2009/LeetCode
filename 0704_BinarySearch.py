# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            k = (i + j) // 2
            if nums[k] == target:
                return k
            elif nums[k] < target:
                i = k + 1
            else:
                j = k - 1

        return -1
        

if __name__ == '__main__':
    def unitTest(sol):
        r = sol.search(nums = [-1,0,3,5,9,12], target = 9)
        print(r)
        assert r == 4

        r = sol.search([-1,0,3,5,9,12], target = 2)
        print(r)
        assert r == -1

    unitTest(Solution())
