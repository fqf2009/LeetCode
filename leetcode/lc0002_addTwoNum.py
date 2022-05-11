from lib.ListUtil import ListNode, ListNodeUtil
from typing import Optional

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single 
# digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = p = ListNode()
        while l1 or l2 or carry > 0:
            if l1:
                carry += l1.val
                l1 = l1.next

            if l2:
                carry += l2.val
                l2 = l2.next
            
            p.next = ListNode(carry % 10)
            p = p.next
            carry //= 10

        return head.next


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
            ([0], [0], [0]),
            ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
            ([9, 9, 9, 9, 9], [1], [0, 0, 0, 0, 0, 1]),
        ])
        def test_addTwoNumbers(self, l1, l2, expected):
            sol = self.solution()       # type:ignore
            head1 = ListNodeUtil.createLinkedList(l1)
            head2 = ListNodeUtil.createLinkedList(l2)
            head3 = ListNodeUtil.toArrayList(sol.addTwoNumbers(head1, head2))
            print(head3)
            self.assertEqual(head3, expected)

    main()
