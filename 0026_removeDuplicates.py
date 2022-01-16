# Given an integer array nums sorted in non-decreasing order, remove the
# duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, 
# you must instead have the result be placed in the first part of the array
# nums. More formally, if there are k elements after removing the duplicates, 
# then the first k elements of nums should hold the final result. It does not 
# matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying 
# the input array in-place with O(1) extra memory.

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                if i < j:
                    nums[i] = nums[j]
                    
        return i + 1

if __name__ == '__main__':
    def unitTest(sol):
        a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        r = sol.removeDuplicates(a)
        print(r, a[:r])
        assert a[:r] == [0, 1, 2, 3, 4]

    unitTest(Solution())
