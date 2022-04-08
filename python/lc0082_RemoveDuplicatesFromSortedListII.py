# Given the head of a sorted linked list, delete all nodes that have
# duplicate numbers, leaving only distinct numbers from the original
# list. Return the linked list sorted as well.
# Constraints:
#   The number of nodes in the list is in the range [0, 300].
#   -100 <= Node.val <= 100
#   The list is guaranteed to be sorted in ascending order.
from typing import Optional
from lib.ListUtil import ListNode, ListNodeUtil


# Linked List: O(n)
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h0 = p = ListNode(next = head)  # p is lagging behind one node
        while p and p.next:
            p1 = p.next                 # p1 is current node
            cnt = 1
            while p1.next and p1.val == p1.next.val:    # count duplicates
                cnt += 1
                p1 = p1.next            # p1 points to the last duplicate
            if cnt > 1:
                p.next = p1.next        # skip all duplicates
            else:
                p = p1                  # p points to current node

        return h0.next


if __name__ == '__main__':
    def unitTest(sol):
        head = ListNodeUtil.createLinkedList([1, 2, 3, 3, 4, 4, 5])
        r = ListNodeUtil.toArrayList(sol.deleteDuplicates(head))
        print(r)
        assert r == [1, 2, 5]

        head = ListNodeUtil.createLinkedList([1, 1, 1, 2, 3])
        r = ListNodeUtil.toArrayList(sol.deleteDuplicates(head))
        print(r)
        assert r == [2, 3]

        head = ListNodeUtil.createLinkedList([1, 2, 3, 3])
        r = ListNodeUtil.toArrayList(sol.deleteDuplicates(head))
        print(r)
        assert r == [1, 2]

        head = ListNodeUtil.createLinkedList([1, 1, 1, 2, 2, 3, 3])
        r = ListNodeUtil.toArrayList(sol.deleteDuplicates(head))
        print(r)
        assert r == []

    unitTest(Solution())
