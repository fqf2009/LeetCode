from typing import List, DefaultDict
import itertools

# Tarjan's strongly connected components algorithm
# Note it is for Directed Graph in wikipedia, but here it is for Undirected Graph

# There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a
# network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can
# reach other servers directly or indirectly through the network. A critical connection is a connection that,
# if removed, will make some servers unable to reach some other server.
# Return all critical connections in the network in any order.

# Use backtracking instead of recursion
# Pre-condition: all nodes are connected
# Complexity: O(n) (visit each node: O(n), update past visited nodes' lowlink: O(n))
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def firstUnusedEdge(node):
            for n1, edge in graph[node].items():
                if not edge:
                    return n1
            return None

        def markZone(lowlinkVal: int):
            for i in reversed(range(len(visitStack))):
                if lowlink[visitStack[i]] > lowlinkVal:
                    lowlink[visitStack[i]] = lowlinkVal

        graph = DefaultDict(dict)
        for conn in connections:
            n1, n2 = tuple(conn)
            graph[n1][n2] = False  # False means the edge is not used yet
            graph[n2][n1] = False

        bridge = []
        lowlink = [-1] * n  # -1 means not visited yet
        # sequence to tag each new node, unless later it encounter a lower lowlink
        counter = itertools.count() 
        # initially set by sequence, later all nodes in same zone with second
        # visit path get lowest lowlink among them
        lowlink[0] = next(counter)
        # used to find previous visited higher lowlink nodes, when a lower lowlink node is encounted
        visitStack = []
        visitStack.append(0)
        while len(visitStack) > 0:
            node1 = visitStack[-1]  # peek stack
            node2 = firstUnusedEdge(node1)
            if node2 != None:
                # print((node1, node2)) # for debugging
                graph[node1][node2] = True  # Edge is now used
                graph[node2][node1] = True
                if lowlink[node2] == -1:
                    lowlink[node2] = next(counter)
                    visitStack.append(node2)
                elif lowlink[node1] > lowlink[node2]:
                    lowlink[node1] = lowlink[node2]
                    for i in reversed(range(len(visitStack))):
                        if lowlink[visitStack[i]] > lowlink[node2]:
                            lowlink[visitStack[i]] = lowlink[node2]
            else:
                visitStack.pop()    # node1 get poped
                if len(visitStack) > 0:
                    node0 = visitStack[-1]
                    if lowlink[node0] > lowlink[node1]:
                        markZone(lowlink[node1])          # move to here to reduce the times of revisiting history
                    elif lowlink[node0] < lowlink[node1]: # different lowlink means bridge between critical zones
                        bridge.append(sorted([node0, node1]))

        # print(lowlink)    # for debugging
        return bridge


# Use backtracking instead of recursion
# Pre-condition: all nodes are connected
class Solution1:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def firstUnusedEdge(node):
            for n1, edge in graph[node].items():
                if not edge:
                    return n1
            return None

        graph = DefaultDict(dict)
        for conn in connections:
            n1, n2 = tuple(conn)
            graph[n1][n2] = False  # False means the edge is not used yet
            graph[n2][n1] = False

        bridge = []
        lowlink = [-1] * n  # -1 means not visited
        counter = itertools.count()
        lowlink[0] = next(counter)
        visitStack = []  # when lower lowlink value is found, use stack to find previous nodes with higher lowlink
        visitStack.append(0)
        while len(visitStack) > 0:
            node1 = visitStack[-1]  # peek stack
            node2 = firstUnusedEdge(node1)
            if node2 != None:
                # print((node1, node2)) # for debugging
                graph[node1][node2] = True
                graph[node2][node1] = True
                if lowlink[node2] == -1:
                    lowlink[node2] = next(counter)
                    visitStack.append(node2)
                elif lowlink[node1] > lowlink[node2]:
                    for i in reversed(range(len(visitStack))):
                        if lowlink[visitStack[i]] <= lowlink[node2]:
                            break
                        lowlink[visitStack[i]] = lowlink[node2]
            else:
                visitStack.pop()
                if len(visitStack) > 0:
                    node0 = visitStack[-1]
                    if lowlink[node0] != lowlink[node1]:
                        bridge.append(sorted([node0, node1]))

        # print(lowlink)    # for debugging
        return bridge


# !!! Error 1: Because if ever a decendent node find a ancester with lower lowlink value, its parent
#              and ancestry nodes only get their lowlink updated when dfsTarjan returns. (not immediately
#              broadcasts to all nodes in the stack, up to new found visited lower lowlink node.) So next
#              time when another node touch any node in this previous chain, it does not get appropriate
#              lowlink value.
# !!! Error 2: n coule be 50000, which is much larger than python's default recursion limit (3000)
class Solution2:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfsTarjan(node: int):
            lowlink[node] = next(counter)
            for n1, edge in graph[node].items():
                if not edge:  # not used yet
                    print((node, n1))
                    graph[node][n1] = True
                    graph[n1][node] = True
                    if lowlink[n1] == -1:  # not visited yet
                        dfsTarjan(n1)
                        if lowlink[node] < lowlink[n1]:
                            bridge.append(sorted([node, n1]))
                    lowlink[node] = min(lowlink[node], lowlink[n1])

            return

        graph = DefaultDict(dict)
        for conn in connections:
            n1, n2 = tuple(conn)
            graph[n1][n2] = False  # False means the edge is not used yet
            graph[n2][n1] = False

        # sys.setrecursionlimit(100000) # no use
        bridge = []
        lowlink = [-1] * n  # -1 means not visited
        counter = itertools.count()
        for i in range(n):
            if lowlink[i] == -1:
                dfsTarjan(i)

        print(lowlink)
        return bridge


if __name__ == "__main__":
    sol = Solution()

    n = 4
    connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
    r = sol.criticalConnections(n, connections)
    print(r)
    assert sorted(r) == [[1, 3]]

    n = 2
    connections = [[0, 1]]
    r = sol.criticalConnections(n, connections)
    print(r)
    assert sorted(r) == [[0, 1]]

    n = 10
    connections = [[5, 0], [2, 1], [3, 2], [2, 5], [4, 3], [4, 5], [5, 1], [6, 1], [7, 6], [8, 6], [9, 8], [6, 9]]
    r = sol.criticalConnections(n, connections)
    print(r)
    assert sorted(r) == [[0, 5], [1, 6], [6, 7]]

    n = 10
    connections = [
        [5, 0],
        [2, 1],
        [3, 2],
        [2, 5],
        [4, 3],
        [4, 5],
        [5, 1],
        [6, 1],
        [7, 6],
        [8, 6],
        [9, 8],
        [6, 9],
        [0, 7],
    ]
    r = sol.criticalConnections(n, connections)
    print(r)
    assert sorted(r) == []
