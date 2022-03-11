# An integer array is called arithmetic if it consists of at least three 
# elements and if the difference between any two consecutive elements is the same.
#  - For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
# Given an integer array nums, return the number of arithmetic subarrays of nums.
# A subarray is a contiguous subsequence of the array.
# Example 1:
#   Input: nums = [1,2,3,4]
#   Output: 3
#   Explanation: 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
# Constraints:
#   1 <= nums.length <= 5000
#   -1000 <= nums[i] <= 1000
from typing import List


# DP: T/S: O(n), O(1)
# - assume dp[i] is number of arithmetic slices with ending pos i
# - if nums[i] - nums[i-1] == nums[i-1] - nums[i-2], then
#       dp[i] = dp[i] + 1
# - e.g. [1, 2, 3]  =>  [1, 2, 3, 4]  =>  [1, 2, 3, 4, 5]
#        dp[2] = 1  =>  dp[3] = 2     =>  dp[4] = 3
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = res = 0
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp += 1
                res += dp
            else:
                dp = 0

        return res


# T/S: O(n), O(1)
# - to simplify, no need to save left pointer, just save the count
class Solution1:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        count = 0
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                count += 1
            else:
                res += count * (count+1) // 2
                count = 0

        res += count * (count+1) // 2
        return res


# Two pointers: T/S: O(n), O(1)
class Solution2:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return 0
        diff = nums[1] - nums[0]
        left = 0
        right = 2
        res = 0
        while right < n:
            if nums[right] - nums[right-1] != diff:
                if right - left >= 3:
                    k = right - left - 3 + 1
                    res += k * (k+1) // 2
                left = right - 1
                diff = nums[right] - nums[right-1]
            right += 1

        if right - left >= 3:
            k = right - left - 3 + 1
            res += k * (k+1) // 2

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.numberOfArithmeticSlices([1,2,3,4])
        print(r)
        assert r == 3

        r = sol.numberOfArithmeticSlices([1])
        print(r)
        assert r == 0

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
