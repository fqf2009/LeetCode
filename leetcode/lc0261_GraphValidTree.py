# You have a graph of n nodes labeled from 0 to n - 1. You are given 
# an integer n and a list of edges where edges[i] = [ai, bi] indicates 
# that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, 
# and false otherwise.

# Constraints:
#   1 <= n <= 2000
#   0 <= edges.length <= 5000
#   edges[i].length == 2
#   0 <= ai, bi < n
#   ai != bi
#   There are no self-loops or repeated edges.
from typing import List
from collections import deque


# Graph Theory: For the graph to be a valid tree, it must have exactly
#   n - 1 edges. Any less, and it can't possibly be fully connected. 
#   Any more, and it has to contain cycles. Additionally, if the graph
#   is fully connected and contains exactly n - 1 edges, it can't possibly 
#   contain a cycle, and therefore must be a tree!
# - check nodes == n, and edges = n-1
# - then try to use BFS/DFS from any node to visit the entire tree/graph
# - use stack to implement iterative DFS!!!
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1: return True
        graph = {}
        for a, b in edges:
            graph.setdefault(a, set()).add(b)
            graph.setdefault(b, set()).add(a)

        if len(graph) < n or len(edges) != n - 1: return False

        stack = [0]
        visited = set()
        while len(stack) > 0:
            x = stack.pop()
            visited.add(x)
            for y in graph[x]:
                if y not in visited:
                    stack.append(y)
        
        return len(visited) == n


# Union Find: O(n), O(n)
# - 3 conditions:
#   - edges == n-1
#   - all nodes are conected
#   - only one network (graph)
class Solution0:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1: return True
        if not len(edges) == n-1: return False

        uf = {}
        def find(x):
            if uf.setdefault(x, x) != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        for x, y in edges:
            uf[find(x)] = find(y)

        return len(uf) == n and len(set(find(x) for x in uf.keys())) == 1


# DFS, but avoid going backward, to see if there is circle
class Solution1:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1: return True
        graph = {}
        for a, b in edges:
            graph.setdefault(a, set()).add(b)
            graph.setdefault(b, set()).add(a)

        if len(graph) < n: return False
        stack = [(0, -1)]    # (node, parent)
        visited = set()
        while len(stack) > 0:
            x, p = stack.pop()
            visited.add(x)
            for y in graph[x]:
                if y != p:
                    if y in visited:        # circle
                        return False
                    stack.append((y, x))    # type:ignore

        return len(visited) == n


# Analysis: O(N+E)
# - remove leaf node one by one, until no leaf left.
# - if there is still node in graph, it is not a tree.
class Solution2:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1: return True
        graph = {}
        for a, b in edges:
            graph.setdefault(a, set()).add(b)
            graph.setdefault(b, set()).add(a)

        if len(graph) < n: return False
        que = deque(x for x, y in graph.items() if len(y) == 1)
        while len(que) > 0:
            x = que.popleft()
            y = list(graph[x])[0]
            del graph[x]
            graph[y].remove(x)
            if len(graph[y]) == 0:
                return len(graph) == 1  # only one root is allowed
            elif len(graph[y]) == 1:
                que.append(y)

        return False


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.validTree(n = 5, edges = [[0,1],[0,2],[0,3],[1,4]])
        print(r)
        assert r == True

        r = sol.validTree(n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]])
        print(r)
        assert r == False
        
        r = sol.validTree(n = 3, edges = [[1, 0]])
        print(r)
        assert r == False

        r = sol.validTree(n = 1, edges = [])
        print(r)
        assert r == True

    unitTest(Solution())
    unitTest(Solution0())
    unitTest(Solution1())
    unitTest(Solution2())
