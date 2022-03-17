# You are given a list of songs where the ith song has a duration of time[i] seconds.
# Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
# Constraints:
# 1 <= time.length <= 6 * 10^4
# 1 <= time[i] <= 500
from typing import List
from collections import defaultdict


# Similar to 2-sum
# - to meet the condidtion:
#   ((time[i] % 60) + (time[j] % 60)) will be either 60 or 0
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counter = defaultdict(int)
        res = 0
        for t in time:
            mod = t % 60
            opp = (60 - mod) % 60
            res += counter[opp]
            counter[mod] += 1

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.numPairsDivisibleBy60([30, 20, 150, 100, 40])
        print(r)
        assert r == 3

        r = sol.numPairsDivisibleBy60([60, 60, 60])
        print(r)
        assert r == 3

    unitTest(Solution())
