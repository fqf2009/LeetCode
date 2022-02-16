# Given an array of n integers nums, a 132 pattern is a
# subsequence of three integers nums[i], nums[j] and nums[k]
# such that i < j < k and nums[i] < nums[k] < nums[j].
# Return true if there is a 132 pattern in nums, otherwise,
# return false.
# Constraints:
#   n == nums.length
#   1 <= n <= 2 * 105
#   -109 <= nums[i] <= 109
from typing import List


# Stack: O(n)
# - assume M[i] is the min value till pos i, i.e., M[i] = min[:i+1]
# - prepare a stack and then scan the nums array backwards
# - if stack is empty, or current value great or equal than the
#   item at stack top, push value into stack
# - if stack item is less than current min value, pop stack item
# - repeat until stack top item is between min and current value.
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        M = [nums[0]] * n
        for i in range(1, n):
            M[i] = min(M[i-1], nums[i])
        stk = []
        i = n - 1
        while i > 0:
            if len(stk) == 0 or nums[i] <= stk[-1]:
                stk.append(nums[i])
                i -= 1
            elif stk[-1] <= M[i]:
                stk.pop()
                continue
            else:
                return True
        
        return False


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.find132pattern([1, 2, 3, 4])
        print(r)
        assert r == False

        r = sol.find132pattern([3, 1, 4, 2])
        print(r)
        assert r == True

        r = sol.find132pattern([-1, 3, 2, 0])
        print(r)
        assert r == True

    unitTest(Solution())
