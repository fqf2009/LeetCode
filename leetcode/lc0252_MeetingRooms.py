# Given an array of meeting time intervals where intervals[i] = [starti, endi],
# determine if a person could attend all meetings.
# Constraints:
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti < endi <= 10^6
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i, (start, end) in enumerate(intervals):
            if i > 0 and start < intervals[i - 1][1]:
                return False
        return True


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.canAttendMeetings([[0, 30], [5, 10], [15, 20]])
        print(r)
        assert r == False

        r = sol.canAttendMeetings([[7, 10], [2, 4]])
        print(r)
        assert r == True

        r = sol.canAttendMeetings([[1, 5], [5, 7]])
        print(r)
        assert True

    unit_test(Solution())
