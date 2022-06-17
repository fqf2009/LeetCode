# There are a total of numCourses courses you have to take, labeled 
# from 0 to numCourses - 1. You are given an array prerequisites where 
# prerequisites[i] = [ai, bi] indicates that you must take course bi 
# first if you want to take course ai. For example, the pair [0, 1], 
# indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. 
# If there are many valid answers, return any of them. If it is 
# impossible to finish all courses, return an empty array.

# Constraints:
#   1 <= numCourses <= 2000
#   0 <= prerequisites.length <= numCourses * (numCourses - 1)
#   prerequisites[i].length == 2
#   0 <= ai, bi < numCourses
#   ai != bi
#   All the pairs [ai, bi] are distinct.
from typing import List
from collections import defaultdict


# Topology Sort using DFS - sort DG (Directed Graph) and detect cycle
# Time:  O(V+E), where V is number of vertices (vertex)
# Space: O(V+E)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfsVisitNoCycle(node) -> bool:
            if visited[node] == 1:  # previously visited in another search
                return True
            if visited[node] == -1: # previously visited in this search, cycle detected
                return False
            visited[node] = -1      # mark visiting in this search
            for x in graph[node]:
                if not dfsVisitNoCycle(x):
                    return False
            visited[node] = 1       # mark visited
            visitOrder.append(node)
            return True

        graph = defaultdict(set)
        for course, prereq in prerequisites:    # O(E)
            graph[course].add(prereq)

        # 0: not visited, 1: visited, -1: in DFS searching stack
        visited = [0] * numCourses
        visitOrder = []
        for i in range(len(visited)):           # O(V)
            if visited[i] == 0 and not dfsVisitNoCycle(i):
                return []

        return visitOrder


# Topology Sort using BFS & Node Indegree - sort DG (Directed Graph) and detect cycle
# Time:  O(V+E), where V is number of vertices (vertex)
# Space: O(V+E)
class Solution1:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        indegree = {}
        for course, prereq in prerequisites:    # O(E)
            graph[course].add(prereq)
            indegree.setdefault(prereq, 0)
            indegree[prereq] += 1

        toVisit = set(range(numCourses)) - set(indegree.keys())
        visitOrder = []
        while len(toVisit) > 0:                 # O(V)
            node = toVisit.pop()
            visitOrder.append(node)
            for x in graph[node]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    toVisit.add(x)
                    del indegree[x]

        if len(indegree) != 0:
            return []
        return visitOrder[::-1]


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.findOrder(numCourses=2, prerequisites=[[1, 0]])
        print(r)
        assert r == [0,1]

        r = sol.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])
        print(r)
        assert r == [0,1,2,3] or r == [0,2,1,3]

    unitTest(Solution())
    unitTest(Solution1())
