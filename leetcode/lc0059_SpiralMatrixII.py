# Given a positive integer n, generate an n x n matrix filled with
# elements from 1 to n2 in spiral order.
# Constraints:
#   1 <= n <= 20
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        i, j = 0, -1
        r, c = n, n
        delta = 1
        res = [[0] * n for _ in range(n)]
        v = 0
        while r * c > 0:
            for _ in range(c):
                j += delta
                v += 1
                res[i][j] = v
            r -= 1
            for _ in range(r):
                i += delta
                v += 1
                res[i][j] = v
            c -= 1
            delta *= -1

        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.generateMatrix(3)
        print(r)
        assert r == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

        r = sol.generateMatrix(1)
        print(r)
        assert r == [[1]]

    unit_test(Solution())
