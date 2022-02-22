# Dijkstra's algorithm to get longest (not shortest) path in undirected graph
# Complexity: (e+n)*log(n), where e is edge count, n is vertex count

# Difference between Dijkstra's algorithm and Prim's algorithm (LeetCode 1584):
# - Both have the similar complexity.
# - Both need to store info of the known set of nodes (from edges actually), 
#   then retrieve the lowest priority value item, and then use it to visit
#   the un-visited set of nodes. So both can use PriorityQueue to save storing 
#   and retrieving time: From N to log(N), where N is queue length.
# - Both keep a set of visited nodes to avoid re-visiting.
# - Dijkstra algorithm keeps the distance (cost) from source node to each 
#   queued node. Each item it adds an edge (node1, node2) into queue, it adds 
#   the distince of source to node1, with the distance of node1 to node2. When
#   it pop the edge from queue, it gets the node with the lowest cost by far.
# - Prim's algorithm keeps the distance of node1 to node2 when adding the edge 
#   to the queue. The meaning is from the set of visited nodes to the set of 
#   unvisited nodes, pick shortest edge for next visiting.

# You are given an undirected weighted graph of n nodes (0-indexed), represented
# by an edge list where edges[i] = [a, b] is an undirected edge connecting the
# nodes a and b with a probability of success of traversing that edge succProb[i].
# Given two nodes start and end, find the path with the maximum probability of
# success to go from start to end and return its success probability. If there is 
# no path from start to end, return 0. Your answer will be accepted if it differs 
# from the correct answer by at most 1e-5.
from typing import List
import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = {}
        for i in range(len(edges)):
            node1, node2 = tuple(edges[i])
            graph.setdefault(node1, set()).add((node2, succProb[i]))
            graph.setdefault(node2, set()).add((node1, succProb[i]))

        prob = []
        visited = set()
        # use negative priority value because heapq is min heap, i.e., pop method returns the smallest item
        heapq.heappush(prob, [-1, start])
        while len(prob) > 0:
            p0, node  = tuple(heapq.heappop(prob))
            if node == end:
                return -p0
            if node not in visited:
                visited.add(node)
                for neighbor, p1 in graph.get(node, []):
                    heapq.heappush(prob, [p0 * p1, neighbor])

        return 0.0


if __name__ == '__main__':
    sol = Solution()

    n = 500
    edges = [[193,229],[133,212],[224,465]]
    succProb = [0.91,0.78,0.64]
    start = 4
    end = 364
    r = sol.maxProbability(n, edges, succProb, start, end)
    print(r)
    assert(r == 0.0)

    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.2]
    start = 0
    end = 2
    r = sol.maxProbability(n, edges, succProb, start, end)
    print(r)
    assert(r == 0.25)
            
    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.3]
    start = 0
    end = 2
    r = sol.maxProbability(n, edges, succProb, start, end)
    print(r)
    assert(r == 0.3)
    
    n = 3
    edges = [[0,1]]
    succProb = [0.5]
    start = 0
    end = 2
    r = sol.maxProbability(n, edges, succProb, start, end)
    print(r)
    assert(r == 0)
