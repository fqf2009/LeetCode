from typing import List
from operator import itemgetter
import bisect

# There is a 2D grid of size n x n where each cell of this grid has a lamp that is initially turned off.
# You are given a 2D array of lamp positions lamps, where lamps[i] = [rowi, coli] indicates that the lamp
#  at grid[rowi][coli] is turned on. Even if the same lamp is listed more than once, it is turned on.
# When a lamp is turned on, it illuminates its cell and all other cells in the same row, column, or diagonal.
# You are also given another 2D array queries, where queries[j] = [rowj, colj]. For the jth query, determine
# whether grid[rowj][colj] is illuminated or not. After answering the jth query, turn off the lamp at
# grid[rowj][colj] and its 8 adjacent lamps if they exist. A lamp is adjacent if its cell shares either
# a side or corner with grid[rowj][colj]. Return an array of integers ans, where ans[j] should be 1 if the
# cell in the jth query was illuminated, or 0 if the lamp was not.

# Use binary search to improve the performance for checking lamps.
# Project diagonal lights of lamps to the edge of grid, so that binary search can be used as well.
# Complexity: O(m*log(n)), where m is queries' count, and n is lamps' count
class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        def checkHorzVert(lights, i, j) -> bool:
            left = bisect.bisect_left(lights, [i])
            illuminated = False
            while left < len(lights) and lights[left][0] == i:
                if lights[left][2] != 0:
                    illuminated = True
                left += 1
            return illuminated

        def checkDiagonal(lights, i, j) -> bool:
            left = bisect.bisect_left(lights, [i])
            illuminated = False
            while left < len(lights) and lights[left][0] == i:
                if lights[left][2] != 0:
                    illuminated = True
                left += 1
            return illuminated

        def turnOffHorzVert(lights, i, j):
            left = bisect.bisect_left(lights, [i - 1])
            illuminated = False
            while left < len(lights) and lights[left][0] <= i + 1:
                if lights[left][2] != 0:
                    if abs(lights[left][1] - j) <= 1:
                        lights[left][2] = 0
                left += 1
            return illuminated

        def turnOffDiagonal(lights, i, j):
            left = bisect.bisect_left(lights, [i - 2])
            illuminated = False
            while left < len(lights) and lights[left][0] <= i + 2:
                if lights[left][2] != 0:
                    x = (lights[left][0] + lights[left][1]) // 2
                    y = (lights[left][0] - lights[left][1]) // 2
                    a = (i + j) // 2
                    b = (i - j) // 2
                    if abs(x - a) <= 1 and abs(y - b) <= 1:
                        lights[left][2] = 0
                left += 1
            return illuminated

        # gridIllumination() starts here
        if len(queries) == 0:
            return []

        if len(lamps) == 0:
            return [0] * len(queries)

        vert = [[x[0], x[1], 1] for x in sorted(lamps)]
        horz = [[x[1], x[0], 1] for x in sorted(lamps, key=itemgetter(1))]
        dia1 = [[x[0] + x[1], x[0] - x[1], 1] for x in lamps]
        dia2 = [[x[0] - x[1], x[0] + x[1], 1] for x in lamps]
        dia1.sort()
        dia2.sort()
        ans = []
        for query in queries:
            i, j = query[0], query[1]
            illum1 = checkHorzVert(vert, i, j)
            illum2 = checkHorzVert(horz, j, i)
            illum3 = checkDiagonal(dia1, i + j, i - j)
            illum4 = checkDiagonal(dia2, i - j, i + j)
            illuminated = illum1 or illum2 or illum3 or illum4
            ans.append(int(illuminated))
            if illuminated:
                turnOffHorzVert(vert, i, j)
                turnOffHorzVert(horz, j, i)
                turnOffDiagonal(dia1, i + j, i - j)
                turnOffDiagonal(dia2, i - j, i + j)

        return ans


# Brute Force: O(M*N), where M is len(lamps), N is len(queries)
# Time limit exceeded
class Solution1:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for query in queries:
            i, j = tuple(query)
            illuminated = False
            for lamp in lamps:
                m, n = tuple(lamp)
                if m >= 0:  # still on
                    if i == m or j == n or abs(i - m) == abs(j - n):
                        illuminated = True
                        if abs(i - m) <= 1 and abs(j - n) <= 1:
                            lamp[0] = -1    # turn off
            ans.append(int(illuminated))

        return ans


if __name__ == '__main__':
    sol = Solution()

    n = 10
    lamps = [[3,4],[6,6],[1,8],[4,5],[8,7],[0,6],[5,2],[1,9]]
    queries = [[7,9],[2,8],[8,6],[6,8],[2,8]]
    r = sol.gridIllumination(n, lamps, queries)
    print(r)
    assert(r == [1,1,1,1,1])

    n = 6
    lamps = [[2, 5], [4, 2], [0, 3], [0, 5], [1, 4], [4, 2], [3, 3], [1, 0]]
    queries = [[4, 3], [3, 1], [5, 3], [0, 5], [4, 4], [3, 3]]
    r = sol.gridIllumination(n, lamps, queries)
    print(r)
    assert(r == [1, 0, 1, 1, 0, 1])

    n = 5
    lamps = [[0, 0], [4, 4]]
    queries = [[1, 1], [1, 0]]
    r = sol.gridIllumination(n, lamps, queries)
    print(r)
    assert(r == [1, 0])

    n = 5
    lamps = [[0, 0], [4, 4]]
    queries = [[1, 1], [1, 1]]
    r = sol.gridIllumination(n, lamps, queries)
    print(r)
    assert(r == [1, 1])

    n = 5
    lamps = [[0, 0], [0, 4]]
    queries = [[0, 4], [0, 1], [1, 4]]
    r = sol.gridIllumination(n, lamps, queries)
    print(r)
    assert(r == [1, 1, 0])
