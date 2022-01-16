# Given an integer array nums and an integer val, remove all occurrences
# of val in nums in-place. The relative order of the elements may be changed.

# Since it is impossible to change the length of the array in some languages, 
# you must instead have the result be placed in the first part of the array
# nums. More formally, if there are k elements after removing the duplicates, 
# then the first k elements of nums should hold the final result. It does not
# matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying 
# the input array in-place with O(1) extra memory.

from typing import List, Optional


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = -1
        for j in range(0, len(nums)):
            if nums[j] != val:
                i += 1
                if i < j:
                    nums[i] = nums[j]

        return i + 1


if __name__ == '__main__':
    def unitTest(sol):
        a = [0, 1, 2, 2, 3, 0, 4, 2]
        r = sol.removeElement(a, 2)
        print(r, a[:r])
        assert a[:r] == [0, 1, 3, 0, 4]

    unitTest(Solution())
