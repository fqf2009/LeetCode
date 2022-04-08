# You are given an m x n grid grid of values 0, 1, or 2, where:
# - each 0 marks an empty land that you can pass by freely,
# - each 1 marks a building that you cannot pass through, and
# - each 2 marks an obstacle that you cannot pass through.
# You want to build a house on an empty land that reaches all buildings in the
# shortest total travel distance. You can only move up, down, left, and right.
# Return the shortest travel distance for such a house. If it is not possible
# to build such a house according to the above rules, return -1.
# The total travel distance is the sum of the distances between the houses of
# the friends and the meeting point.
#
# - The distance is calculated using Manhattan Distance, where
#   distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
# - Note the above is misleading!!! What we really need is the travel distance.
#   Manhattan Distance is only correct when there is no obstacle, or other 
#   buildings blocking the route. Therefore, BFS is the only remaining choice.
#
# Constraints:
#   m == grid.length
#   n == grid[i].length
#   1 <= m, n <= 50
#   grid[i][j] is either 0, 1, or 2.
#   There will be at least one building in the grid.
from collections import deque
from turtle import distance
from typing import List


# BFS: from buildings to lands
# - T/S: O(B*m*n), O(m*n), i.e., from each building (B), bfs visit each cell (m*n)
# Analysis:
# - distance[i][j] to accumulate each buiding to each land (grid[i][j])'s shortest
#   distance, only those lands visited by each building will be valid.
# - Optimize: mark the lands in grid each time when it is visited by a building;
#             simply decreasing it by one each time, and value will be -nth building;
#             e.g. 0 => -1 for first visit, -1 => -2 for second visit, etc.
#             if it is not the -(n-1) value before the change, skip it
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        MAX_DISTANCE = 2**31
        m, n = len(grid), len(grid[0])
        land_distance = [[0]*n for _ in range(m)]
        
        def bfs_visit(i: int, j: int) -> int:
            res = MAX_DISTANCE
            que = deque()
            que.append((i, j, 0))
            while que:
                i, j, distance = que.popleft()
                for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == -nth_building:
                        grid[x][y] -= 1     # visited, ready for visit from next building
                        land_distance[x][y] += distance + 1
                        que.append((x, y, distance + 1))
                        res = min(res, land_distance[x][y])
            return res

        res = -1
        nth_building = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = bfs_visit(i, j)
                    if res == MAX_DISTANCE: # this building cannot reach any previous valid land
                        return -1
                    nth_building += 1

        return res


# BFS: from lands to buildings
# - Optimize: record all lands during BFS, after first successful visit to all
#             buildings, skip remaining lands not in building_reachable_lands.
# !!! Wrong - building reachable lands could be in different sets. Set test case!!!
class SolutionError:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        MAX_DISTANCE = 2**31
        m, n = len(grid), len(grid[0])
        total_buildings = sum(1 for i in range(m) for j in range(n) if grid[i][j] == 1)
        building_reachable_lands = set()
        
        que = deque()

        def bfs_visit(keep_lands):
            visited = [[False]*n for _ in range(m)]
            buildings = 0
            travels = 0
            while que:
                i, j, distance = que.popleft()
                for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n and grid[x][y] != 2 and not visited[x][y]:
                        visited[x][y] = True
                        if grid[x][y] == 1:
                            buildings += 1
                            travels += distance + 1
                        else: # grid[i1][j1] == 0
                            if keep_lands:
                                building_reachable_lands.add((i, j))
                            que.append((x, y, distance + 1))
            return (buildings, travels)

        keep_lands = True
        res = MAX_DISTANCE
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (len(building_reachable_lands) == 0
                                        or (i, j) in building_reachable_lands):
                    que.clear()
                    que.append((i, j, 0))
                    buildings, travels = bfs_visit(keep_lands)
                    if buildings == total_buildings:
                        keep_lands = False
                        res = min(res, travels)
                    elif keep_lands:
                        building_reachable_lands.clear()


        return -1 if res == MAX_DISTANCE else res


# BFS: from lands to buildings
# - Time Limit Exceeded - 78 / 85 test cases passed.
# - T/S: O(L*m*n), O(m*n), i.e., from each land (L), bfs visit each cell (m*n)
class Solution1:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        MAX_DISTANCE = 2**31
        m, n = len(grid), len(grid[0])
        total_buildings = sum(1 for i in range(m) for j in range(n) if grid[i][j] == 1)
        que = deque()

        def bfs_visit():
            visited = [[False]*n for _ in range(m)]
            buildings = 0
            travels = 0
            while que:
                i, j, distance = que.popleft()
                for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n and grid[x][y] != 2 and not visited[x][y]:
                        visited[x][y] = True
                        if grid[x][y] == 1:
                            buildings += 1
                            travels += distance + 1
                        else: # grid[i1][j1] == 0
                            que.append((x, y, distance + 1))
            return (buildings, travels)

        res = MAX_DISTANCE
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    que.clear()
                    que.append((i, j, 0))
                    buildings, travels = bfs_visit()
                    if buildings == total_buildings:
                        res = min(res, travels)
        
        return -1 if res == MAX_DISTANCE else res


# DFS - Wrong! because the travel distance is needed, not Manhattan Distance.
#              besides, build can block route as well.
# T/S: O(m*n + B*L), O(m*n), where:
#       m*n are grid size, B and L are number of buildings and lands.
# - first, from one build, DFS visit all other buildings and empty lands;
#   collect cordinates of all buildings and empty lands.
# - if the number of visited builds is less than the number of total builds,
#   there is no solution, return -1;
# - iterate through all empty lands visited in first step, for each one,
#   calculate total travel distance with all buildings.
class Solution9:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        buildings = []
        lands = []
        visited = [[False]*n for _ in range(m)]

        def dfs_visit(i, j):
            if visited[i][j] or grid[i][j] == 2: return

            visited[i][j] = True
            if grid[i][j] == 1:
                buildings.append((i, j))
            else: # grid[i][j] == 0
                lands.append((i, j))

            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                i1, j1 = i + di, j + dj
                if 0 <= i1 < m and 0 <= j1 < n:
                    dfs_visit(i1, j1)

        total_builds = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if total_builds == 0:
                        dfs_visit(i, j)     # from first building to visit all
                    total_builds += 1               

        # no empty lands, or cannot connect to all buildings
        if len(buildings) < total_builds or len(lands) == 0:
            return -1

        res = m*n*(m+n)
        for x, y in lands:
            distance = 0
            for i, j in buildings:
                distance += abs(x - i) + abs(y - j)
            res = min(res, distance)

        return res


if __name__ == "__main__":
    def unit_test(sol):
        grid = [[2,0,0],        # building reachable lands are not in the same set!!!
                [0,1,0],
                [1,0,0]]
        r = sol.shortestDistance(grid)
        print(r)
        assert r == 2

        r = sol.shortestDistance([[1,1],    # building can block route too.
                                  [0,1]])
        print(r)
        assert r == -1

        r = sol.shortestDistance([[1, 0, 2, 0, 1], 
                                  [0, 0, 0, 0, 0], 
                                  [0, 0, 1, 0, 0]])
        print(r)
        assert r == 7

        r = sol.shortestDistance([[1, 0, 0, 2, 1], 
                                  [0, 0, 0, 0, 2], 
                                  [0, 0, 1, 0, 0]])
        print(r)
        assert r == -1

        r = sol.shortestDistance([[1, 0]])
        print(r)
        assert r == 1

        r = sol.shortestDistance([[1]])
        print(r)
        assert r == -1

        grid = [[0,2,0,0,0,2,0,0,1,0,0,0,0,0,0,0,0,0,0,0,2,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,2,1,0,0,1,0,0,0,0,1,0],
                [0,2,1,0,0,0,0,0,2,0,1,1,1,2,0,0,0,0,0,1,0,0,0,2,0,0,1,0,0,0,0,0,0,1,0,2,0,1,0,0,0,2,0,0,0,0,0],
                [0,0,0,0,0,2,0,2,1,0,0,0,2,0,2,0,0,1,1,0,0,0,0,0,0,2,0,0,0,0,0,2,0,2,1,0,0,0,0,0,0,2,0,0,0,0,0],
                [1,0,0,0,1,2,0,0,0,0,2,0,0,0,1,0,2,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,1,0,0,0,0,1,0,0,0,1],
                [0,0,0,2,1,0,2,0,0,0,0,0,0,2,0,0,0,2,0,1,0,0,0,0,0,1,0,0,0,2,0,2,2,0,0,1,2,0,0,1,0,0,1,0,0,0,1],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [0,1,1,1,0,0,0,1,1,0,0,0,0,0,2,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,2,0,2,1,1,0,0,0,0,1,0,0,0,2,0,0,0],
                [0,2,0,0,0,0,2,0,0,0,1,2,0,2,0,1,1,0,0,1,0,2,0,0,2,1,0,0,0,0,2,0,0,0,0,0,0,0,2,1,0,0,0,1,2,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
                [1,0,1,2,0,0,0,0,1,2,1,0,0,1,0,0,2,0,0,0,2,0,0,0,1,2,1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0,0,0,1,0,0,2,0,1,0,2,0,0,2,0,0,0,0,2,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,2,0,2,2,2,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,1,0,0,1,0,0,0,1,0,0,0,2,0,2,1,0,2,0,0,0,2,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,2,0,0,0,0,0,0],
                [0,0,0,0,0,2,0,2,2,0,0,0,0,0,1,2,0,0,0,0,0,2,0,0,0,0,2,0,0,2,2,0,0,0,1,0,1,0,2,0,0,0,0,0,0,2,0],
                [0,2,2,2,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,2,1,0,0,0,1,1,2,0,1,0,1,2,0,0,0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0],
                [0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,2,1,0,0,0,0,0,2,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,2,0,2,1,2,0,1],
                [0,0,1,0,1,0,0,2,2,0,0,2,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
                [2,0,0,0,2,0,0,0,0,0,0,0,1,0,2,0,1,1,2,2,0,0,2,0,0,1,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,2,1,0,0],
                [0,2,0,0,0,2,0,1,0,0,0,0,0,1,0,0,0,2,0,2,0,0,1,0,0,0,2,0,2,0,0,0,0,2,2,0,0,0,0,0,0,0,0,2,0,1,0],
                [0,0,1,0,0,2,0,0,0,0,0,0,0,1,0,0,0,2,0,1,0,0,1,1,0,0,0,1,0,0,0,0,0,2,1,0,1,0,2,0,0,0,1,0,0,0,1],
                [0,0,0,0,0,0,0,0,1,0,0,0,2,0,0,0,0,0,0,0,0,0,1,2,1,0,1,0,0,0,2,0,1,0,0,0,0,0,0,0,2,0,0,0,0,1,0],
                [0,0,1,0,0,2,2,0,0,0,0,0,0,0,0,2,0,1,1,0,0,0,0,0,2,0,0,0,0,0,1,0,0,0,2,0,0,0,1,0,2,0,2,0,0,0,0],
                [0,0,0,0,0,2,0,0,0,0,2,2,0,1,0,2,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,2,0,0,2,0,0,2],
                [1,0,1,0,2,2,0,0,2,1,0,2,2,0,0,0,0,0,2,1,0,2,2,0,0,0,0,0,0,1,2,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,2,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
                [0,1,0,0,0,2,0,0,2,1,0,1,0,0,0,0,0,2,0,0,2,0,2,1,0,0,0,0,0,2,0,0,2,2,0,1,0,0,1,1,0,0,0,0,0,2,2],
                [0,1,1,1,1,0,0,0,0,2,0,0,2,2,1,0,0,1,2,2,0,0,0,0,1,0,0,0,0,0,0,0,0,0,2,0,2,0,2,0,0,0,0,0,0,0,2],
                [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,2,0,0,1,0,0,0,0,0,2,0,2,2,0,0,0,0,0,0,0,0,2,0],
                [0,0,0,0,0,0,0,0,0,2,0,0,2,0,0,0,0,0,0,0,0,0,2,0,0,0,1,0,0,2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,1,2,2,0,1,0,2,0,0,2,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,2,0,1,0,0,2,2,0,1,1,0,0,1,1,0],
                [0,0,2,2,1,1,2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,2,1,0,0,0,0,0,0,1,0,0,0,2,0,0,0,0,0,1,2,1,0],
                [0,0,1,0,0,0,0,0,2,0,2,1,0,1,0,0,2,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,1,1,2,0,0,0,0,0,0,0,2],
                [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,1,0,0,0,2,0,0,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0,0,0,0,0,2,0,1,2,1,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,1,0,0,0,0,0,0,0],
                [0,0,0,1,2,0,0,0,0,0,2,2,0,0,0,1,0,1,0,0,0,1,1,0,0,0,1,2,0,0,0,2,0,0,0,0,0,1,0,0,0,0,0,2,0,1,0],
                [0,1,0,0,0,0,0,0,2,0,2,1,1,0,2,2,0,0,0,0,2,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,2,0,0,0,0],
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,1,0,0,0,2,0,2,1,0,2,0,0,0,0,0,0,1,2,0,0,2,1,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0],
                [0,0,0,2,0,1,1,1,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,2,0,2,0,2,2,0,2,2,0,0,1,0,0,2,0,0,0,0,0,1,2,0,0],
                [0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
                [0,0,0,2,2,0,0,2,0,0,0,0,0,0,1,2,2,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,2,0,0,2,0,0,0,1,0,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,2,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,1,0,1,0,0,2,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0]]
        r = sol.shortestDistance(grid)
        print(r)
        assert r == 6267

    unit_test(Solution())
    unit_test(Solution1())
