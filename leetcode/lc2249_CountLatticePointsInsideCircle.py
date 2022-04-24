# Given a 2D integer array circles where circles[i] = [xi, yi, ri] 
# represents the center (xi, yi) and radius ri of the ith circle 
# drawn on a grid, return the number of lattice points that are 
# present inside at least one circle.
# Note:
#   A lattice point is a point with integer coordinates.
#   Points that lie on the circumference of a circle are also considered to be inside it.
# Constraints:
#   1 <= circles.length <= 200
#   circles[i].length == 3
#   1 <= xi, yi <= 100
#   1 <= ri <= min(xi, yi)
from typing import List


# HashSet: O(p), where p = number_of_points_in_all_circles
# Analysis:
# - iterate over circle's edge to get all points inside circle
# - use set to remove duplicates
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()
        for x, y, r in circles:
            i, j = 0, r
            while j >= 0:
                if i*i + j*j <= r*r:
                    points.update((p, y+j) for p in range(x-i, x+i+1))
                    points.update((p, y-j) for p in range(x-i, x+i+1))
                    i += 1
                else:
                    i -= 1  # important, otherwise may miss some points
                    j -= 1

        return len(points)


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.countLatticePoints([[8,9,6],[9,8,4],[4,1,1],[8,5,1],[7,1,1],
                                    [6,7,5],[7,1,1],[7,1,1],[5,5,3]])
        print(r)
        assert r == 141

        r = sol.countLatticePoints([[2,2,1]])
        print(r)
        assert r == 5

        r = sol.countLatticePoints([[2,2,2],[3,4,1]])
        print(r)
        assert r == 16

    unit_test(Solution())
