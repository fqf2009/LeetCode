# Given an integer array nums and an integer k, return the length
# of the shortest non-empty subarray of nums with a sum of at
# least k. If there is no such subarray, return -1.
# A subarray is a contiguous part of an array.

# Constraints:
#   1 <= nums.length <= 10^5
#   -10^5 <= nums[i] <= 10^5
#   1 <= k <= 10^9
from typing import List
from collections import deque


# Deque (double-ended queue) + Sliding window: O(n)
# - P[i+1] is the prefix sum (or cumulative sum) of nums[:i+1]
# - Q = deque(), will keep index for each increasing P[i]
# - if P[i+1] is not larger than Q[-1], pop it up until it does
# - if P[i+1] - P[Q[0]] >= k, record i+1 - Q[0], (if it is the 
#   shortest length of subarray), and then pop up the Q[0].
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        P = [0] * (n+1)
        Q = deque()
        Q.append(0)
        res = n + 1
        for i in range(n):
            if nums[i] >= k: return 1
            P[i+1] += P[i] + nums[i]
            while len(Q) > 0 and P[i+1] <= P[Q[-1]]:
                Q.pop()
            while len(Q) > 0 and P[i+1] - P[Q[0]] >= k:
                res = min(res, i+1 - Q[0])
                Q.popleft()
            Q.append(i+1)

        if res > n:
            return -1
        return res


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.shortestSubarray(nums=[84, -37, 32, 40, 95], k=167)
        print(r)
        assert r == 3

        r = sol.shortestSubarray(nums=[1], k=1)
        print(r)
        assert r == 1

        r = sol.shortestSubarray(nums=[1, 2], k=4)
        print(r)
        assert r == -1

        r = sol.shortestSubarray(nums=[2, -1, 2], k=3)
        print(r)
        assert r == 3

    unit_test(Solution())
