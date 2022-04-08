# Given an n x n matrix where each of the rows and columns is sorted
# in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not
# the kth distinct element.
# You must find a solution with a memory complexity better than O(n2).
# Constraints:
#   n == matrix.length == matrix[i].length
#   1 <= n <= 300
#   -10^9 <= matrix[i][j] <= 10^9
#   All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
#   1 <= k <= n^2
# Follow up:
#  - Could you solve the problem with a constant memory (i.e., O(1) 
#    memory complexity)?
#  - Could you solve the problem in O(n) time complexity? The solution 
#    may be too advanced for an interview but you may find reading this
#    paper (http://www.cse.yorku.ca/~andy/pubs/X+Y.pdf) fun.
import heapq
from typing import List


# PriorityQueue - T/S: O(k*log(min(k,n))), O(min(k,n))
# - similar to 0023 Merge k Lists
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        que = [(matrix[i][0], i, 0) for i in range(min(k, n))]  # (val, row, col)
        heapq.heapify(que)
        val = -1
        for _ in range(k):
            val, r, c = heapq.heappop(que)
            if c < n-1:
                heapq.heappush(que, (matrix[r][c+1], r, c+1)) #type:ignore
        return val


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.kthSmallest(matrix=[[1,   5,  9],
                                    [10, 11, 13],
                                    [12, 13, 15]],
                            k=8)
        print(r)
        assert r == 13

        r = sol.kthSmallest(matrix=[[-5]], k=1)
        print(r)
        assert r == -5

    unitTest(Solution())
