# A cinema has n rows of seats, numbered from 1 to n and there are ten seats
# in each row, labelled from 1 to 10 as shown in the figure above.
#  - [1][2][3][aisle][4][5][6][7][aisle][8][9][10]
#  - aisle one is between 3 and 4; aisle two is between 7, 8
# Given the array reservedSeats containing the numbers of seats already
# reserved, for example, reservedSeats[i] = [3,8] means the seat located
# in row 3 and labelled with 8 is already reserved.

# Return the maximum number of four-person groups you can assign on
# the cinema seats. A four-person group occupies four adjacent seats
# in one single row. Seats across an aisle (such as [3,3] and [3,4])
# are not considered to be adjacent, but there is an exceptional case
# on which an aisle split a four-person group, in that case, the aisle
# split a four-person group in the middle, which means to have two
# people on each side.
# Constraints:
#   1 <= n <= 10^9
#   1 <= reservedSeats.length <= min(10*n, 10^4)
#   reservedSeats[i].length == 2
#   1 <= reservedSeats[i][0] <= n
#   1 <= reservedSeats[i][1] <= 10
#   All reservedSeats[i] are distinct.
from collections import defaultdict
from typing import List


# Analysis:
# - each row has 3 overlapping 4-seats group: [2-5] [4-7] [6-9]
#                2 max non-overlapping group: [2-5] [6-9]
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = defaultdict(set)
        for i, j in reservedSeats:
            if 2 <= j <= 5:
                seats[i].add(0)
            if 4 <= j <= 7:
                seats[i].add(1)
            if 6 <= j <= 9:
                seats[i].add(2)

        return 2 * n - sum(2 if len(x) == 3 else 1 for x in seats.values())


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.maxNumberOfFamilies(3, [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]])
        print(r)
        assert r == 4

        r = sol.maxNumberOfFamilies(2, [[2, 1], [1, 8], [2, 6]])
        print(r)
        assert r == 2

        r = sol.maxNumberOfFamilies(4, [[4, 3], [1, 4], [4, 6], [1, 7]])
        print(r)
        assert r == 4

    unit_test(Solution())
