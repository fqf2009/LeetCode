from lib.ListUtil import ListNode, ListNodeUtil
from typing import Optional

# Given the head of a linked list, remove the nth node from the end of 
# the list and return its head.


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


# Put nodes in an array: Space complexity: O(n)
class Solution1:
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
        assert(lst == [1, 2, 3, 5])

        h1 = ListNodeUtil.createLinkedList([1])
        h2 = Solution().removeNthFromEnd(h1, 1)
        lst = ListNodeUtil.toArrayList(h2)
        print(lst)
        assert(lst == [])

        h1 = ListNodeUtil.createLinkedList([1, 2])
        h2 = Solution().removeNthFromEnd(h1, 1)
        lst = ListNodeUtil.toArrayList(h2)
        print(lst)
        assert(lst == [1])

    unitTest(Solution())
    unitTest(Solution1())
