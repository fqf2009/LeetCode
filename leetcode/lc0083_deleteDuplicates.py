# Given the head of a sorted linked list, delete all duplicates such that
# each element appears only once. Return the linked list sorted as well.
# Constraints:
#   The number of nodes in the list is in the range [0, 300].
#   -100 <= Node.val <= 100
#   The list is guaranteed to be sorted in ascending order.

# Definition for singly-linked list.
from typing import Optional
from lib.ListUtil import ListNode, ListNodeUtil


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p and p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next

        return head


if __name__ == '__main__':
    def unitTest(sol):
        head = ListNodeUtil.createLinkedList([1, 1, 1])
        r = ListNodeUtil.toArrayList(sol.deleteDuplicates(head))
        print(r)
        assert r == [1]

        head = ListNodeUtil.createLinkedList([1, 1, 2])
        r = ListNodeUtil.toArrayList(sol.deleteDuplicates(head))
        print(r)
        assert r == [1, 2]

        head = ListNodeUtil.createLinkedList([1, 1, 2, 3, 3])
        r = ListNodeUtil.toArrayList(sol.deleteDuplicates(head))
        print(r)
        assert r == [1, 2, 3]

    unitTest(Solution())
