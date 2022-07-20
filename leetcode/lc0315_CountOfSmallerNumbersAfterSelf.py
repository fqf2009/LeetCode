# You are given an integer array nums and you have to return a new
# counts array. The counts array has the property where counts[i]
# is the number of smaller elements to the right of nums[i].
# Constraints:
#   1 <= nums.length <= 10^5
#   -10^4 <= nums[i] <= 10^4
from sortedcontainers import SortedList
from typing import List


# SortedList - T/S: O(n*log(n)), O(n)
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        visited = SortedList()
        for v in reversed(nums):
            res.append(visited.bisect_left(v))
            visited.add(v)

        return res[::-1]


# Segment Tree
class Solution1:
    def countSmaller(self, nums: List[int]) -> List[int]:
        pass


# Binary Indexed Tree (Fenwick Tree)
class Solution2:
    def countSmaller(self, nums: List[int]) -> List[int]:
        pass


# Merge Sort
class Solution3:
    def countSmaller(self, nums: List[int]) -> List[int]:
        pass


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.countSmaller([5, 2, 6, 1])
        print(r)
        assert r == [2, 1, 1, 0]

        r = sol.countSmaller([-1])
        print(r)
        assert r == [0]

        r = sol.countSmaller([-1, -1])
        print(r)
        assert r == [0, 0]

    unitTest(Solution())
