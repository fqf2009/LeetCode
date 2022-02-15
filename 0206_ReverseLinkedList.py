# Given the head of a singly linked list, reverse the list,
# and return the reversed list.
from lib.ListUtil import ListNode, ListNodeUtil
from typing import List, Optional


# Reverse linked list in place: O(n)
# - h is new head down the road, p points to next node from head
# - as long as p is not null yet, use p1 to hold next node from p, then
#   reverse p to point to h, finally h and p points to p and p1, ...
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        h, p = head, head.next
        h.next = None
        while p:
            p1 = p.next
            p.next = h
            h = p
            p = p1

        return h

if __name__ == '__main__':
    def unit_test(sol):
        h1 = ListNodeUtil.createLinkedList([1, 2, 3, 4, 5])
        h2 = sol.reverseList(h1)
        r = ListNodeUtil.toArrayList(h2)
        print(r)
        assert(r == [5, 4, 3, 2, 1])

        h1 = ListNodeUtil.createLinkedList([1, 2])
        h2 = sol.reverseList(h1)
        r = ListNodeUtil.toArrayList(h2)
        print(r)
        assert(r == [2, 1])

        h1 = ListNodeUtil.createLinkedList([])
        h2 = sol.reverseList(h1)
        r = ListNodeUtil.toArrayList(h2)
        print(r)
        assert(r == [])

    unit_test(Solution())
