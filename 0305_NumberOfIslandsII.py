# You are given an empty 2D binary grid grid of size m x n. The grid
# represents a map where 0's represent water and 1's represent land. Initially,
# all the cells of grid are water cells (i.e., all the cells are 0's).

# We may perform an add land operation which turns the water at position
# into a land. You are given an array positions where positions[i] = [ri, ci]
# is the position (ri, ci) at which we should operate the ith operation.

# Return an array of integers answer where answer[i] is the number of islands
# after turning the cell (ri, ci) into a land.

# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.

# Constraints:
#   1 <= m, n, positions.length <= 10^4
#   1 <= m * n <= 10^4
#   positions[i].length == 2
#   0 <= ri < m
#   0 <= ci < n
from typing import List


# Union Find: O(k), where k = len(positions)
# - use data struction UF to keep track the numbers of islands, i.e. connected land
#   groups.
# - increase islands each time to add a land.
# - reduce islands each time to union lands into island.
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = {}
        def find(c):
            if c in uf:
                if uf[c] != c:
                    uf[c] = find(uf[c])
                return uf[c]
            else:
                return -1
        
        islands = 0
        res = []
        for x1, y1 in positions:
            c1 = x1*100000 + y1
            if c1 not in uf:
                uf[c1] = c1
                islands += 1
            else:
                c1 = find(c1)

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x2, y2 = x1 + dx, y1 + dy
                if 0 <= x2 < m and 0 <= y2 < n:
                    c2 = find(x2*100000 + y2)
                    if c2 != -1 and c1 != c2:
                        uf[c1] = c2
                        c1 = c2
                        islands -= 1
                        
            res.append(islands)

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.numIslands2(m=1, n=1, positions=[[0, 0]])
        print(r)
        assert r == [1]

        r = sol.numIslands2(m=3, n=3, positions=[[0, 0], [0, 1], [1, 2], [2, 1]])
        print(r)
        assert r == [1, 1, 2, 3]

    unitTest(Solution())
