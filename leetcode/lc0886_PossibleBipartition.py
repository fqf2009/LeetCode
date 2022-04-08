# We want to split a group of n people (labeled from 1 to n) into
# two groups of any size. Each person may dislike some other people,
# and they should not go into the same group.

# Given the integer n and the array dislikes where dislikes[i] = [ai, bi]
# indicates that the person labeled ai does not like the person labeled bi,
# return true if it is possible to split everyone into two groups in this way.

# Constraints:
#   1 <= n <= 2000
#   0 <= dislikes.length <= 10^4
#   dislikes[i].length == 2
#   1 <= dislikes[i][j] <= n
#   ai < bi
#   All the pairs of dislikes are unique.
from typing import List, Optional
from collections import deque


# BFS - T/S: O(n), O(n)
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = {}
        for i, j in dislikes:
            graph.setdefault(i, list()).append(j)
            graph.setdefault(j, list()).append(i)

        que = deque()
        visited = {x: 0 for x in graph.keys()}  # either dict or list is ok
        for x, c in visited.items():
            if c == 0:
                que.append((x, 1))
                while len(que) > 0:
                    y, c = que.popleft()
                    visited[y] = c
                    for z in graph[y]:
                        if visited[z] == c:
                            return False
                        if visited[z] == 0:
                            que.append((z, 3-c))
        return True


# DFS - T/S: O(n), O(n)
# - build a graph, node is index of people, edge is dislike relation
# - DFS for visit each node, color it with one color, and visit neighbour,
#   to color it with another color, it the neighbour already has a
#   conflicting color, return False.
class Solution1:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfsVisit(x: int, c: int) -> bool:
            visited[x] = c
            for y in graph[x]:
                if visited[y] == c:
                    return False
                if visited[y] == 0:
                    if not dfsVisit(y, 3-c):
                        return False
            return True

        graph = {}
        for i, j in dislikes:
            graph.setdefault(i, list()).append(j)
            graph.setdefault(j, list()).append(i)

        visited = [0] * (n + 1)
        for i in range(1, n+1):
            if visited[i] == 0 and i in graph:
                if not dfsVisit(i, 1):
                    return False

        return True


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.possibleBipartition(n=4, dislikes=[[1, 2], [1, 3], [2, 4]])
        print(r)
        assert r == True

        r = sol.possibleBipartition(3, dislikes=[[1, 2], [1, 3], [2, 3]])
        print(r)
        assert r == False

        r = sol.possibleBipartition(n=5, dislikes=[[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]])
        print(r)
        assert r == False

    unitTest(Solution())
    unitTest(Solution1())
