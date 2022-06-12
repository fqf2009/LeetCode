# You are visiting a farm that has a single row of fruit trees
# arranged from left to right. The trees are represented by an
# integer array fruits where fruits[i] is the type of fruit the
# ith tree produces.
# You want to collect as much fruit as possible. However, the
# owner has some strict rules that you must follow:
# You only have two baskets, and each basket can only hold a
# single type of fruit. There is no limit on the amount of
# fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly
# one fruit from every tree (including the start tree) while
# moving to the right. The picked fruits must fit in one of
# your baskets.
# Once you reach a tree with fruit that cannot fit in your
# baskets, you must stop.
# Given the integer array fruits, return the maximum number of
# fruits you can pick.
# Constraints:
#   1 <= fruits.length <= 10^5
#   0 <= fruits[i] < fruits.length
from collections import Counter
from typing import List


# Sliding window: O(n)
# ref - 0159_LongestSubstringWithAtMostTwoDistinctCharacters
# ref - 0340_LongestSubstringWithAtMostKDistinctCharacters
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        seen = Counter()
        res = 0
        j = 0
        for i, v in enumerate(fruits):
            seen[v] += 1
            while len(seen) > 2:
                seen[fruits[j]] -= 1
                if seen[fruits[j]] == 0:
                    del seen[fruits[j]]
                j += 1

            res = max(res, i - j + 1)

        return res


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.totalFruit([1, 2, 1])
        print(r)
        assert r == 3

        r = sol.totalFruit([1, 2, 1])
        print(r)
        assert r == 3

        r = sol.totalFruit([1, 2, 3, 2, 2])
        print(r)
        assert r == 4

    unitTest(Solution())
