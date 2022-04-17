# Given a 1-indexed array of integers numbers that is already
# sorted in non-decreasing order, find two numbers such that
# they add up to a specific target number. Let these two numbers
# be numbers[index1] and numbers[index2]
# where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by
# one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution.
# You may not use the same element twice.

# Your solution must use only constant extra space.
from typing import List

# Two pointers: O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            total = numbers[i] + numbers[j]
            if total == target:
                return [i + 1, j + 1]
            elif total < target:
                i += 1
            else:
                j -= 1
                
        return [-1, -1]


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.twoSum(numbers=[5,25,75], target=100)
        print(r)
        assert r == [2, 3]

        r = sol.twoSum(numbers=[5,25,75], target=200)
        print(r)
        assert r == [-1, -1]

        r = sol.twoSum(numbers=[2, 7, 11, 15], target=9)
        print(r)
        assert r == [1, 2]

        r = sol.twoSum(numbers=[2, 3, 4], target=6)
        print(r)
        assert r == [1, 3]

        r = sol.twoSum(numbers=[-1, 0], target=-1)
        print(r)
        assert r == [1, 2]

    unitTest(Solution())
