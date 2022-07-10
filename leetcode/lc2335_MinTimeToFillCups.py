# You have a water dispenser that can dispense cold, warm, and hot water.
# Every second, you can either fill up 2 cups with different types of water,
# or 1 cup of any type of water.
# You are given a 0-indexed integer array amount of length 3 where
# amount[0], amount[1], and amount[2] denote the number of cold, warm, and
# hot water cups you need to fill respectively. Return the minimum number
# of seconds needed to fill up all the cups.
# Constraints:
#   amount.length == 3
#   0 <= amount[i] <= 100
from typing import List


# O(max(amount))
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        res = 0
        while True:
            amount.sort()
            if amount[0] == 0:
                res += amount[2]
                break
            amount[1] -= 1
            amount[2] -= 1
            res += 1

        return res


# Brain-teaser + Greedy: O(1)
# Analysis:
# - The optimal strategy is to always fill two different cups if possible.
# - One of the two cups will always be from the biggest stack.
# - There is no difference between the smallest and the medium stack because
#   you can take either of them exhaust it and proceed to the remaining stack
# - So we can just distribute the smallest stack optimally between the medium
#   and biggest stacks!
# - e.g.: [1, 3, 5] => [0, 4, 5]
#         [3, 4, 4] => [0, 5, 6]
class Solution1:
    def fillCups(self, amount: List[int]) -> int:
        return max(max(amount), (sum(amount) + 1) // 2)


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.fillCups([1, 4, 2])
        print(r)
        assert r == 4

        r = sol.fillCups([5, 4, 4])
        print(r)
        assert r == 7

        r = sol.fillCups([5, 0, 0])
        print(r)
        assert r == 5

    unit_test(Solution())
    unit_test(Solution1())
