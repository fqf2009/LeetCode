# Given the head of a linked list, return the list 
# after sorting it in ascending order.

# Constraints:
#   The number of nodes in the list is in the range [0, 5 * 10^4].

from typing import List, Optional
from lib.ListUtil import ListNode, ListNodeUtil

# Merge Sort
# time: O(n*log(n)), space: O(log(n)), due to recursion depth log(n)
class Solution:
    def findMid(self, head: ListNode) ->ListNode:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next    # type:ignore
            fast = fast.next.next
        return slow             # type:ignore

    def mergeList(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        h0 = p = ListNode()
        while head1 and head2:
            if head1.val <= head2.val:
                p.next = head1
                head1 = head1.next
            else:
                p.next = head2
                head2 = head2.next
            p = p.next
        p.next = head1 if head1 else head2
        return h0.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = self.findMid(head)
        right = mid.next
        mid.next = None
        head = self.sortList(head)
        right = self.sortList(right)
        return self.mergeList(head, right)


if __name__ == '__main__':
    def unitTest(sol):
        h1 = ListNodeUtil.createLinkedList([4, 2, 1, 3])
        h2 = sol.sortList(h1)
        r = ListNodeUtil.toArrayList(h2)
        print(r)
        assert(r == [1, 2, 3, 4])

        h1 = ListNodeUtil.createLinkedList([-1, 5, 3, 4, 0])
        h2 = sol.sortList(h1)
        r = ListNodeUtil.toArrayList(h2)
        print(r)
        assert(r == [-1, 0, 3, 4, 5])

        h1 = ListNodeUtil.createLinkedList([])
        h2 = sol.sortList(h1)
        r = ListNodeUtil.toArrayList(h2)
        print(r)
        assert(r == [])

    unitTest(Solution())
