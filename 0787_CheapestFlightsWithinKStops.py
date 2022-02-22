# There are n cities connected by some number of flights. You are given
# an array flights where flights[i] = [from[i], to[i], price[i]] indicates that
# there is a flight from city from[i] to city to[i] with cost price[i].
# You are also given three integers src, dst, and k, return the cheapest price
# from src to dst with at most k stops. If there is no such route, return -1.

# Constraints:
#   1 <= n <= 100
#   0 <= flights.length <= (n * (n - 1) / 2)
#   flights[i].length == 3
#   0 <= fromi, toi < n
#   fromi != toi
#   1 <= pricei <= 10^4
#   There will not be any multiple flights between two cities.
#   0 <= src, dst, k < n
#   src != dst
from typing import List
import heapq

# BFS...

# Dijkstra's Algorithm
# - modifications:
#   - this is directed graph, one edge for each flights[i]
#   - do not use visited[], instead, add:
#     stops[i]: when visiting i-th node, how many stops away from src;
#     costs[i]: when visiting i-th node, what is the cost so far;
#   - if visiting i-th node again, add them back to minheap if 
#     costs or stops is better.
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for n1, n2, cost in flights:
            graph.setdefault(n1, list()).append((n2, cost))

        minHeap = []
        costs = [2**31] * (n+1)
        stops = [2**31] * (n+1)
        heapq.heappush(minHeap, (0, 0, src))    # [cost, stop, node]
        while len(minHeap) > 0:
            cost, stop, node = heapq.heappop(minHeap)
            if node == dst:
                return cost
            if stop == k + 1:
                continue
            for n1, c1 in graph.get(node, []):
                if cost + c1 < costs[n1]:   # not visited or better cost than last visit
                    stops[n1] = stop + 1
                    costs[n1] = cost + c1
                    heapq.heappush(minHeap, (cost + c1, stop + 1, n1))
                elif stop + 1 < stops[n1]:  # not visited or less stops than last visit
                    stops[n1] = stop + 1
                    costs[n1] = cost + c1
                    heapq.heappush(minHeap, (cost + c1, stop + 1, n1))

        return -1


# Dijkstra's Algorithm
# !!! Time Limit Exceeded, dead loop for DCG (Directed Cyclic Graph) !!!
# - modifications:
#   - this is directed graph, one edge for each flights[i]
#   - when adding adjacent nodes, check for dst, and keep the min price,
#     if the stops is within the limit.
#   - do not add dst to minHeap.
#   - do not use visited[], some nodes will be added to minHeap multiple times
#     due to multiple routes, no problem because this is a directed graph.
#   - exit only when minHeap is exhausted.
class Solution1:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for n1, n2, price in flights:
            graph.setdefault(n1, list()).append((n2, price))

        res = 2**31
        minHeap = []
        heapq.heappush(minHeap, (0, 0, src))    # [price, stops, node]
        while len(minHeap) > 0:
            price, stops, node = heapq.heappop(minHeap)
            for n1, p1 in graph.get(node, []):
                if n1 == dst:
                    if stops <= k:
                        res = min(res, price + p1)
                else:
                    heapq.heappush(minHeap, (price + p1, stops + 1, n1))

        return res if res < 2**31 else -1


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.findCheapestPrice(n=5, flights=[[1, 2, 10], [2, 0, 7], [1, 3, 8], [4, 0, 10],
                                                [3, 4, 2], [4, 2, 10], [0, 3, 3], [3, 1, 6], 
                                                [2, 4, 5]],
                                  src=0, dst=4, k=1)
        print(r)
        assert r == 5

        r = sol.findCheapestPrice(n=11, flights=[[0, 3, 3], [3, 4, 3], [4, 1, 3], [0, 5, 1],
                                                 [5, 1, 100], [0, 6, 2], [6, 1, 100], [0, 7, 1],
                                                 [7, 8, 1], [8, 9, 1], [9, 1, 1], [1, 10, 1],
                                                 [10, 2, 1], [1, 2, 100]],
                                  src=0, dst=2, k=4)
        print(r)
        assert r == 11

        r = sol.findCheapestPrice(n=4, flights=[[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]],
                                  src=0, dst=3, k=1)
        print(r)
        assert r == 6

        r = sol.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]],
                                  src=0, dst=2, k=1)
        print(r)
        assert r == 200

        r = sol.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]],
                                  src=0, dst=2, k=0)
        print(r)
        assert r == 500

    unitTest(Solution())
    # unitTest(Solution1())   # dead loop for DCG (Directed Cyclic Graph)
