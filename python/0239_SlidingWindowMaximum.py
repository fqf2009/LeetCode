# You are given an array of integers nums, there is a sliding window of
# size k which is moving from the very left of the array to the very
# right. You can only see the k numbers in the window. Each time the
# sliding window moves right by one position.
# Return the max sliding window.
# Constraints:
#   1 <= nums.length <= 10^5
#   -10^4 <= nums[i] <= 10^4
#   1 <= k <= nums.length
# Example 1:
#   Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
#   Output: [3,3,5,5,6,7]
#   Explanation:
#   Window position                Max
#   ---------------               -----
#   [1  3  -1] -3  5  3  6  7       3
#    1 [3  -1  -3] 5  3  6  7       3
#    1  3 [-1  -3  5] 3  6  7       5
#    1  3  -1 [-3  5  3] 6  7       5
#    1  3  -1  -3 [5  3  6] 7       6
#    1  3  -1  -3  5 [3  6  7]      7
from typing import List
from collections import deque
import heapq


# Deque: T/S: O(n), O(k)
# - ensure the deque window only has decreasing elements.
#   That way, the leftmost element is always the largest.
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        for i in range(len(nums)):
            while dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res


# PriorityQueue (HeapQueue)
# T/S: O(n*log(k)), O(k)
class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = [(-x, i) for i, x in enumerate(nums[:k])]
        heapq.heapify(window)
        res = []
        for i in range(len(nums) - k + 1):
            while window[0][1] < i:
                heapq.heappop(window)
            res.append(-window[0][0])
            if i + k < len(nums):
                heapq.heappush(window, (-nums[i + k], i + k))

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.maxSlidingWindow([2, 7, 8], 2)
        print(r)
        assert r == [7, 8]

        r = sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
        print(r)
        assert r == [3, 3, 5, 5, 6, 7]

        r = sol.maxSlidingWindow([1], 1)
        print(r)
        assert r == [1]

    unitTest(Solution())
