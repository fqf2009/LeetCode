# You are given a 0-indexed array nums that consists of n distinct 
# positive integers. Apply m operations to this array, where in the ith
# operation you replace the number operations[i][0] with operations[i][1].
# It is guaranteed that in the ith operation:
#  - operations[i][0] exists in nums.
#  - operations[i][1] does not exist in nums.
#  - Return the array obtained after applying all the operations.
# Constraints:
#   n == nums.length
#   m == operations.length
#   1 <= n, m <= 105
#   All the values of nums are distinct.
#   operations[i].length == 2
#   1 <= nums[i], operations[i][0], operations[i][1] <= 10^6
#   operations[i][0] will exist in nums when applying the ith operation.
#   operations[i][1] will not exist in nums when applying the ith operation.
from typing import List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        map = {v: i for i, v in enumerate(nums)}
        for v1, v2 in operations:
            map[v2] = map[v1]
            del map[v1]

        return [v for i, v in sorted((i, v) for v, i in map.items())]


if __name__ == "__main__":

    def unit_arrayChange(sol):
        r = sol.arrayChange([1, 2, 4, 6], operations=[[1, 3], [4, 7], [6, 1]])
        print(r)
        assert r == [3, 2, 7, 1]

        r = sol.arrayChange([1, 2], operations=[[1, 3], [2, 1], [3, 2]])
        print(r)
        assert r == [2, 1]

    unit_arrayChange(Solution())
