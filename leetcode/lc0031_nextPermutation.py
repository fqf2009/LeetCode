# Implement next permutation, which rearranges numbers into the lexicographically 
# next greater permutation of numbers.
# If such an arrangement is impossible, it must rearrange it to the lowest possible 
# order (i.e., sorted in ascending order).
# The replacement must be in place and use only constant extra memory.
# Constraints:
#   1 <= nums.length <= 100
#   0 <= nums[i] <= 100
from typing import List


# Analysis:
#  - what does this next permutation mean? greater in one-by-one field comparison.
#  - e.g., [3,2,1] (Ever Decreasing Series) has no next permutation, only to 
#          reverse to minimum permutation [1,2,3]
#  - e.g., [8,9,6,10,7,2], the [10,7,2] portion has no next greater permutation. So
#          find the 6 (pivot) where EDS stops, then find the minimum number in EDS but 
#          than 6, it is 7. Now swap 6 and 7, we get [8,9,7,10,6,2], which is greater
#          greater than original permutation, and the last portion [10,6,2] is still EDS.
#          if we reverse this EDS, we get [2,6,10], this is the minimum for this portion.
#          So, we get the next permutation [8,9,7,2,6,10].
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        p = 0   # pos to reverse array
        for i in reversed(range(n-1)):
            if nums[i] < nums[i + 1]:   # i is pivot pos
                k = n - 1
                for j in reversed(range(i+1, n)):
                    if nums[j] > nums[i]:
                        k = j           # k is swap pos
                        break
                nums[i], nums[k] = nums[k], nums[i]
                p = i + 1
                break

        # reverse
        for i in range(p, p + (n - p) // 2):
            nums[i], nums[-1 - (i-p)] = nums[-1 - (i-p)], nums[i]


if __name__ == "__main__":
    def unitTest(sol):
        nums = [1,3,2]
        sol.nextPermutation(nums)
        print(nums)
        assert(nums == [2,1,3])

        nums = [8,9,6,10,7,2]
        print(nums)
        sol.nextPermutation(nums)
        assert(nums == [8,9,7,2,6,10])

        nums = [1,2,3]
        print(nums)
        sol.nextPermutation(nums)
        assert(nums == [1,3,2])

        nums = [3,2,1]
        print(nums)
        sol.nextPermutation(nums)
        assert(nums == [1,2,3])

        nums = [1,1,5]
        print(nums)
        sol.nextPermutation(nums)
        assert(nums == [1,5,1])

        nums = [1]
        print(nums)
        sol.nextPermutation(nums)
        assert(nums == [1])

    unitTest(Solution())
