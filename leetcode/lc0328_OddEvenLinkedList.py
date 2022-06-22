# Given the head of a singly linked list, group all the nodes with odd indices
# together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should
# remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time
# complexity.
# Constraints:
#   The number of nodes in the linked list is in the range [0, 10^4].
#   -10^6 <= Node.val <= 10^6
from lib.ListUtil import ListNode, ListNodeUtil
from typing import Optional


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        h1 = p1 = ListNode()  # odd
        h2 = p2 = ListNode()  # even
        p = head
        while p and p.next:
            p1.next, p2.next = p, p.next  # two nodes assigned to two lists
            p = p.next.next  # move two steps each time
            p1, p2 = p1.next, p2.next

        if p:
            p1.next = p
            p1 = p

        p1.next = h2.next
        p2.next = None      # !!! important to prevent cyclic linked list
        return h1.next


if __name__ == "__main__":

    def unit_test(sol):
        head = ListNodeUtil.createLinkedList([1, 2, 3, 4, 5])
        r = ListNodeUtil.toArrayList(sol.oddEvenList(head))
        print(r)
        assert r == [1, 3, 5, 2, 4]

        head = ListNodeUtil.createLinkedList([2, 1, 3, 5, 6, 4, 7])
        r = ListNodeUtil.toArrayList(sol.oddEvenList(head))
        print(r)
        assert r == [2, 3, 6, 7, 1, 5, 4]

    unit_test(Solution())
