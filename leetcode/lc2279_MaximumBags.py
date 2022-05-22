# You have n bags numbered from 0 to n - 1. You are given two 0-indexed
# integer arrays capacity and rocks. The ith bag can hold a maximum of
# capacity[i] rocks and currently contains rocks[i] rocks. You are also
# given an integer additionalRocks, the number of additional rocks you
# can place in any of the bags.
# Return the maximum number of bags that could have full capacity after
# placing the additional rocks in some bags.
# Constraints:
#   n == capacity.length == rocks.length
#   1 <= n <= 5 * 10^4
#   1 <= capacity[i] <= 10^9
#   0 <= rocks[i] <= capacity[i]
#   1 <= additionalRocks <= 10^9
from itertools import accumulate
from typing import List


class Solution1:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        fill = sorted(capacity[i] - rocks[i] for i in range(n) if capacity[i] > rocks[i])
        res = n - len(fill) + len(list(x for x in accumulate(fill) if x <= additionalRocks))
        return res


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        fill = sorted(capacity[i] - rocks[i] for i in range(n) if capacity[i] > rocks[i])
        res = n - len(fill)
        for f in fill:
            if additionalRocks >= f:
                res += 1
                additionalRocks -= f
            else:
                break
        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.maximumBags([2, 3, 4, 5], rocks=[1, 2, 4, 4], additionalRocks=2)
        print(r)
        assert r == 3

        r = sol.maximumBags([10, 2, 2], rocks=[2, 2, 0], additionalRocks=100)
        print(r)
        assert r == 3

        r = sol.maximumBags([10, 2, 2], rocks=[2, 2, 0], additionalRocks=5)
        print(r)
        assert r == 2

    unit_test(Solution())
    unit_test(Solution1())
