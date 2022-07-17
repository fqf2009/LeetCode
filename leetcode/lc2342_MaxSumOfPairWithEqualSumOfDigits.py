# You are given a 0-indexed array nums consisting of positive integers.
# You can choose two indices i and j, such that i != j, and the sum of
# digits of the number nums[i] is equal to that of nums[j].
# Return the maximum value of nums[i] + nums[j] that you can obtain over
# all possible indices i and j that satisfy the conditions.
# Constraints:
#   1 <= nums.length <= 10^5
#   1 <= nums[i] <= 10^9
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res = -1
        dsMap = {}
        for v in nums:
            ds = sum(int(x) for x in str(v))
            if ds in dsMap:
                v0 = dsMap[ds]
                res = max(res, v0 + v)
                dsMap[ds] = max(v0, v)
            else:
                dsMap[ds] = v
        return res


class Solution1:
    def maximumSum(self, nums: List[int]) -> int:
        res = -1
        dsMap = {}
        for v in nums:
            ds, v1 = 0, v
            while v1 > 0:
                ds += v1 % 10
                v1 //= 10
            if ds in dsMap:
                v0 = dsMap[ds]
                res = max(res, v0 + v)
                dsMap[ds] = max(v0, v)
            else:
                dsMap[ds] = v
        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.maximumSum([18, 43, 36, 13, 7])
        print(r)
        assert r == 54

        r = sol.maximumSum([10, 12, 19, 14])
        print(r)
        assert r == -1

    unit_test(Solution())
    unit_test(Solution1())
