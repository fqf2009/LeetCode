# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find
# all possible paths from node 0 to node n - 1 and return them in any order.
# The graph is given as follows: graph[i] is a list of all nodes you can visit 
# from node i (i.e., there is a directed edge from node i to node graph[i][j]).

# Constraints:
#   n == graph.length
#   2 <= n <= 15
#   0 <= graph[i][j] < n
#   graph[i][j] != i (i.e., there will be no self-loops).
#   All the elements of graph[i] are unique.
#   The input graph is guaranteed to be a DAG.
from typing import List


# DFS + Recursion
# - DAG, no circle, no need to mark visited
# - creating new list each time, so no need to use stack
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def findPath(start, end, path: List):
            if start == end:
                pathes.append(path)
            else:
                for node in graph[start]:
                    findPath(node, end, path + [node])

        pathes = []
        findPath(0, len(graph) - 1, [0])
        return pathes


# Use stack and recursion to performe DFS (depth first search)
class Solution1:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def findPath(start, end):
            if start == end:
                res.append(path.copy())
                return

            for node in graph[start]:
                path.append(node)
                findPath(node, end)
                path.pop()

            return

        path = [0]
        res = []
        findPath(0, len(graph) - 1)
        return res

if __name__ == '__main__':
    def unitTest(sol):
        r = sol.allPathsSourceTarget(graph=[[1, 2], [3], [3], []])
        print(r)
        assert(r == [[0, 1, 3], [0, 2, 3]])

        r = sol.allPathsSourceTarget(graph=[[4, 3, 1], [3, 2, 4], [3], [4], []])
        print(r)
        assert(r == [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]])

        r = sol.allPathsSourceTarget(graph=[[1], []])
        print(r)
        assert(r == [[0, 1]])

        r = sol.allPathsSourceTarget(graph=[[1, 2, 3], [2], [3], []])
        print(r)
        assert(r == [[0, 1, 2, 3], [0, 2, 3], [0, 3]])

        r = sol.allPathsSourceTarget(graph=[[1, 3], [2], [3], []])
        print(r)
        assert(r == [[0, 1, 2, 3], [0, 3]])

    unitTest(Solution())
