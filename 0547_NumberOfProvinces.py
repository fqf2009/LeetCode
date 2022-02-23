# There are n cities. Some of them are connected, while some are not.
# If city a is connected directly with city b, and city b is connected
# directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and
# no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1
# if the ith city and the jth city are directly connected, and
# isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.

# Constraints:
#   1 <= n <= 200
#   n == isConnected.length
#   n == isConnected[i].length
#   isConnected[i][j] is 1 or 0.
#   isConnected[i][i] == 1
#   isConnected[i][j] == isConnected[j][i]
from typing import List, Optional


# Union Find
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = {}
        def find(x):
            if uf.setdefault(x, x) != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        n = len(isConnected)
        for i in range(n):
            for j in range(0, i):
                if isConnected[i][j] == 1:
                    uf[find(i)] = find(j)

        return n - len(uf) + len(set(find(x) for x in uf))


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.findCircleNum(isConnected=[[1, 1, 0],
                                           [1, 1, 0], 
                                           [0, 0, 1]])
        print(r)
        assert r == 2

        r = sol.findCircleNum(isConnected=[[1, 0, 0], 
                                           [0, 1, 0],
                                           [0, 0, 1]])
        print(r)
        assert r == 3

    unitTest(Solution())
