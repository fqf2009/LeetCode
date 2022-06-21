# There are n houses in a village. We want to supply water for
# all the houses by building wells and laying pipes.
# For each house i, we can either build a well inside it directly
# with cost wells[i - 1] (note the -1 due to 0-indexing), or pipe
# in water from another well to it. The costs to lay pipes between
# houses are given by the array pipes where each
# pipes[j] = [house1j, house2j, costj] represents the cost to connect
# house1j and house2j together using a pipe. Connections are
# bidirectional, and there could be multiple valid connections
# between the same two houses with different costs.
# Return the minimum total cost to supply water to all houses.
# Constraints:
#   2 <= n <= 10^4
#   wells.length == n
#   0 <= wells[i] <= 10^5
#   1 <= pipes.length <= 10^4
#   pipes[j].length == 3
#   1 <= house1j, house2j <= n
#   0 <= costj <= 10^5
#   house1j != house2j
from collections import defaultdict, deque
import heapq
from typing import List


# MST (Minimus Spanning Tree) - Prim's Algorithm
# - Build a graph (undirected or bidirectional), each house is a node,
#   pipe cost is edge weight;
# - Use one virtual node representing all wells in each house,
#   the edge weight from this node to other nodes (houses) is
#   the well cost at each house;
# - even if all house are connected, sometimes it is better to build
#   more than one wells, due to well cost is lower than pipe cost;
# - if there are disconnected graph (forest), the virtual node magically
#   connect them; meaning different graphs have to connect to different
#   wells.
# - the reason the check visited at two places:
#   - the first place is a must, because multiple edges to the same
#     node could be added.
#   - second place: optional, just reduce some unnecessay overhead
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        graph = defaultdict(list)
        for h1, h2, cost in pipes:
            graph[h1].append((h2, cost))
            graph[h2].append((h1, cost))

        for i, cost in enumerate(wells):
            graph[i+1].append((0, cost))  # 0 is virtual node for wells
            graph[0].append((i+1, cost))

        hq = [(0, 0)]  # cost, next_house
        heapq.heapify(hq)
        visited = set()
        res = 0
        while hq:
            cost, h1 = heapq.heappop(hq)
            if h1 in visited: continue      # need check!!!
            res += cost
            visited.add(h1)
            for h2, cost in graph[h1]:
                if h2 not in visited:       # could remove, just waste some memory
                    heapq.heappush(hq, (cost, h2))

        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.minCostToSupplyWater(3, wells=[1, 2, 2], pipes=[[1, 2, 1], [2, 3, 1]])
        print(r)
        assert r == 3

        r = sol.minCostToSupplyWater(2, wells=[1, 1], pipes=[[1, 2, 1], [1, 2, 2]])
        print(r)
        assert r == 2

    unit_test(Solution())
