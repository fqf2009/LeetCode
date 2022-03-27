# Alice and Bob are opponents in an archery competition. The competition has set
# the following rules:
# 1. Alice first shoots numArrows arrows and then Bob shoots numArrows arrows.
# 2. The points are then calculated as follows:
#    - The target has integer scoring sections ranging from 0 to 11 inclusive.
#    - For each section of the target with score k (in between 0 to 11), say
#      Alice and Bob have shot ak and bk arrows on that section respectively.
#      If ak >= bk, then Alice takes k points. If ak < bk, then Bob takes k points.
#    - However, if ak == bk == 0, then nobody takes k points.
# For example, if Alice and Bob both shot 2 arrows on the section with score 11,
# then Alice takes 11 points. On the other hand, if Alice shot 0 arrows on the
# section with score 11 and Bob shot 2 arrows on that same section, then Bob
# takes 11 points.
#
# You are given the integer numArrows and an integer array aliceArrows of size 12,
# which represents the number of arrows Alice shot on each scoring section from
# 0 to 11. Now, Bob wants to maximize the total number of points he can obtain.
#
# Return the array bobArrows which represents the number of arrows Bob shot on each
# scoring section from 0 to 11. The sum of the values in bobArrows should equal
# numArrows.
#
# If there are multiple ways for Bob to earn the maximum total points, return any
# one of them.
from typing import List
from functools import cache


# Backtracking - T/S: O(2^n), O(n)
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        def backtracking(i, arrows, bobPoints):
            if i == len(aliceArrows) - 1:
                bobArrows[i] = arrows
                if arrows > aliceArrows[i]:
                    if bobPoints + i > res[0]:
                        res[0] = bobPoints + i
                        res[1] = bobArrows.copy()
                elif bobPoints > res[0]:
                    res[0] = bobPoints
                    res[1] = bobArrows.copy()
            else:
                backtracking(i+1, arrows, bobPoints)
                if arrows > aliceArrows[i]:
                    bobArrows[i] = aliceArrows[i] + 1
                    backtracking(i+1, arrows - bobArrows[i], bobPoints + i)
                    bobArrows[i] = 0

        bobArrows = [0] * len(aliceArrows)
        res = [0, [0]]  # maxPoints, maxBobArrows
        backtracking(0, numArrows, 0)

        return res[1]


# DP - T/S: O(2^n) in worst case scenario
# - DP can get the max points, as well as states!!!
class Solution1:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        n = len(aliceArrows)
        @cache
        def dp(i, arrows) -> int:
            if i == 0 or arrows == 0:
                return 0
            if arrows > aliceArrows[i]:
                dp1 = dp(i-1, arrows - aliceArrows[i] - 1) + i
                dp2 = dp(i-1, arrows)
                return max(dp1, dp2)
            else:
                return dp(i-1, arrows)

        # dp(n - 1, numArrows)  # no need do this, will be called later
        bobArrows = [0] * n
        arrowsLeft = numArrows
        for i in reversed(range(n)):
            if dp(i, arrowsLeft) > dp(i-1, arrowsLeft): 
                bobArrows[i] = aliceArrows[i] + 1
                arrowsLeft -= bobArrows[i]

        bobArrows[0] += arrowsLeft
        return bobArrows


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.maximumBobPoints(9, [1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0])
        print(r)
        assert r == [0, 0, 0, 0, 1, 1, 0, 0, 1, 2, 3, 1]

        r = sol.maximumBobPoints(3, [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2])
        print(r)
        assert r == [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]

    unitTest(Solution())
    unitTest(Solution1())
