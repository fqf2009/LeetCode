from typing import List
from operator import itemgetter
import heapq

# Sorting + Priority Queue

# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i],
# obtaining a profit of profit[i]. You're given the startTime, endTime and profit arrays,
# return the maximum profit you can take such that there are no two jobs in the subset with
# overlapping time range. If you choose a job that ends at time X you will be able to start
# another job that starts at time X.

# Time complexity: O(n*log(n)), consists of:
#   - Sorting: O(n*log(n))
#   - Loop (O(n)) and PQ push (log(n)): O(n*log(n))
# chains    - each job chain contains a queue of jobs without conflict, each item in queue
#             contains the endtime of a job, and the accumulated profit of chain.
# maxProfit - tracks the max profit of all the poped out chain. Because the to-do jobs's
#             start time are greater than those poped out, they can always get profit starting
#             from this maxProfit. So no need to push items back into the poped-out chain.
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        chains = []
        maxProfit = 0
        for start, end, prof in jobs:
            while len(chains) > 0 and chains[0][0] <= start: # peek the PQ for chain non-conflicting with next job
                _, chainProfit = heapq.heappop(chains)
                maxProfit = max(maxProfit, chainProfit)
            heapq.heappush(chains, (end, maxProfit + prof))

        return max(chains, key = itemgetter(1))[1]


if __name__ == '__main__':
    sol = Solution()

    r = sol.jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70])
    print(r)
    assert(r == 120)

    r = sol.jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60])
    print(r)
    assert(r == 150)

    r = sol.jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4])
    print(r)
    assert(r == 6)