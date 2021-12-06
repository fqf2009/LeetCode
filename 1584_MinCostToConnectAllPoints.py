from typing import List
import heapq

# You are given an array points representing integer coordinates of some points on a 2D-plane,
# where points[i] = [xi, yi]. The cost of connecting two points [xi, yi] and [xj, yj] is the
# manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute
# value of val. Return the minimum cost to make all points connected. All points are connected
# if there is exactly one simple path between any two points.

# Use Prim's algorithm to construct a Minimum Spanning Tree (MST)

# Success - Only improve a little when avoiding unnecessary heapq in graph itself
# Reason - The graph is so dense. every point can connect other points, so the edge count is n*(n-1)/2.
#          The max heapq len could be edge count, so the each push effort is log(n^2), i.e., 2*log(n).
#          Each eage needs to be pushed, so the time complexity is O((n^2)*log(n)) .
# Runtime: 6440 ms, faster than 7.76% of Python3 online submissions for Min Cost to Connect All Points.
# Memory Usage: 199.5 MB, less than 5.03% of Python3 online submissions for Min Cost to Connect All Points.
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0
        adjacency = {}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                if p1 != p2:
                    distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                    adjacency.setdefault(tuple(p1), []).append((distance, tuple(p2)))
                    adjacency.setdefault(tuple(p2), []).append((distance, tuple(p1)))

        visited = set()
        mst = []
        heapq.heappush(mst, (0, tuple(points[0])))
        cost = 0
        while len(mst) > 0:
            d1, p1 = heapq.heappop(mst)
            if p1 not in visited:
                visited.add(p1)
                cost += d1
                for d2, p2 in adjacency.get(p1, []):
                    if p2 not in visited:
                        heapq.heappush(mst, (d2, p2))

        return cost


# Initial version
# Success - But performance still needs further improvement
# Runtime: 7700 ms, faster than 5.02% of Python3 online submissions for Min Cost to Connect All Points.
# Memory Usage: 183 MB, less than 5.22% of Python3 online submissions for Min Cost to Connect All Points.
class Solution1:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0
        adjacency = {}
        for p1 in points:
            for p2 in points:
                if p1 != p2:
                    distances = adjacency.setdefault(tuple(p1), [])
                    # unnecessay to use heapq (priority queue) here!!!
                    heapq.heappush(distances, (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]), tuple(p2)))
        
        visited = set()
        mst = []
        heapq.heappush(mst, (0, tuple(points[0])))
        cost = 0
        while len(mst) > 0:
            d1, p1 = heapq.heappop(mst)
            if p1 in visited:
                continue
            visited.add(p1)
            cost += d1
            neighbors = adjacency[p1]
            while len(neighbors) > 0:
                d2, p2  = heapq.heappop(neighbors)
                if p2 in visited:
                    continue
                heapq.heappush(mst, (d2, p2))

        return cost


if __name__ == '__main__':
    sol = Solution()

    r = sol.minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]])
    print(r)
    assert(r == 20)

    r = sol.minCostConnectPoints(points = [[3,12],[-2,5],[-4,1]])
    print(r)
    assert(r == 18)

    r = sol.minCostConnectPoints(points = [[0,0],[1,1],[1,0],[-1,1]])
    print(r)
    assert(r == 4)

    r = sol.minCostConnectPoints(points = [[-1000000,-1000000],[1000000,1000000]])
    print(r)
    assert(r == 4000000)

    r = sol.minCostConnectPoints(points = [[0,0]])
    print(r)
    assert(r == 0)
