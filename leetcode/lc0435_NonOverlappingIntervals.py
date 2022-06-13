# Given an array of intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of intervals you need to remove to make the 
# rest of the intervals non-overlapping.
# Constraints:
#   1 <= intervals.length <= 10^5
#   intervals[i].length == 2
#   -5 * 104 <= starti < endi <= 5 * 10^4
from typing import List


# Greedy: O(n*log(n))
# - sort by start points, if two intervals are overlapping, we want to 
#   remove the interval that has the longer end point
# - the longer interval will always overlap with more or the same number
#   of future intervals compared to the shorter one
# - e.g. 1 :  [-------------------------]       <-- remove this
#                [-------------]
#                   [----------------]          <-- then remove this
#                                  [-------------]
# - the reason is: we sort intervals by start point!!!
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        s0, e0 = intervals[0]
        res = 0
        for s1, e1 in intervals[1:]:
            if s1 < e0:     # Overlap
                if e0 > e1:
                    s0, e0 = s1, e1         # delete previous one
                elif e0 == e1 and s0 < s1:  # delete previous one
                    s0 = s1
                                            # delete current one, nothing to do
                res += 1                    # increase deletion count
            else:           # non-overlapping
                s0, e0 = s1, e1

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]])
        print(r)
        assert r == 2

        r = sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])
        print(r)
        assert r == 1

        r = sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]])
        print(r)
        assert r == 2

        r = sol.eraseOverlapIntervals([[1,2],[2,3]])
        print(r)
        assert r == 0

    unitTest(Solution())
