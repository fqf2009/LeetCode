# There are n gas stations along a circular route, where the amount of gas
# at the i-th station is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to
# travel from the i-th station to its next (i + 1)th station. You begin the
# journey with an empty tank at one of the gas stations.
# Given two integer arrays gas and cost, return the starting gas station's
# index if you can travel around the circuit once in the clockwise direction,
# otherwise return -1. If there exists a solution, it is guaranteed to be unique.
# Constraints:
#   gas.length == n
#   cost.length == n
#   1 <= n <= 105
#   0 <= gas[i], cost[i] <= 10^4
from typing import List


# global cumulative sum + current cumulative sum
# Analysis:
# - assume global csum is total_tank, current cumulative sum is curr_tank
# - if total_tank < 0, not enough gas for whole circle, obviously
# - if curr_tank < 0, means from start_station to curr_station, not enough
#   gas to travel, so try to start from next station, obviously it is better
#   than current station, and obviously from last station to current station
#   the net gas is deficit.
# - when it runs to end, if total_tank >= 0, then start_station will be the
#   first station which meets the condition.
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank, curr_tank, start_station = 0, 0, 0
        for i in range(len(gas)):
            curr_tank += gas[i] - cost[i]
            total_tank += gas[i] - cost[i]
            if curr_tank < 0:
                curr_tank = 0
                # start_station = i, also ok; 0 is tried before, already failed.
                start_station = (i + 1) % len(gas)

        if total_tank < 0:
            return -1
        else:
            return start_station


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.canCompleteCircuit([7, 1, 0, 11, 4], [5, 9, 1, 2, 5])
        print(r)
        assert r == 3

        r = sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
        print(r)
        assert r == 3

        r = sol.canCompleteCircuit([2, 3, 4], [3, 4, 3])
        print(r)
        assert r == -1

    unitTest(Solution())
