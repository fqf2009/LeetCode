# You are given an array of positive integers beans, where each 
# integer represents the number of magic beans found in a 
# particular magic bag.

# Remove any number of beans (possibly none) from each bag such 
# that the number of beans in each remaining non-empty bag (still 
# containing at least one bean) is equal. Once a bean has been 
# removed from a bag, you are not allowed to return it to any of 
# the bags.

# Return the minimum number of magic beans that you have to remove.
from typing import List

# Analysis:
# - take an example: beans=[4, 1, 6, 5]
# - sort it to: [1, 4, 5, 6], total beans is 16
# - if we pick 1, as the target number of beans in each bag,
#   we need to remove 16 - 1 * 4 (bags) = 12 beans
# - if we pick 4, as the target number of beans in each bag,
#   we need to remove 16 - 4 * 3 (remaining bags) = 4 beans
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n = len(beans)
        beans.sort()
        res = total = sum(beans)
        for i in range(n):
            res = min(res, total - beans[i] * (n - i))

        return res


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.minimumRemoval(beans=[2, 10, 3, 2])
        print(r)
        assert r == 7

        r = sol.minimumRemoval(beans=[4, 1, 6, 5])
        print(r)
        assert r == 4

        r = sol.minimumRemoval(beans=[2, 10, 3])
        print(r)
        assert r == 5

        r = sol.minimumRemoval(beans=[2, 3])
        print(r)
        assert r == 1

        r = sol.minimumRemoval(beans=[2, 10])
        print(r)
        assert r == 2

        r = sol.minimumRemoval(beans=[2,])
        print(r)
        assert r == 0

    unitTest(Solution())
