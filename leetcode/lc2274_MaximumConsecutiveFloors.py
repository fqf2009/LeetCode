# Alice manages a company and has rented some floors of a building 
# as office space. Alice has decided some of these floors should be 
# special floors, used for relaxation only.
# You are given two integers bottom and top, which denote that Alice
# has rented all the floors from bottom to top (inclusive). You are 
# also given the integer array special, where special[i] denotes a 
# special floor that Alice has designated for relaxation.
# Return the maximum number of consecutive floors without a special floor.
# Constraints:
#   1 <= special.length <= 10^5
#   1 <= bottom <= special[i] <= top <= 10^9
#   All the values of special are unique.
from itertools import chain
from typing import List


class Solution1:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        arr = sorted(chain(special, [bottom-1, top+1]))
        return max(y-x-1 for x, y in zip(arr, arr[1:]))


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.append(bottom-1)
        special.append(top+1)
        special.sort()
        return max(special[i] - special[i-1] - 1 for i in range(1, len(special)))


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.maxConsecutive(bottom = 6, top = 39, special = [38])
        print(r)
        assert r == 32

        r = sol.maxConsecutive(bottom = 2, top = 9, special = [4,6])
        print(r)
        assert r == 3

        r = sol.maxConsecutive(bottom = 6, top = 8, special = [7,6,8])
        print(r)
        assert r == 0


    unit_test(Solution())
    unit_test(Solution1())
