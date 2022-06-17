# There is an infrastructure of n cities with some number of roads
# connecting these cities. Each roads[i] = [ai, bi] indicates that
# there is a bidirectional road between cities ai and bi.
# The network rank of two different cities is defined as the total
# number of directly connected roads to either city. If a road is
# directly connected to both cities, it is only counted once.
# The maximal network rank of the infrastructure is the maximum
# network rank of all pairs of different cities.
# Given the integer n and the array roads, return the maximal network
# rank of the entire infrastructure.
# Constraints:
#   2 <= n <= 100
#   0 <= roads.length <= n * (n - 1) / 2
#   roads[i].length == 2
#   0 <= ai, bi <= n-1
#   ai != bi
#   Each pair of cities has at most one road connecting them.
from typing import List


# O(n^2)
# Indegree of both nodes - 1 if inter-connected
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = set()
        indegree = [0] * n
        for i, j in roads:
            adj.add((min(i, j), max(i, j)))
            indegree[i] += 1
            indegree[j] += 1

        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                res = max(res, indegree[i] + indegree[j] - (1 if (i, j) in adj else 0))

        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.maximalNetworkRank(4, [[0, 1], [0, 3], [1, 2], [1, 3]])
        print(r)
        assert r == 4

        r = sol.maximalNetworkRank(5, [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]])
        print(r)
        assert r == 5

        r = sol.maximalNetworkRank(8, [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]])
        print(r)
        assert r == 5

    unit_test(Solution())
