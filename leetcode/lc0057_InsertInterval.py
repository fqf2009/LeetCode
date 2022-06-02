# You are given an array of non-overlapping intervals intervals
# where intervals[i] = [starti, endi] represent the start and
# the end of the ith interval and intervals is sorted in ascending order
# by starti. You are also given an interval newInterval = [start, end]
# that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted
# in ascending order by starti and intervals still does not have any
# overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# Constraints:
#   0 <= intervals.length <= 10^4
#   intervals[i].length == 2
#   0 <= starti <= endi <= 10^5
#   intervals is sorted by starti in ascending order.
#   newInterval.length == 2
#   0 <= start <= end <= 10^5
from itertools import chain
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ns, ne = newInterval
        res = []
        for start, end in intervals:
            if start > ns:
                break
            res.append([start, end])

        for start, end in chain([newInterval], intervals[len(res) :]):
            if res and start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])

        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.insert([[1, 3], [6, 9]], [2, 5])
        print(r)
        assert r == [[1, 5], [6, 9]]

        r = sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
        print(r)
        assert r == [[1, 2], [3, 10], [12, 16]]

        r = sol.insert([], [5, 7])
        print(r)
        assert r == [[5, 7]]

    unit_test(Solution())
