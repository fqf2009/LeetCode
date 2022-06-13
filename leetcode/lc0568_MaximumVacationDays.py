# LeetCode wants to give one of its best employees the option to travel
# among n cities to collect algorithm problems. But all work and no play
# makes Jack a dull boy, you could take vacations in some particular
# cities and weeks. Your job is to schedule the traveling to maximize
# the number of vacation days you could take, but there are certain
# rules and restrictions you need to follow.
# Rules and restrictions:
#  - You can only travel among n cities, represented by indexes from
#    0 to n - 1. Initially, you are in the city indexed 0 on Monday.
#  - The cities are connected by flights. The flights are represented
#    as an n x n matrix (not necessarily symmetrical), called flights
#    representing the airline status from the city i to the city j.
#    If there is no flight from the city i to the city j,
#    flights[i][j] == 0; Otherwise, flights[i][j] == 1.
#    Also, flights[i][i] == 0 for all i.
#  - You totally have k weeks (each week has seven days) to travel. You
#    can only take flights at most once per day and can only take flights
#    on each week's Monday morning. Since flight time is so short, we do
#    not consider the impact of flight time.
#  - For each city, you can only have restricted vacation days in different
#    weeks, given an n x k matrix called days representing this relationship.
#    For the value of days[i][j], it represents the maximum days you could
#    take a vacation in the city i in the week j.
#  - You could stay in a city beyond the number of vacation days, but you
#    should work on the extra days, which will not be counted as vacation days.
#  - If you fly from city A to city B and take the vacation on that day,
#    the deduction towards vacation days will count towards the vacation
#    days of city B in that week.
#  - We do not consider the impact of flight hours on the calculation of
#    vacation days.
# Given the two matrices flights and days, return the maximum vacation
# days you could take during k weeks.
# Constraints:
#   n == flights.length
#   n == flights[i].length
#   n == days.length
#   k == days[i].length
#   1 <= n, k <= 100
#   flights[i][j] is either 0 or 1.
#   0 <= days[i][j] <= 7
from functools import cache
from typing import List


# DFS + Memo
# - T/S: O(n^2*k), O(n*k), where n = cities, k = weeks,
#        there are n*k states (due to memo), each iterate n times.
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n, k = len(flights), len(days[0])

        @cache
        def dfs(city, week) -> int:
            if week == k:
                return 0
            res = 0
            for i in range(n):
                if i == city or flights[city][i] == 1:  # stay in city_i or fly to city_i
                    res = max(res, days[i][week] + dfs(i, week + 1))
            return res

        return dfs(0, 0)


# DP - 
# - T/S: O(n^2*k), O(n), where n = cities, k = weeks
# - dp[i][j] stands for the max vacation days we can get in week i staying in city j.
# - dp[i][j] = max(dp[i - 1][k] + days[j][i]) (k = 0...N - 1, if we can go from city k to city j).
# - dp of week i only depends on week i - 1, so compress two dimensional dp array to one dimension.
# class Solution1:
#     def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
#         pass
        # n, k = len(flights), len(days[0])   # n = cities, k = weeks
        # dp = [0] * n
        # for w in reversed(range(k)): # for each week
        #     dp1 = [0] * n
        #     for i in range(n):
        #         for j in range(n):
        #             if (i == j or flights[i][j] == 1):
        #                 dp1[i] = max(dp1[i], dp[j] + days[j][w])
        #     dp = dp1

        # return max(dp)


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.maxVacationDays([[0, 1, 1], [1, 0, 1], [1, 1, 0]], days=[[1, 3, 1], [6, 0, 3], [3, 3, 3]])
        print(r)
        assert r == 12

        r = sol.maxVacationDays([[0, 1, 1], [1, 0, 1], [1, 1, 0]], days=[[7, 0, 0], [0, 7, 0], [0, 0, 7]])
        print(r)
        assert r == 21

        r = sol.maxVacationDays([[0, 0, 0], [0, 0, 0], [0, 0, 0]], days=[[1, 1, 1], [7, 7, 7], [7, 7, 7]])
        print(r)
        assert r == 3

    unit_test(Solution())
    # unit_test(Solution1())
