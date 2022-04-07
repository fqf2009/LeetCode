# There are a total of numCourses courses you have to take, labeled 
# from 0 to numCourses - 1. You are given an array prerequisites where 
# prerequisites[i] = [ai, bi] indicates that you must take course bi 
# first if you want to take course ai. For example, the pair [0, 1], 
# indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
# Constraints:
#   1 <= numCourses <= 10^5
#   0 <= prerequisites.length <= 5000
#   prerequisites[i].length == 2
#   0 <= ai, bi < numCourses
#   All the pairs prerequisites[i] are unique.

from typing import List
from collections import defaultdict


# DFS to detect cycle in DG (Directed Graph)
# - T/S: O(V + E), O(V + E)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs_has_cycle(node) -> bool:
            if node not in visited or visited[node] == 1:
                return False
            if visited[node] == -1:
                return True
            visited[node] = -1
            for x in graph[node]:
                if dfs_has_cycle(x):
                    return True
            visited[node] = 1       # mark visited in post-order
            return False

        graph = defaultdict(set)
        for course, preq in prerequisites:
            graph[course].add(preq)

        # 0: not visited, 1: visited, -1: temporarily mark for this DFS visit
        visited = {x: 0 for x in graph.keys()}
        for node in visited:
            if dfs_has_cycle(node):
                return False

        return True


# Topology Sort + BFS: to detect cycle in DG (Directed Graph)
# - T/S: O(V + E), O(V + E)
class Solution1:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        indegree = defaultdict(int)
        for course, preq in prerequisites:
            indegree[preq] += 1
            graph[course].add(preq)

        to_visit = set(graph.keys()) - set(indegree.keys())
        while to_visit:
            node = to_visit.pop()
            for x in graph[node]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    to_visit.add(x)
                    del indegree[x]

        return len(indegree) == 0


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.canFinish(numCourses=2, prerequisites=[[1, 0]])
        print(r)
        assert r == True

        r = sol.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]])
        print(r)
        assert r == False

        r = sol.canFinish(numCourses=2, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]])
        print(r)
        assert r == True

    unit_test(Solution())
    unit_test(Solution1())
