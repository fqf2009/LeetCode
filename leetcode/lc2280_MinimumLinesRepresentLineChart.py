# You are given a 2D integer array stockPrices where stockPrices[i] = [dayi, pricei]
# indicates the price of the stock on day dayi is pricei. A line chart is created 
# from the array by plotting the points on an XY plane with the X-axis representing
# the day and the Y-axis representing the price and connecting adjacent points.
# 
# One such example is shown below:
#   Input: stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]
#   Output: 3
#   Explanation:
#       The diagram above represents the input, with the X-axis representing 
#       the day and Y-axis representing the price.
#       The following 3 lines can be drawn to represent the line chart:
#       - Line 1 (in red) from (1,7) to (4,4) passing through
#         (1,7), (2,6), (3,5), and (4,4).
#       - Line 2 (in blue) from (4,4) to (5,4).
#       - Line 3 (in green) from (5,4) to (8,1) passing through
#         (5,4), (6,3), (7,2), and (8,1).
#       It can be shown that it is not possible to represent the line chart
#       using less than 3 lines.
# Constraints:
#   1 <= stockPrices.length <= 10^5
#   stockPrices[i].length == 2
#   1 <= dayi, pricei <= 10^9
#   All dayi are distinct.

import math
from typing import List

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        A = stockPrices
        A.sort()
        res = 0
        coprime = (0, 0)
        for sp1, sp2 in zip(A, A[1:]):
            dd = sp2[0] - sp1[0]
            pd = sp2[1] - sp1[1]
            gcd = math.gcd(dd, pd)
            coprime1 = (dd // gcd, pd // gcd)
            if coprime[0] == 0 or coprime != coprime1:
                res += 1
                coprime = coprime1

        return res


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.minimumLines([[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]])
        print(r)
        assert r == 3

        r = sol.minimumLines([[3,4],[1,2],[7,8],[2,3]])
        print(r)
        assert r == 1

        r = sol.minimumLines([[1, 2]])
        print(r)
        assert r == 0

        r = sol.minimumLines([[1, 2], [2,3]])
        print(r)
        assert r == 1

    unit_test(Solution())
