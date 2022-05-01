# You are given an integer array cards where cards[i] represents the value of the ith card.
# A pair of cards are matching if the cards have the same value.
# Return the minimum number of consecutive cards you have to pick up to have a pair of
# matching cards among the picked cards. If it is impossible to have matching cards, return -1.
# Constraints:
#   1 <= cards.length <= 10^5
#   0 <= cards[i] <= 10^6
from typing import List


# Sliding Window - T/S: O(n), O(n)
# Analysis:
# - iterate over cards, save item's pos into map
# - if any item encountered before, then keep the min length,
#   and delete all items until current item's previous pos.
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res, j = 10**9, 0
        pos = {}
        for i, v in enumerate(cards):
            if v not in pos:
                pos[v] = i
            else:
                res = min(res, i - pos[v] + 1)
                for k in range(j, pos[v]):
                    del pos[cards[k]]
                j = pos[v] + 1
                pos[v] = i

        return -1 if res == 10**9 else res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.minimumCardPickup([3, 4, 2, 3, 4, 7])
        print(r)
        assert r == 4

        r = sol.minimumCardPickup([1, 0, 5, 3])
        print(r)
        assert r == -1

    unit_test(Solution())
