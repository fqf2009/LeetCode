from typing import List
from collections import defaultdict

# There are a total of numCourses courses you have to take, labeled 
# from 0 to numCourses - 1. You are given an array prerequisites where 
# prerequisites[i] = [ai, bi] indicates that you must take course bi 
# first if you want to take course ai. For example, the pair [0, 1], 
# indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. 
# If there are many valid answers, return any of them. If it is 
# impossible to finish all courses, return an empty array.

# DFS (Depth First Search) to sort DG (Directed Graph) and detect cycle
class Solution1:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfsVisitNoCycle(node) -> bool:
            if visited[node] == 1:
                return True
            if visited[node] == -1:
                return False
            visited[node] = -1
            for x in graph[node]:
                if not dfsVisitNoCycle(x):
                    return False
            visited[node] = 1
            visitOrder.append(node)
            return True

        graph = defaultdict(set)
        for req in prerequisites:
            graph[req[0]].add(req[1])

        # 0: not visited, 1: visited, -1: in DFS searching stack
        visited = [0] * numCourses
        visitOrder = []
        for i in range(len(visited)):
            if not dfsVisitNoCycle(i):
                return []

        return visitOrder


# BFS (Breadth First Search) to sort DG (Directed Graph) and detect cycle
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        indegree = {}
        for req in prerequisites:
            indegree.setdefault(req[1], 0)
            indegree[req[1]] += 1
            graph[req[0]].add(req[1])

        toVisit = set(range(numCourses)) - set(indegree.keys())
        visitOrder = []
        while len(toVisit) > 0:
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
    sol = Solution()

    r = sol.findOrder(numCourses=2, prerequisites=[[1, 0]])
    print(r)
    assert(r == [0,1])

    r = sol.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])
    print(r)
    assert(r == [0,1,2,3] or r == [0,2,1,3])


        