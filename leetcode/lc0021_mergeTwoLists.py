from typing import Optional
from lib.ListUtil import ListNode, ListNodeUtil

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by
# splicing together the nodes of the first two lists.
# Return the head of the merged linked list.


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = p = ListNode()
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                p.next = l1
                p = l1
                l1 = l1.next
            else:
                p.next = l2
                p = l2
                l2 = l2.next

        p.next = l1 if l1 else l2
        return head.next


if __name__ == '__main__':
    sol = Solution()

    h1 = ListNodeUtil.createLinkedList([1, 2, 4])
    h2 = ListNodeUtil.createLinkedList([1, 3, 4])
    r = ListNodeUtil.toArrayList(sol.mergeTwoLists(h1, h2))
    print(r)
    assert(r == [1, 1, 2, 3, 4, 4])

    h1 = ListNodeUtil.createLinkedList([])
    h2 = ListNodeUtil.createLinkedList([])
    r = ListNodeUtil.toArrayList(sol.mergeTwoLists(h1, h2))
    print(r)
    assert(r == [])

    h1 = ListNodeUtil.createLinkedList([])
    h2 = ListNodeUtil.createLinkedList([0])
    r = ListNodeUtil.toArrayList(sol.mergeTwoLists(h1, h2))
    print(r)
    assert(r == [0])
