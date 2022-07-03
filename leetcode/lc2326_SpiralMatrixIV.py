# You are given two integers m and n, which represent the dimensions of a matrix.
# You are also given the head of a linked list of integers.
# Generate an m x n matrix that contains the integers in the linked list presented
# in spiral order (clockwise), starting from the top-left of the matrix. If there 
# are remaining empty spaces, fill them with -1.
# Return the generated matrix.
# Constraints:
#   1 <= m, n <= 10^5
#   1 <= m * n <= 10^5
#   The number of nodes in the list is in the range [1, m * n].
#   0 <= Node.val <= 1000
from typing import List, Optional
from lib.ListUtil import ListNode, ListNodeUtil


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1]*n for _ in range(m)]
        i, j, step = 0, -1, 1
        while head:
            for _ in range(n):
                if not head: break
                j += step
                res[i][j] = head.val
                head = head.next
            m -= 1
            for _ in range(m):
                if not head: break
                i += step
                res[i][j] = head.val
                head = head.next
            n -= 1
            step = -step

        return res
        

if __name__ == '__main__':
    def unit_test(sol):
        head = ListNodeUtil.createLinkedList([3,0,2,6,8,1,7,9,4,2,5,5,0])
        r = sol.spiralMatrix(3, 5, head)
        print(r)
        assert r == [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]

        head = ListNodeUtil.createLinkedList([0,1,2])
        r = sol.spiralMatrix(1, 4, head)
        print(r)
        assert r == [[0,1,2,-1]]

    unit_test(Solution())
