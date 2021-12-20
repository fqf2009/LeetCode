from typing import List

# Given an array of integers nums and an integer target, return indices of the  
# two numbers such that they add up to target. You may assume that each input  
# would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            if target - nums[i] in visited:
                return [visited[target - nums[i]], i]
            visited[nums[i]] = i
        return []

if __name__ == '__main__':
    sol = Solution()

    r = sol.twoSum([2, 7, 11, 15], 9)
    print(r)
    assert(sorted(r) == [0, 1])

    r = sol.twoSum([2, 7, 11, 15, 23], 38)
    print(r)
    assert(sorted(r) == [3, 4])

    r = sol.twoSum([3, 3], 6)
    print(r)
    assert(sorted(r) == [0, 1])