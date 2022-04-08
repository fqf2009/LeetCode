# You are given an m x n grid rooms initialized with these three possible values.
# * -1 A wall or an obstacle.
# * 0 A gate.
# * INF Infinity means an empty room. We use the value 231 - 1 = 2147483647
#   to represent INF as you may assume that the distance to a gate is
#   less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is
# impossible to reach a gate, it should be filled with INF.
# Constraints:
#   m == rooms.length
#   n == rooms[i].length
#   1 <= m, n <= 250
#   rooms[i][j] is -1, 0, or 2^31 - 1.
from collections import deque
from typing import List


# BFS - T/S: O(m*n), O(1)
# - Start searching from all gates at the same time
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROOM = 2**31 - 1
        m, n = len(rooms), len(rooms[0])
        dq = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    dq.append((i, j, 0))
        while dq:
            i, j, d = dq.popleft()
            for di, dj in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and rooms[x][y] == ROOM:
                    rooms[x][y] = d + 1
                    dq.append((x, y, d+1))


# DFS - T/S: O(m*n), O(1) - Wrong
# !!! Note for the edge case, e.g., see the test case 1,
#     at up-right corner, the distance is supposed to be 2:
#           ...-1,0,1,3],
#           ... -1,-1,2],
#           ...     0,1],
#           ...      -1]
#     The reason is when cell(0,12) is visited, it forces cell(0,13)
#     to search downward, but block the left side.
class Solution1:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROOM = 2**31 - 1
        m, n = len(rooms), len(rooms[0])

        def dfs_visit(i, j):
            if rooms[i][j] < ROOM:
                return rooms[i][j]
            rooms[i][j] = -ROOM  # temporarily mark it, to avoid endless loop
            distance = ROOM
            for di, dj in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n:
                    neib_distance = min(distance, dfs_visit(x, y))
                    if neib_distance >= 0:
                        distance = min(distance, neib_distance + 1)

            rooms[i][j] = distance  # set at post-order
            return distance

        for i in range(m):
            for j in range(n):
                dfs_visit(i, j)


if __name__ == "__main__":

    def unit_test(sol):
        ROOM = 2**31 - 1
        rooms = [
            [0, ROOM, ROOM, 0, -1, -1, 0, 0, 0, -1, -1, 0, ROOM, ROOM],
            [ROOM, -1, ROOM, -1, ROOM, 0, -1, ROOM, -1, ROOM, ROOM, -1, -1, ROOM],
            [0, 0, -1, ROOM, -1, ROOM, -1, -1, ROOM, 0, 0, ROOM, 0, ROOM],
            [-1, 0, ROOM, -1, 0, 0, -1, ROOM, 0, ROOM, 0, -1, 0, -1],
        ]
        sol.wallsAndGates(rooms)
        print(rooms)
        assert rooms == [
            [0, 1, 1, 0, -1, -1, 0, 0, 0, -1, -1, 0, 1, 2],
            [1, -1, 2, -1, 1, 0, -1, 1, -1, 1, 1, -1, -1, 2],
            [0, 0, -1, ROOM, -1, 1, -1, -1, 1, 0, 0, 1, 0, 1],
            [-1, 0, 1, -1, 0, 0, -1, 1, 0, 1, 0, -1, 0, -1],
        ]

        rooms = [
            [ROOM, -1, 0, ROOM],
            [ROOM, ROOM, ROOM, -1],
            [ROOM, -1, ROOM, -1],
            [0, -1, ROOM, ROOM],
        ]
        sol.wallsAndGates(rooms)
        print(rooms)
        assert rooms == [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]

        rooms = [[-1]]
        sol.wallsAndGates(rooms)
        print(rooms)
        assert rooms == [[-1]]

    unit_test(Solution())
