# A square matrix is said to be an X-Matrix if both of the
# following conditions hold:
#  - All the elements in the diagonals of the matrix are non-zero.
#  - All other elements are 0.
# Given a 2D integer array grid of size n x n representing a square
# matrix, return true if grid is an X-Matrix. Otherwise, return false.
# Constraints:
#   n == grid.length == grid[i].length
#   3 <= n <= 100
#   0 <= grid[i][j] <= 10^5
from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.checkXMatrix([[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]])
        print(r)
        assert r == True

        r = sol.checkXMatrix([[5, 7, 0], [0, 3, 1], [0, 5, 0]])
        print(r)
        assert r == False

    unit_test(Solution())
