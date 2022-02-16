# On a 2D plane, we place n stones at some integer coordinate
# points. Each coordinate point may have at most one stone.

# A stone can be removed if it shares either the same row or
# the same column as another stone that has not been removed.

# Given an array stones of length n where stones[i] = [xi, yi]
# represents the location of the ith stone, return the largest
# possible number of stones that can be removed.

# Constraints:
#   1 <= stones.length <= 1000
#   0 <= xi, yi <= 10^4
#   No two stones are at the same coordinate point.
from typing import List

# Graph + DFS - T/S: O(n), O(n^2)
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(x: int):
            visited[x] = True
            for y in gr[x]:
                if not visited[y]:
                    dfs(y)

        gr = {}
        for i, j in stones:
            gr.setdefault(i, set()).add(~j)
            gr.setdefault(~j, set()).add(i)
        
        islands = 0
        visited = {x: False for x in gr.keys()}
        for x in gr.keys():
            if not visited[x]:
                dfs(x)
                islands += 1

        return len(stones) - islands


# Idea and code from https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/discuss/197668/Count-the-Number-of-Islands-O(N)
# - Connected stones can be reduced to 1 stone,
#   max_stones_removed = stones_number - islands_number
# - DFS can be used to count islands, and also can be used to
#   reveal how to remove stone, just remove stones in reverse
#   order of DFS.
# - Below is the Union Find solution:
#    - each point's x and y become two connected nodes in UF.
#    - different points having either the same x or y are connected.
#    - total nodes in UF are the number of different x and y.
#    - path compression is implemented in find()
#    - to differentiate x and y, use ~y. e.g. ~5 will be -6.
#      using -y is not good, because 0 and -0 are the same.
#    - T/S: O(n), O(n)
class Solution1:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = {}

        def find(x):
            if x != uf.setdefault(x, x):
                uf[x] = find(uf[x])     # path compression
            return uf[x]

        for i, j in stones:
            uf[find(i)] = find(~j)
        return len(stones) - len({find(x) for x in uf}) # use set to unique root


if __name__ == '__main__':
    def unit_test(sol):
        # [[1, 1, 0],
        #  [1, 0, 1],
        #  [0, 1, 1]]
        r = sol.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]])
        print(r)
        assert r == 5

        # [[1, 0, 1],
        #  [0, 1, 0],
        #  [1, 0, 1]]
        r = sol.removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]])
        print(r)
        assert r == 3

        # [[1, 1, 0, 0, 1],
        #  [1, 1, 0, 0, 0],
        #  [0, 1, 1, 0, 0],
        #  [0, 0, 1, 1, 1],
        #  [1, 0, 0, 1, 1]]
        r = sol.removeStones([[0, 0], [0, 1], [0, 4], [1, 0], [1, 1], [2, 1], [2, 2],
                              [3, 2], [3, 3], [3, 4], [4, 0], [4, 3], [4, 4]])
        print(r)
        assert r == 12

    unit_test(Solution())
    unit_test(Solution1())
