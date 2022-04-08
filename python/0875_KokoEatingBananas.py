# Koko loves to eat bananas. There are n piles of bananas, the ith pile
# has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she 
# chooses some pile of bananas and eats k bananas from that pile. If the 
# pile has less than k bananas, she eats all of them instead and will not
# eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas
# before the guards return.

# Return the minimum integer k such that she can eat all the bananas within 
# h hours.

from typing import List
import math

# Binary search
# Time complexity: O(n*log(m)), where n = len(piles), m = max(piles)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i, j = math.ceil(sum(piles) / h), max(piles)
        res = j
        while i <= j and i > 0:
            k = (i + j) // 2
            hours = sum(map(lambda x: math.ceil(x / k), piles))
            if hours <= h:
                res = min(k, res)
                j = k - 1
            else:
                i = k + 1
        
        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.minEatingSpeed(piles = [312884470], h = 312884469)
        print(r)
        assert(r == 2)

        r = sol.minEatingSpeed(piles = [312884470], h = 312884470)
        print(r)
        assert(r == 1)

        r = sol.minEatingSpeed(piles = [3,6,7,11], h = 8)
        print(r)
        assert(r == 4)

        r = sol.minEatingSpeed(piles = [30,11,23,4,20], h = 5)
        print(r)
        assert(r == 30)

        r = sol.minEatingSpeed(piles = [30,11,23,4,20], h = 6)
        print(r)
        assert(r == 23)

    unitTest(Solution())
