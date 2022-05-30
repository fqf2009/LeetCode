# You are given a 0-indexed integer array nums. In one step, remove 
# all elements nums[i] where nums[i - 1] > nums[i] for 
# all 0 < i < nums.length.
# Return the number of steps performed until nums becomes a 
# non-decreasing array.
# Example 1:
#   Input: nums = [5,3,4,4,7,3,6,11,8,5,11]
#   Output: 3
#   Explanation: The following are the steps performed:
#   - Step 1: [5,3,4,4,7,3,6,11,8,5,11] becomes [5,4,4,7,6,11,11]
#   - Step 2: [5,4,4,7,6,11,11] becomes [5,4,7,11,11]
#   - Step 3: [5,4,7,11,11] becomes [5,7,11,11]
#   [5,7,11,11] is a non-decreasing array. Therefore, we return 3.
# Constraints:
#   1 <= nums.length <= 10^5
#   1 <= nums[i] <= 10^9
from typing import List


# Stack + DP - T/S: O(n), O(n)
# - reference: https://leetcode.com/problems/steps-to-make-array-non-decreasing/discuss/2085864/C%2B%2BPython-Stack-%2B-DP-%2B-Explanation
# Analysis:
# - Note the problem is not about how many items to remove, it is about steps!
# - The point is to check each item in reversed order!
# - dp[i] means the number of element nums[i] can eat, i.e., to eat
#   those items (in ascending/non-decreasing order) in stack
# - if stack is empty, add item to stack
# - if item > stack_top_item, pop it and calculate dp[i]:
#   - dp[i] increase by one each time, but if stack_top_item's dp is larger,
#     use that one. i.e.,
#   - two nodes i, j both are eating small items after them, when item i is
#     to eat item j, max(dp[i] + 1, dp[j]) means if item j take more steps
#     to eat remaining items, use dp[j] instead of (dp[i]+1). Note (dp[i]+1)
#     already includes steps of item i eating item j. In reality, item i will
#     eat item j first, before item j could finish all its task.
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        res = 0
        stack = []
        for i in reversed(range(len(nums))):
            while stack and nums[i] > nums[stack[-1]]:
                dp[i] = max(dp[i] + 1, dp[stack.pop()])
                res = max(res, dp[i])        
            stack.append(i)

        return res


# Stack + DP
# - Works too even without reversed scanning
# - Periodic monotonic decreasing stack to save (val, steps)
# - first item in stack (val_0, 0)
# - scan through items:
#   - if new item is less than stack_top_item, push (val_i, 1)
#   - continuous decreasing items, all push with (val_i, 1),
#     meaning they can all be removed in 1 steps.
#   - if new item is great or equal max_val, push with (val_i, 0)
#   - if new item is greater or equal than stack_top_item, and
#     less than max_val, pop stack and get stack_top_steps + 1,
#     continue doing this, to make sure stack is monotonic
#     decreasing since item of max_val.
class Solution1:
    def totalSteps(self, nums: List[int]) -> int:
        res, max_val = 0, 0
        stack = []  # (val, steps)
        for v in nums:
            steps = 1 if stack and v < stack[-1][0] else 0
            while stack and stack[-1][0] <= v < max_val:
                steps = max(steps, stack.pop()[1] + 1)
            stack.append([v, steps])
            res = max(res, steps)
            max_val = max(v, max_val)

        return res


# ***** More Stack Problems *****
# Sum of Total Strength of Wizards
# Car Fleet II
# Find the Most Competitive Subsequence
# Minimum Number of Removals to Make Mountain Array
# Final Prices With a Special Discount in a Shop
# Constrained Subsequence Sum
# Minimum Cost Tree From Leaf Values
# Sum of Subarray Minimums
# Online Stock Span
# Score of Parentheses
# Next Greater Element II
# Next Greater Element I
# Largest Rectangle in Histogram
# Trapping Rain Water


if __name__ == "__main__":

    def unit_test(solution):
        print(solution.__name__)
        sol = solution()

        r = sol.totalSteps([1682,63,124,147,897,1210,1585,1744,1764,1945,323,984,
                            1886,346,481,1059,1388,1483,1516,1842,1868,1877,504,
                            1197,785,955,970,1848,1851,398,907,995,1167,1214,1423,
                            1452,1464,1474,1311,1427,1757,1992,57,1625,1260,700,725])
        print(r)
        assert r == 10
        
        r = sol.totalSteps([9, 6, 14, 15, 15, 7, 2, 6, 15, 13])
        print(r)
        assert r == 2

        r = sol.totalSteps([12, 8, 14, 9])
        print(r)
        assert r == 1

        r = sol.totalSteps([5, 14, 15, 2, 11, 5, 13, 15])
        print(r)
        assert r == 3

        r = sol.totalSteps([10, 1, 2, 3, 4, 5, 6, 1, 2, 3])
        print(r)
        assert r == 6

        r = sol.totalSteps([5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11])
        print(r)
        assert r == 3

        r = sol.totalSteps([4, 5, 7, 7, 13])
        print(r)
        assert r == 0

    unit_test(Solution)
    unit_test(Solution1)
