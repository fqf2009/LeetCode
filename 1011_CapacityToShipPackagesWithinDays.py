# A conveyor belt has packages that must be shipped from one port to another
# within days days.
# The ith package on the conveyor belt has a weight of weights[i]. Each day,
# we load the ship with packages on the conveyor belt (in the order given
# by weights). We may not load more weight than the maximum weight capacity
# of the ship.
# Return the least weight capacity of the ship that will result in all the
# packages on the conveyor belt being shipped within days days.
# Constraints:
#   1 <= days <= weights.length <= 5 * 10^4
#   1 <= weights[i] <= 500
from typing import List


# Prefix Sum + Binary Search:
# T/S: O(d*log(n)*log(w)), O(n)
#   where d = days, n = len(weights), w = sum(weights) - sum(weights)/days
# Analysis:
# - first create a prefix sum array:
#       csum[i] = cumulative weight till package[i]
# - two level of binary searches:
#   - 1. ship capacity: from sum(weights)/days to sum(weights)
#   - 2. for a picked ship capacity, perform d (days) times
#        binary search in csum array, to check if each day take
#        max packages under capacity, can ship all packages at end.
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        csum = [0] * (len(weights) + 1)
        for i, w in enumerate(weights):
            csum[i+1] = csum[i] + w

        def can_ship(cap) -> bool:
            prev_pkg = 0
            for _ in range(days):
                pkg1 = prev_pkg + 1
                pkg2 = len(csum) - 1
                curr_pkg = -1
                while pkg1 <= pkg2:
                    pkg = (pkg1 + pkg2) // 2
                    if csum[pkg] - csum[prev_pkg] <= cap:
                        curr_pkg = pkg
                        pkg1 = pkg + 1
                    else:
                        pkg2 = pkg - 1

                if curr_pkg == len(csum) - 1:
                    return True
                elif curr_pkg == -1:
                    return False
                prev_pkg = curr_pkg

            return False

        cap2 = sum(weights)
        cap1 = cap2 // days
        res = cap2
        while cap1 <= cap2:
            cap = (cap1 + cap2) // 2
            if can_ship(cap):
                res = cap
                cap2 = cap - 1
            else:
                cap1 = cap + 1

        return res


# One level of Biniary Search: O(n*log(w)), O(1)
# - LeetCode has lots of small test cases, this approach is faster than
#   the above one.
class Solution1:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(cap) -> bool:
            csum = 0
            ships = 0
            for w in weights:
                if csum + w > cap:
                    ships += 1
                    csum = w
                else:
                    csum += w

                if w > cap or ships >= days:
                    return False

            return True

        cap2 = sum(weights)
        cap1 = cap2 // days
        res = cap2
        while cap1 <= cap2:
            cap = (cap1 + cap2) // 2
            if can_ship(cap):
                res = cap
                cap2 = cap - 1
            else:
                cap1 = cap + 1

        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5)
        print(r)
        assert r == 15

        r = sol.shipWithinDays([3, 2, 2, 4, 1, 4], days=3)
        print(r)
        assert r == 6

        r = sol.shipWithinDays([1, 2, 3, 1, 1], days=4)
        print(r)
        assert r == 3

    # unit_test(Solution())
    unit_test(Solution1())
