# You have a graph of n nodes. You are given an integer n and an array edges
# where edges[i] = [ai, bi] indicates that there is an edge between ai and
# bi in the graph.
# Return the number of connected components in the graph.
from typing import List


# Union Find
# - Small improvement: count group during unioning
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = {}
        def find(x):
            if uf.setdefault(x, x) != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        group = n
        for x, y in edges:
            n1, n2 = find(x), find(y)
            if n1 != n2:
                uf[n1] = n2
                group -= 1

        return group


# Union Find
class Solution1:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = {}
        def find(x):
            if uf.setdefault(x, x) != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        for x, y in edges:
            uf[find(x)] = find(y)

        return n - len(uf) + len({find(x) for x in uf})


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.countComponents(n=5, edges=[[0, 1], [1, 2], [3, 4]])
        print(r)
        assert r == 2

        r = sol.countComponents(n=5, edges=[[0, 1], [1, 2], [2, 3], [3, 4]])
        print(r)
        assert r == 1

    unitTest(Solution())
    unitTest(Solution1())
