# Alice and Bob have an undirected graph of n nodes and 3 types of edges:
#   Type 1: Can be traversed by Alice only.
#   Type 2: Can be traversed by Bob only.
#   Type 3: Can by traversed by both Alice and Bob.
# Given an array edges where edges[i] = [typei, ui, vi] represents a
# bidirectional edge of type typei between nodes ui and vi, find the
# maximum number of edges you can remove so that after removing the edges,
# the graph can still be fully traversed by both Alice and Bob. The graph
# is fully traversed by Alice and Bob if starting from any node, they can
# reach all other nodes.
# Return the maximum number of edges you can remove, or return -1 if it's
# impossible for the graph to be fully traversed by Alice and Bob.

# Constraints:
#   1 <= n <= 10^5
#   1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
#   edges[i].length == 3
#   1 <= edges[i][0] <= 3
#   1 <= edges[i][1] < edges[i][2] <= n
#   All tuples (typei, ui, vi) are distinct.
from typing import List


# Union Find - T/S: O(E), O(E)
# - sort edge, so that type 3 edge is used first.
# - use edge to connect nodes (for Alice and Bob independently).
# - if nodes are already fully connectly, then the edge can be removed.
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufA, ufB = {}, {}   # union find data structure for alice and bob each
        def find(uf, x):
            if x not in uf: return -1
            if uf[x] != x:
                uf[x] = find(uf, uf[x])
            return uf[x]

        def union(uf, x, y):
            if x not in uf:
                uf[x] = x
            x1 = find(uf, x)
            if y not in uf:
                uf[y] = y
            y1 = find(uf, y)
            if x1 != y1:
                uf[x1] = y1
                return 0
            return 1

        rmEdge = 0
        edges.sort(reverse=True)
        for type, x, y in edges:
            if type == 3:
                rmEdge += union(ufA, x, y) * union(ufB, x, y)
            elif type == 1:
                rmEdge += union(ufA, x, y)
            else:
                rmEdge += union(ufB, x, y)

        if (len(ufA) != n or len(ufB) != n or
            len(set(find(ufA, x) for x in ufA.keys())) != 1 or
            len(set(find(ufB, x) for x in ufB.keys())) != 1):
           return -1

        return rmEdge


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.maxNumEdgesToRemove(n=4, edges=[[3, 1, 2], [3, 2, 3], [1, 1, 3], 
                                                [1, 2, 4], [1, 1, 2], [2, 3, 4]])
        print(r)
        assert r == 2

        r = sol.maxNumEdgesToRemove(n=4, edges=[[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]])
        print(r)
        assert r == 0

        r = sol.maxNumEdgesToRemove(n=4, edges=[[3, 2, 3], [1, 1, 2], [2, 3, 4]])
        print(r)
        assert r == -1

    unitTest(Solution())
