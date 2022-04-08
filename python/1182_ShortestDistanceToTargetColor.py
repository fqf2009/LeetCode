# You are given an array colors, in which there are three
# colors: 1, 2 and 3.
# You are also given some queries. Each query consists of two integers
# i and c, return the shortest distance between the given index i and
# the target color c. If there is no solution return -1.
# Constraints:
#   1 <= colors.length <= 5*10^4
#   1 <= colors[i] <= 3
#   1 <= queries.length <= 5*10^4
#   queries[i].length == 2
#   0 <= queries[i][0] < colors.length
#   1 <= queries[i][1] <= 3
from typing import List


# DP + Iteration
# - dpL[c, i], at position i, nearest pos from left for color c
# - dpR[c, i], at position i, nearest pos from right for color c
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        dpL = [[0]*n for _ in range(3)]
        dpR = [[0]*n for _ in range(3)]
        for i in range(n):
            for j in range(3):
                if colors[i] == j+1:
                    dpL[j][i] = i
                else:
                    dpL[j][i] = dpL[j][i-1] if i > 0 else -2**31
                if colors[n-1-i] == j+1:
                    dpR[j][n-1-i] = n-1-i
                else:
                    dpR[j][n-1-i] = dpR[j][n-i] if n-i < n else 2**31

        res = []
        for i, c in queries:
            d = min(i - dpL[c-1][i], dpR[c-1][i] - i)
            if d > 2**30:
                res.append(-1)
            else:
                res.append(d)

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.shortestDistanceColor([1, 1, 2, 1, 3, 2, 2, 3, 3], [[1, 3], [2, 2], [6, 1]])
        print(r)
        assert r == [3, 0, 3]

        r = sol.shortestDistanceColor([1, 2], [[0, 3]])
        print(r)
        assert r == [-1]

        r = sol.shortestDistanceColor([2, 1, 2, 2, 1], [[1, 1], [4, 3], [1, 3], [4, 2], [2, 1]])
        print(r)
        assert r == [0, -1, -1, 1, 1]

    unitTest(Solution())
