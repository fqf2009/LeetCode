# You are given an array time where time[i] denotes the time taken by the 
# ith bus to complete one trip.
# Each bus can make multiple trips successively; that is, the next trip 
# can start immediately after completing the current trip. Also, each 
# bus operates independently; that is, the trips of one bus do not 
# influence the trips of any other bus.
# You are also given an integer totalTrips, which denotes the number 
# of trips all buses should make in total. Return the minimum time 
# required for all buses to complete at least totalTrips trips.
# Constraints:
#   1 <= time.length <= 10^5
#   1 <= time[i], totalTrips <= 10^7
from typing import List
import heapq


# Binary Search - T/S: O(n*log(m)), O(1), where n=len(time), m=max(time)
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        leastTime = int(totalTrips / sum(1/t for t in time))
        i, j = leastTime, leastTime + max(time)
        minTime = j
        while i <= j:
            k = (i+j) // 2
            trips = sum(k // t for t in time)
            if trips >= totalTrips:
                minTime = min(minTime, k)
                j = k - 1
            else:
                i = k + 1

        return minTime


# PriorityQueue - T/S: O(n*log(n)), O(n), where n=len(time)
# - sum(1/t for t in time): is how many trips (fractional) all buses
#   can finish per unit of time
# - int(totalTrips / sum(1/t for t in time)): minimum unit of time to
#   finish totalTrips by all buses
# - then build schedule for buses' trip finishing time using PriorityQueue
# - each time pop up the first finishing bus, add its trip time as next 
#   schedule and push back to queue.
class Solution1:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        minTime = int(totalTrips / sum(1/t for t in time))
        schedule = []
        trips = 0
        for i, t in enumerate(time):
            trips += minTime // t
            schedule.append((minTime + t - (minTime % t), i))   # (nextTime, i_bus)

        heapq.heapify(schedule)
        while trips < totalTrips:
            minTime, i = heapq.heappop(schedule)
            trips += 1
            heapq.heappush(schedule, (minTime + time[i], i))

        return minTime


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.minimumTime(time = [3,3,8], totalTrips = 6)
        print(r)
        assert r == 9

        r = sol.minimumTime(time = [5,10,10], totalTrips = 9)
        print(r)
        assert r == 25

        r = sol.minimumTime(time = [1,2,3], totalTrips = 5)
        print(r)
        assert r == 3

        r = sol.minimumTime(time = [2], totalTrips = 1)
        print(r)
        assert r == 2
        
    unitTest(Solution())
    unitTest(Solution1())
