# Given an array of meeting time intervals where intervals[i] = [starti, endi],
# return the minimum number of conference rooms required.
# Constraints:
#   1 <= intervals.length <= 10^4
#   0 <= starti < endi <= 10^6
from functools import cache
from itertools import accumulate, chain
from typing import List
import heapq


# Sweep Line - T/S: O(n*log(n)), O(n)
# - sort start and end time of all intervals together,
# - scan through sorted array, increase the count when encountering
#   start time, and decrease the count when encountering end time
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        return max(accumulate(y for _, y in sorted(
            chain.from_iterable(((s, 1), (e, -1)) for s, e in intervals))))


# Priority Queue - O(n*log(n)), O(n)
# - iterate over meeting intervals order by start time
# - use priority queue (min heap) to keep all used rooms, sorted on end time
# - if a new interval with start time >= min(end time in used rooms), meaning
#   an old room is free to be reused, pop it out, replace it with new end time;
#   otherwise, add end time to priority queue
# - at the end, the size of priority queue is the minimum number of rooms required
class Solution1:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        for start, end in sorted(intervals):    # sort by start time
            if len(rooms) > 0 and start >= rooms[0]: # a meeting room is free now
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)          # sort by end time in priority queue

        return len(rooms)


# Greedy: Wrong! Just counting is not enough! Because it does not cover
#         all scenarios how meeting room is reused.
# - similar to 0646_MaximumLengthOfPairChain
# - more similar to 0452_MinimumArrowsToBurstBalloons
# - the difference is what and how to count the number
# - although not clearly stated, in this problem,
#   end[i] == start[i+1] is not considered overlap.
class Solution2:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        max_rooms, curr_rooms, prev_end = 0, 0, 0
        for start, end in sorted(intervals, key=lambda x: x[::-1]): # sort by end time
            if start >= prev_end:
                prev_end = end
                curr_rooms = 1
            else:
                curr_rooms += 1
            max_rooms = max(curr_rooms, max_rooms)

        return max_rooms


if __name__ == '__main__':
    def unitTest(Sol):
        print(Sol.__name__)
        sol = Sol()

        # test case for duplicate time points
        r = sol.minMeetingRooms(intervals=[[9,10],[4,9],[4,17]])
        print(r)
        assert r == 2

        r = sol.minMeetingRooms(intervals=[[8, 14], [12, 13], [6, 13], [1, 9]])
        print(r)
        assert r == 3

        r = sol.minMeetingRooms(intervals=[[9, 16], [6, 16], [1, 9], [3, 15]])
        print(r)
        assert r == 3

        r = sol.minMeetingRooms(intervals=[[13, 15], [1, 13]])
        print(r)
        assert r == 1

        r = sol.minMeetingRooms(intervals=[[0, 30], [5, 10], [15, 20]])
        print(r)
        assert r == 2

        r = sol.minMeetingRooms(intervals=[[7, 10], [2, 4]])
        print(r)
        assert r == 1

    unitTest(Solution)
    unitTest(Solution1)
