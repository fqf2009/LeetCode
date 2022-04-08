# You are given two lists of closed intervals, firstList and secondList,
# where firstList[i] = [starti, endi] and secondList[j] = [startj, endj].
# Each list of intervals is pairwise disjoint and in sorted order.
# Return the intersection of these two interval lists.
# A closed interval [a, b] (with a <= b) denotes the set of real
# numbers x with a <= x <= b.

# The intersection of two closed intervals is a set of real numbers
# that are either empty or represented as a closed interval. For example,
# the intersection of [1, 3] and [2, 4] is [2, 3].

# Constraints:
#   0 <= firstList.length, secondList.length <= 1000
#   firstList.length + secondList.length >= 1
#   0 <= starti < endi <= 109
#   endi < starti+1
#   0 <= startj < endj <= 109
#   endj < startj+1
from typing import List


# Two Pointers to Merge Intervals: O(n)
# - simplify the code
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []
        while i < len(A) and j < len(B):
            lo = max(A[i][0], B[j][0])  # start of intersection
            hi = min(A[i][1], B[j][1])  # end of intersection
            if lo <= hi:
                res.append([lo, hi])
            if A[i][1] < B[j][1]:
                i += 1
            elif A[i][1] > B[j][1]:
                j += 1
            else:
                i += 1
                j += 1

        return res


# Two Pointers: O(n)
# - too easy to have bug???
class Solution1:
    def intervalIntersection(self, firstList: List[List[int]],
                             secondList: List[List[int]]) -> List[List[int]]:
        m, n = len(firstList), len(secondList)
        if m*n == 0:
            return []

        i = j = 0
        l1, r1 = firstList[0]
        l2, r2 = secondList[0]
        res = []
        while True:
            if r1 < r2:
                if l2 <= r1:
                    res.append([max(l1, l2), r1])
                i += 1
                if i == m:
                    break
                l1, r1 = firstList[i]
            elif r1 == r2:
                res.append([max(l1, l2), r1])
                i += 1
                j += 1
                if i == m or j == n:
                    break
                l1, r1 = firstList[i]
                l2, r2 = secondList[j]
            else:  # r1 > r2
                if l1 <= r2:
                    res.append([max(l1, l2), r2])
                j += 1
                if j == n:
                    break
                l2, r2 = secondList[j]

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]],
                                     [[1, 5], [8, 12], [15, 24], [25, 26]])
        print(r)
        assert r == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

        r = sol.intervalIntersection([[1, 3], [5, 9]], [])
        print(r)
        assert r == []

        r = sol.intervalIntersection([[3, 10]], [[5, 10]])
        print(r)
        assert r == [[5, 10]]

        r = sol.intervalIntersection([[14, 16]], [[7, 13], [16, 20]])
        print(r)
        assert r == [[16, 16]]

        r = sol.intervalIntersection([[3, 5], [9, 20]],
                                     [[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]])
        print(r)
        assert r == [[4, 5], [9, 10], [11, 12], [14, 15], [16, 20]]

    unitTest(Solution())
    unitTest(Solution1())
