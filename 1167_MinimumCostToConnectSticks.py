# You have some number of sticks with positive integer lengths. These lengths
# are given as an array sticks, where sticks[i] is the length of the ith stick.
# You can connect any two sticks of lengths x and y into one stick by paying a cost
# of x + y. You must connect all the sticks until there is only one stick remaining.
# Return the minimum cost of connecting all the given sticks into one stick in this way.
# Example 1:
# Input: sticks = [2,4,3]
# Output: 14
# Explanation: You start with sticks = [2,4,3].
#   1. Combine sticks 2 and 3 for a cost of 2 + 3 = 5. Now you have sticks = [5,4].
#   2. Combine sticks 5 and 4 for a cost of 5 + 4 = 9. Now you have sticks = [9].
#   3. There is only one stick left, so you are done. The total cost is 5 + 9 = 14.
# Constraints:
#   1 <= sticks.length <= 10^4
#   1 <= sticks[i] <= 10^4
import heapq
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        res = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            v = heapq.heappop(sticks) + heapq.heappop(sticks)
            heapq.heappush(sticks, v)
            res += v

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.connectSticks([2, 4, 3])
        print(r)
        assert r == 14

        r = sol.connectSticks([1, 8, 3, 5])
        print(r)
        assert r == 30

        r = sol.connectSticks([5])
        print(r)
        assert r == 0

    unitTest(Solution())
