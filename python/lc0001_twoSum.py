# Given an array of integers nums and an integer target, return indices of the  
# two numbers such that they add up to target. You may assume that each input  
# would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Constraints:
#   2 <= nums.length <= 10^4
#   -10^9 <= nums[i] <= 10^9
#   -10^9 <= target <= 10^9
#   Only one valid answer exists.
from typing import List


# Dict: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, v in enumerate(nums):
            if target - v in visited:
                return [visited[target - v], i]
            visited[v] = i
            
        return []


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.twoSum([2, 7, 11, 15], 9)
        print(r)
        assert sorted(r) == [0, 1]

        r = sol.twoSum([2, 7, 11, 15, 23], 38)
        print(r)
        assert sorted(r) == [3, 4]

        r = sol.twoSum([3, 3], 6)
        print(r)
        assert sorted(r) == [0, 1]
    
    unitTest(Solution())
