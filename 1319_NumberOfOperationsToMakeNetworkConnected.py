# There are n computers numbered from 0 to n - 1 connected by ethernet cables
# connections forming a network where connections[i] = [ai, bi] represents a
# connection between computers ai and bi. Any computer can reach any other
# computer directly or indirectly through the network.

# You are given an initial computer network connections. You can extract certain
# cables between two directly connected computers, and place them between any
# pair of disconnected computers to make them directly connected.

# Return the minimum number of times you need to do this in order to make all
# the computers connected. If it is not possible, return -1.

# Constraints:
#   1 <= n <= 10^5
#   1 <= connections.length <= min(n * (n - 1) / 2, 10^5)
#   connections[i].length == 2
#   0 <= ai, bi < n
#   ai != bi
#   There are no repeated connections.
#   No two computers are connected by more than one cable.
from typing import List


# Union Find
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf = {}
        def find(x):
            if uf.setdefault(x, x) != x:
                uf[x] = find(uf[x])
            return uf[x]

        if len(connections) < n - 1: return -1
        for n1, n2 in connections:
            uf[find(n1)] = find(n2)
        # n - len(uf): nodes not in connections
        # len(set(find(x) for x in uf)): nodes in connections, but in several groups
        return n - len(uf) + len(set(find(x) for x in uf)) - 1


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.makeConnected(n=4, connections=[[0, 1], [0, 2], [1, 2]])
        print(r)
        assert r == 1

        r = sol.makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]])
        print(r)
        assert r == 2

        r = sol.makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2]])
        print(r)
        assert r == -1

    unitTest(Solution())
