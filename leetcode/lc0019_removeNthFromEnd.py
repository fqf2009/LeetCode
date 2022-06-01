# Given the head of a linked list, remove the nth node from the end of 
# the list and return its head.
# Constraints:
#   The number of nodes in the list is sz.
#   1 <= sz <= 30
#   0 <= Node.val <= 100
#   1 <= n <= sz
from lib.ListUtil import ListNode, ListNodeUtil
from typing import Optional


# Scan twice: time O(n), space O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        depth = 0
        p = head
        while p != None:
            depth += 1
            p = p.next
        
        p = dumbHead = ListNode(next = head)
        for _ in range(depth - n):
            p = p.next          # type:ignore

        p.next = p.next.next    # type:ignore
        return dumbHead.next


# Two pointers
class Solution1:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = p2 = h0 = ListNode(next = head)
        for i in range(n):
            p2 = p2.next                # type:ignore
        
        while p2 and p2.next:
            p1, p2 = p1.next, p2.next   # type:ignore
        
        p1.next = p1.next.next          # type:ignore

        return h0.next


# Put nodes in an array: Space complexity: O(n)
class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = [ListNode(next=head)]
        p = head
        while p != None:
            nodes.append(p)
            p = p.next

        if n < len(nodes):
            nodes[-1 - n].next = nodes[- n].next

        return nodes[0].next


if __name__ == "__main__":
    def unitTest(sol):
        h1 = ListNodeUtil.createLinkedList([1, 2, 3, 4, 5])
        h2 = Solution().removeNthFromEnd(h1, 2)
        lst = ListNodeUtil.toArrayList(h2)
        print(lst)
        assert lst == [1, 2, 3, 5]

        h1 = ListNodeUtil.createLinkedList([1])
        h2 = Solution().removeNthFromEnd(h1, 1)
        lst = ListNodeUtil.toArrayList(h2)
        print(lst)
        assert lst == []

        h1 = ListNodeUtil.createLinkedList([1, 2])
        h2 = Solution().removeNthFromEnd(h1, 1)
        lst = ListNodeUtil.toArrayList(h2)
        print(lst)
        assert lst == [1]

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
