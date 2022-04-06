# Given an integer array nums which is sorted in ascending order and all 
# of its elements are unique and given also an integer k, return the kth 
# missing number starting from the leftmost number of the array.
# Constraints:
#   1 <= nums.length <= 5 * 10^4
#   1 <= nums[i] <= 10^7
#   nums is sorted in ascending order, and all the elements are unique.
#   1 <= k <= 10^8
from typing import List


# Array
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n_missing = k
        prev = nums[0]
        for val in nums:
            gap = val - prev - 1
            if gap > 0:
                if n_missing <= gap:
                    return prev + n_missing
                else:
                    n_missing -= gap
            prev = val

        return prev + n_missing


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.missingElement([4,7,9,10], k = 1)
        print(r)
        assert r == 5

        r = sol.missingElement([4,7,9,10], k = 3)
        print(r)
        # assert r == 8

        r = sol.missingElement([1,2,4], k = 3)
        print(r)
        assert r == 6

    unit_test(Solution())
