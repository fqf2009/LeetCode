# You have k servers numbered from 0 to k-1 that are being used to handle
# multiple requests simultaneously. Each server has infinite computational
# capacity but cannot handle more than one request at a time. The requests
# are assigned to servers according to a specific algorithm:
#  - The ith (0-indexed) request arrives.
#  - If all servers are busy, the request is dropped (not handled at all).
#  - If the (i % k)th server is available, assign the request to that server.
#  - Otherwise, assign the request to the next available server (wrapping
#    around the list of servers and starting from 0 if necessary). For
#    example, if the ith server is busy, try to assign the request to the
#    (i+1)th server, then the (i+2)th server, and so on.

# You are given a strictly increasing array arrival of positive integers,
# where arrival[i] represents the arrival time of the ith request, and
# another array load, where load[i] represents the load of the ith request
# (the time it takes to complete). Your goal is to find the busiest
# server(s). A server is considered busiest if it handled the most number
# of requests successfully among all the servers.

# Return a list containing the IDs (0-indexed) of the busiest server(s).
# You may return the IDs in any order.

# Constraints:
#   1 <= k <= 10^5
#   1 <= arrival.length, load.length <= 10^5
#   arrival.length == load.length
#   1 <= arrival[i], load[i] <= 10^9
#   arrival is strictly increasing.
from typing import List
import sortedcontainers
import heapq


# SortedList and PriorityQueue
# Time:  O(n*log(k)), where n is number of requests, k is number of servers
# Space: O(k)
# - to simplify code a little bit
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        servers = sortedcontainers.SortedList(range(k))
        counts = {i:0 for i in range(k)}
        sche = []
        heapq.heapify(sche)
        for i, (ar, ld) in enumerate(zip(arrival, load)):
            while sche:
                if sche[0][0] > ar: break
                servers.add(heapq.heappop(sche)[1])
            avail = len(servers)
            if avail == 0: continue
            j = servers.bisect_left(i % k) % avail
            svr = servers.pop(j)
            heapq.heappush(sche, (ar + ld, svr))
            counts[svr] += 1

        max_reqs = max(counts.values())
        res = [svr for svr, cnt in counts.items() if cnt == max_reqs]

        return res


# SortedDict and PriorityQueue
# Time:  O(n*log(k)), where n is number of requests, k is number of servers
# Space: O(k)
class Solution1:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        servers = sortedcontainers.SortedDict({i:0 for i in range(k)})
        sche = []
        heapq.heapify(sche)
        for i, (ar, ld) in enumerate(zip(arrival, load)):
            while sche:
                if sche[0][0] <= ar:
                    _, svr, reqs = heapq.heappop(sche)
                    servers[svr] = reqs
                else:
                    break
            avail = len(servers)
            if avail == 0: continue
            j = servers.bisect_left(i % k) % avail
            svr, reqs = servers.popitem(j)
            heapq.heappush(sche, (ar + ld, svr, reqs + 1))

        max_reqs = 0
        if len(sche) > 0:
            max_reqs = max(reqs for _, svr, reqs in sche)
        if len(servers) > 0:
            max_reqs = max(max_reqs, max(servers.values()))

        res = []
        res = [svr for _, svr, reqs in sche if reqs == max_reqs]
        res.extend([svr for svr, reqs in servers.items() if reqs == max_reqs])

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.busiestServers(k=3, arrival=[1, 2, 3, 4, 5], load=[5, 2, 3, 3, 3])
        print(r)
        assert r == [1]

        r = sol.busiestServers(k=3, arrival=[1, 2, 3, 4], load=[1, 2, 1, 2])
        print(r)
        assert r == [0]

        r = sol.busiestServers(k=3, arrival=[1, 2, 3], load=[10, 12, 11])
        print(r)
        assert r == [0, 1, 2]

    unitTest(Solution())
