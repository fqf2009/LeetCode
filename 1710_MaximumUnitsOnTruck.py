# You are assigned to put some amount of boxes onto one truck. You are given a
# 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
#  - numberOfBoxesi is the number of boxes of type i.
#  - numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of boxes
# that can be put on the truck. You can choose any boxes to put on the truck as
# long as the number of boxes does not exceed truckSize.
# Return the maximum total number of units that can be put on the truck.
# Constraints:
#   1 <= boxTypes.length <= 1000
#   1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
#   1 <= truckSize <= 10^6
from typing import List


# Greedy: O(nlog(n)) due to sort
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse=True)
        res = 0
        for boxes, units in boxTypes:
            res += min(truckSize, boxes) * units
            truckSize -= boxes
            if truckSize <= 0: break

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.maximumUnits([[1, 3], [2, 2], [3, 1]], 4)
        print(r)
        assert r == 8

        r = sol.maximumUnits([[5, 10], [2, 5], [4, 7], [3, 9]], truckSize=10)
        print(r)
        assert r == 91

    unitTest(Solution())
