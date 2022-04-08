from typing import List

# DP
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prevMax = nums[0]
        prevMin = nums[0]
        mp = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            currMax = max(n, prevMax * n, prevMin * n)
            currMin = min(n, prevMax * n, prevMin * n)
            prevMax, prevMin = currMax, currMin
            mp = max(mp, currMax)

        return mp


class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        dpMax = [0] * len(nums)
        dpMin = [0] * len(nums)
        dpMax[0] = nums[0]
        dpMin[0] = nums[0]
        mp = nums[0]
        for i in range(1, len(nums)):
            dpMax[i] = max(nums[i], dpMax[i-1] * nums[i], dpMin[i-1] * nums[i])
            dpMin[i] = min(nums[i], dpMax[i-1] * nums[i], dpMin[i-1] * nums[i])
            mp = max(mp, dpMax[i])

        return mp


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.maxProduct([5, -3, 0, 2, -2, -3, 5, 2, -3])
        print(r)
        assert r == 120

        r = sol.maxProduct([5, -3, 0, 2, -2, -3, 5, 2, -3, 2])
        print(r)
        assert r == 180

        r = sol.maxProduct([5, -3, 0, 2, -2, -3, 5, 2, -3, -2])
        print(r)
        assert r == 720

        r = sol.maxProduct([2,3,-2,4])
        print(r)
        assert r == 6

        r = sol.maxProduct([-2,0,-1])
        print(r)
        assert r == 0

    unitTest(Solution())
