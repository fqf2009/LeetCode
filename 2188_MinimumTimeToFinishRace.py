# You are given a 0-indexed 2D integer array tires where tires[i] = [fi, ri]
# indicates that the ith tire can finish its xth successive lap in
# fi * ri(x-1) seconds.
# For example, if fi = 3 and ri = 2, then the tire would finish its 1st lap
# in 3 seconds, its 2nd lap in 3 * 2 = 6 seconds, its 3rd lap in 3 * 22 = 12
# seconds, etc.
# You are also given an integer changeTime and an integer numLaps.
# The race consists of numLaps laps and you may start the race with any tire.
# You have an unlimited supply of each tire and after every lap, you may
# change to any given tire (including the current tire type) if you wait
# changeTime seconds.
# Return the minimum time to finish the race.

# Constraints:
#   1 <= tires.length <= 10^5
#   tires[i].length == 2
#   1 <= fi, changeTime <= 10^5
#   2 <= ri <= 10^5
#   1 <= numLaps <= 1000
from typing import List
from functools import cache


# DP: O(m + n^2), where n = numLaps, m = len(tires)
# - assume dp[i] is minimum time to finish the race
# - dp[i] = min(go straight i loops without change, 
#               dp[j] + changeTime + dp[i-j] for j in range(1, i//2 + 1))
# Optimize: O(18*m + 18*n) => O(m + n)
# - in best case when fi = 1, ri = 2, time of the 18th lap is:
#   1 + 2^(18-1) = 131073, but changeTime < 10^5, 
#   so never go straight more than 18 laps.
# - dp[i] = min(go straight i loops without change, 
#               dp[j] + changeTime + dp[i-j] for j in range(1, min(19, i//2 + 1)))
class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        @cache
        def dp(i: int) -> int:
            if i == 1: return go_straight[1]
            res = go_straight[i] if i <= 18 else 10**10
            for j in range(1, min(19, i//2 + 1)):
                res = min(res, dp(j) + changeTime + dp(i - j))
            return res

        go_straight = [10**10] * 19
        for f, r in tires:
            totalTime = lapTime = f
            for i in range(1, 19):
                go_straight[i] = min(go_straight[i], totalTime)
                lapTime *= r
                totalTime += lapTime
                if totalTime > 2e5: break

        return dp(numLaps)


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.minimumFinishTime(tires=[[2, 3], [3, 4]], changeTime=5, numLaps=4)
        print(r)
        assert r == 21

        r = sol.minimumFinishTime(tires=[[1, 10], [2, 2], [3, 4]], changeTime=6, numLaps=5)
        print(r)
        assert r == 25

    unitTest(Solution())
