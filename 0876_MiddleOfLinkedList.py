# Given the head of a singly linked list, return the middle
# node of the linked list.
# If there are two middle nodes, return the second middle node.

from typing import Optional
from lib.ListUtil import ListNode, ListNodeUtil

# Scan twice: more clear, easier to write
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        depth = 0
        p1 = p2 = head
        while p2:
            p2 = p2.next
            depth += 1
        
        for _ in range(depth // 2):
            p1 = p1.next        # type:ignore
        
        return p1

# Two pointers
class Solution1:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        p1, p2 = head, head.next
        while p1 and p2:
            p1, p2 = p1.next, p2.next
            if p2:
                p2 = p2.next
        
        return p1


if __name__ == '__main__':
    def unitTest(sol):
        head = ListNodeUtil.createLinkedList([1, 2, 3, 4, 5])
        node = sol.middleNode(head)
        r = ListNodeUtil.toArrayList(node)
        print(r)
        assert r == [3, 4, 5]

        head = ListNodeUtil.createLinkedList([1, 2, 3, 4, 5, 6])
        node = sol.middleNode(head)
        r = ListNodeUtil.toArrayList(node)
        print(r)
        assert r == [4, 5, 6]

    unitTest(Solution())
    unitTest(Solution1())
