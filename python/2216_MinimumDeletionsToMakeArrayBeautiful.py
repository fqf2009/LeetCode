# You are given a 0-indexed integer array nums. The array nums is beautiful if:
# - nums.length is even.
# - nums[i] != nums[i + 1] for all i % 2 == 0.
# Note that an empty array is considered beautiful.
# You can delete any number of elements from nums. When you delete an element, 
# all the elements to the right of the deleted element will be shifted one unit 
# to the left to fill the gap created and all the elements to the left of the 
# deleted element will remain unchanged.
# Return the minimum number of elements to delete from nums to make it beautiful.
# Constraints:
#   1 <= nums.length <= 10^5
#   0 <= nums[i] <= 10^5
from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        res = 0
        i, n = 0, len(nums)
        while i < n:
            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1
                res += 1
            if j == n:
                return res + 1  # length cannot be odd, so plus one
            i = j + 1   # nums[j] == nums[i], so i move forward to next pair

        return res
        

if __name__ == '__main__':
    def unitTest(sol):
        r = sol.minDeletion(nums = [1,1,2,3,5])
        print(r)
        assert r == 1

        r = sol.minDeletion( nums = [1,1,2,2,3,3])
        print(r)
        assert r == 2

    unitTest(Solution())
