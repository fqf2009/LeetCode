# Given an array of intervals where intervals[i] = [starti, endi], merge all 
# overlapping intervals, and return an array of the non-overlapping intervals 
# that cover all the intervals in the input.
# Constraints:
#   1 <= intervals.length <= 10^4
#   intervals[i].length == 2
#   0 <= starti <= endi <= 10^4
from typing import List

# Stack: O(n*log(n))
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for v in intervals:
            x = res[-1]
            if x[1] >= v[0]:
                x[1] = max(x[1], v[1])
            else:
                res.append(v)

        return res


if __name__ == '__main__':
    r = Solution().merge([[1,3],[2,6],[8,10],[15,18]])
    print(r)
    assert(r == [[1,6],[8,10],[15,18]])

    r = Solution().merge([[1,4],[4,5]])
    print(r)
    assert(r == [[1,5]])

    r = Solution().merge([[1,4],[5,6]])
    print(r)
    assert(r == [[1,4],[5,6]])

    r = Solution().merge([[1,4],[2,3]])
    print(r)
    assert(r == [[1,4]])
