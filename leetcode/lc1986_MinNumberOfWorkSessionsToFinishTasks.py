# There are n tasks assigned to you. The task times are represented
# as an integer array tasks of length n, where the ith task takes
# tasks[i] hours to finish. A work session is when you work for at
# most sessionTime consecutive hours and then take a break.
# You should finish the given tasks in a way that satisfies the
# following conditions:
# If you start a task in a work session, you must complete it in
# the same work session.
# You can start a new task immediately after finishing the previous one.
# You may complete the tasks in any order.
# Given tasks and sessionTime, return the minimum number of work
# sessions needed to finish all the tasks following the conditions above.
# The tests are generated such that sessionTime is greater than or
# equal to the maximum element in tasks[i].
# Constraints:
#   n == tasks.length
#   1 <= n <= 14
#   1 <= tasks[i] <= 10
#   max(tasks[i]) <= sessionTime <= 15
from functools import cache
from typing import List


# https://en.wikipedia.org/wiki/Bin_packing_problem
# DP (bit-mask + backtracking)
# - T/S: O(2^n*K*n), O(2^n*K), where K = sessionTime
# - with memo (cache), still TLE (Time Limit Exceeded)
#   without cache, takes way longer!!!
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        @cache
        def dp(mask, capacity):     # return number of sessions required for bit mask
            if mask == 0:
                return 0
            res = n
            for i in range(n):
                if mask & (1 << i):
                    mask1 = mask - (1 << i)     # mask & ~(1 << i)
                    if capacity >= tasks[i]:
                        res = min(res, dp(mask1, capacity - tasks[i]))
                    else:
                        res = min(res, dp(mask1, sessionTime - tasks[i]) + 1)
            return res

        res = dp((1 << n) - 1, 0)
        # print(dp.cache_info())
        return res


# Backtracking without bitmask
# - cannot use memo, however, it can find good candidates
#   in early phase, and skip any worse solution.
# - without tasks.sort(reverse=True), it will be 20 times slower
#   in LeetCode submission. but no TLE.
class Solution1:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        tasks.sort(reverse=True)    # !!! let good candidate solution appear earlier
        bins = []
        res = n

        def backtrack(p):   # p-th task
            nonlocal res
            if len(bins) >= res:    # !!! skip if not a better solution
                return              # This is the trick to make it fast!!!
            if p == n:      # all tasks are in bins
                res = len(bins)
                return
            for i, v in enumerate(bins):  # put p-th task in existing bins
                if v + tasks[p] <= sessionTime:
                    bins[i] += tasks[p]
                    backtrack(p + 1)
                    bins[i] -= tasks[p]
            bins.append(tasks[p])   # add a new bin
            backtrack(p + 1)
            bins.pop()

        backtrack(0)
        return res


# Not working!!!
class Solution2:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        tasks.sort(reverse=True)

        bin = []
        for t in tasks:
            bin1 = [(v, i) for i, v in enumerate(bin) if v >= t]
            if bin1:
                bin[min(bin1)[1]] -= t
            else:
                bin.append(sessionTime - t)  # remaining capacity

        return len(bin)


if __name__ == "__main__":

    def unit_test(solution):
        print(solution.__name__)
        sol = solution()

        r = sol.minSessions([2, 3, 3, 4, 4, 4, 5, 6, 7, 10], 12)
        print(r)
        assert r == 4

        r = sol.minSessions([1, 2, 3], sessionTime=3)
        print(r)
        assert r == 2

        r = sol.minSessions([3, 1, 3, 1, 1], sessionTime=8)
        print(r)
        assert r == 2

        r = sol.minSessions([1, 2, 3, 4, 5], sessionTime=15)
        print(r)
        assert r == 1

        r = sol.minSessions([5, 9, 7, 4, 4, 7, 7, 9], 9)
        print(r)
        assert r == 7

        r = sol.minSessions([9, 8, 8, 10, 10, 8, 10, 4, 8, 9, 9, 3, 10], 15)
        print(r)
        assert r == 11

        r = sol.minSessions([8, 1, 3, 10, 9, 5, 10, 2, 10, 3, 5, 10, 10, 7], 14)
        print(r)
        assert r == 8

    unit_test(Solution1)
    unit_test(Solution)
