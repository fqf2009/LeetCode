from typing import List
from collections import defaultdict

# There are a total of numCourses courses you have to take, labeled 
# from 0 to numCourses - 1. You are given an array prerequisites where 
# prerequisites[i] = [ai, bi] indicates that you must take course bi 
# first if you want to take course ai. For example, the pair [0, 1], 
# indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# DFS (Depth First Search) to detect cycle in DG (Directed Graph)
# Time coplexity: O(n), Space complexity: O(n)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfsCycle(node) -> bool:
            if node not in visit or visit[node] == 1:
                return False
            if visit[node] == -1:
                return True
            visit[node] = -1
            for x in graph[node]:
                if dfsCycle(x):
                    return True
            visit[node] = 1
            return False

        graph = defaultdict(set)
        for req in prerequisites:
            graph[req[0]].add(req[1])

        # 0: not visited, 1: visited, -1: in DFS searching stack
        visit = {x: 0 for x in graph.keys()}
        for node in visit:
            if dfsCycle(node):
                return False

        return True


# BFS (Breadth First Search) to detect cycle in DG (Directed Graph)
class Solution1:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        indegrees = defaultdict(int)
        for req in prerequisites:
            indegrees[req[1]] += 1
            graph[req[0]].add(req[1])

        toVisit = set(graph.keys()) - set(indegrees.keys())
        while len(toVisit) > 0:
            node = toVisit.pop()
            for x in graph[node]:
                indegrees[x] -= 1
                if indegrees[x] == 0:
                    toVisit.add(x)
                    del indegrees[x]

        return len(indegrees) == 0


if __name__ == '__main__':
    sol = Solution()

    r = sol.canFinish(numCourses=2, prerequisites=[[1, 0]])
    print(r)
    assert(r == True)

    r = sol.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]])
    print(r)
    assert(r == False)
