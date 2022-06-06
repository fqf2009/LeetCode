# Alice has n balloons arranged on a rope. You are given a 0-indexed
# string colors where colors[i] is the color of the ith balloon.
# Alice wants the rope to be colorful. She does not want two consecutive
# balloons to be of the same color, so she asks Bob for help. Bob can
# remove some balloons from the rope to make it colorful. You are given
# a 0-indexed integer array neededTime where neededTime[i] is the time
# (in seconds) that Bob needs to remove the ith balloon from the rope.
# Return the minimum time Bob needs to make the rope colorful.
# Constraints:
#   n == colors.length == neededTime.length
#   1 <= n <= 10^5
#   1 <= neededTime[i] <= 10^4
#   colors contains only lowercase English letters.
from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        grp_sum, grp_max, res = 0, 0, 0
        for i, (c, t) in enumerate(zip(colors, neededTime)):
            grp_sum += t
            grp_max = max(grp_max, t)
            if i == len(colors) - 1 or colors[i + 1] != c:
                res += grp_sum - grp_max
                grp_sum, grp_max = 0, 0

        return res


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.minCost("aaabbbabbbb", [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1])
        print(r)
        assert r == 26

        r = sol.minCost("abaac", [1, 2, 3, 4, 5])
        print(r)
        assert r == 3

        r = sol.minCost("abc", [1, 2, 3])
        print(r)
        assert r == 0

        r = sol.minCost("aabaa", [1, 2, 3, 4, 1])
        print(r)
        assert r == 2

    unitTest(Solution())
