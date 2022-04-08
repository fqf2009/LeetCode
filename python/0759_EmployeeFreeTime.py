# We are given a list schedule of employees, which represents the
# working time for each employee.

# Each employee has a list of non-overlapping Intervals, and these
# intervals are in sorted order.

# Return the list of finite intervals representing common,
# positive-length free time for all employees, also in sorted order.

# (Even though we are representing Intervals in the form [x, y], the
# objects inside are Intervals, not lists or arrays. For example,
# schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0]
# is not defined).  Also, we wouldn't include intervals like [5, 5] in
# our answer, as they have zero length.

# Example 1:
#   Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
#   Output: [[3,4]]
#   Explanation: There are a total of three employees, and all common
#       free time intervals would be [-inf, 1], [3, 4], [10, inf].
#       We discard any intervals that contain inf as they aren't finite.
# Constraints:
#   1 <= schedule.length , schedule[i].length <= 50
#   0 <= schedule[i].start < schedule[i].end <= 10^8

# Definition for an Interval.
from typing import List, Optional
import heapq


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

    def toList(self) -> List[Optional[int]]:
        return [self.start, self.end]

# PriorityQueue
# Time:  O(n*log(m)), where: n is number of all schedules of all employees
# Space: O(m),               m is number of employees
# Analysis:
# - All employees' schecule can be combined together, if there is still
#   free time, it is common free time.
# - If all combined schedules are sorted on start time, pick first one,
#   keep the end time e1, check next [s2, e2]
# - if s2 <= e1, no gap (free time), keep the new end time max(e1, e2)
#   else if s2 > e1, then gap is [e1, s2], new end time e2;
# - Similar to 0023_MergeKSortedLists, because schedule of each employee
#   is already sorted, use PriorityQueue to merge schedules.
class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        pq = []
        for i, sch in enumerate(schedule):
            heapq.heappush(pq, (sch[0].start, sch[0].end, i, 0))
        e1 = -1
        res = []
        while pq:
            s2, e2, i, j = heapq.heappop(pq)
            sch = schedule[i]
            j += 1
            if j < len(sch):
                heapq.heappush(pq, (sch[j].start, sch[j].end, i, j))
            if s2 <= e1:
                e1 = max(e1, e2)
            else:
                if e1 > -1:
                    res.append(Interval(e1, s2))
                e1 = e2

        return res


if __name__ == '__main__':
    def unitTest(sol):
        sch = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
        schedule = []
        for emp_sch in sch:
            schedule.append([Interval(x, y) for x, y in emp_sch])
        freeTime = sol.employeeFreeTime(schedule)
        r = [x.toList() for x in freeTime]
        print(r)
        assert r == [[3, 4]]

        sch = [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]
        schedule = []
        for emp_sch in sch:
            schedule.append([Interval(x, y) for x, y in emp_sch])
        freeTime = sol.employeeFreeTime(schedule)
        r = [x.toList() for x in freeTime]
        print(r)
        assert r == [[5, 6], [7, 9]]

    unitTest(Solution())
