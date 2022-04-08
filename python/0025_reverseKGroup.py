from typing import Optional
from lib.ListUtil import ListNode, ListNodeUtil

# Given the head of a linked list, reverse k nodes (of the list) at a time, and
# return the modified list. k is a positive integer and is less than or equal to
# the length of the linked list. If the number of nodes is not a multiple of k
# then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the nodes, only nodes themselves may be changed.

# Array version of reverse K group:
# def reverseKGroup(arr, k):
#     for i in range(0, len(arr), k):
#         arr[i:i+k] = arr[i:i+k][::-1]
#     return arr


# Slight improvement, only the last portion of nodes (less than k) need visit twice
# Time complexity: O(n)
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # reverse K nodes in place, return the number of nodes reversed
        def reverseKNodes(dummyHead: ListNode) -> int:
            p = newTail = dummyHead.next
            newChain = None
            n = 0
            while p and n < k:
                p1 = p.next
                p.next = newChain
                newChain = p
                p = p1
                n += 1

            dummyHead.next = newChain
            newTail.next = p        #type:ignore
            return n

        if k == 1:
            return head
        h0 = p = ListNode(next=head)
        while p.next:
            newTail = p.next
            n = reverseKNodes(p)
            if n < k:
                reverseKNodes(p)
                break
            p = newTail
        
        return h0.next


# In place reverse list every k nodes: O(n)
class Solution1:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseKNodes(head: ListNode, postTail: Optional[ListNode]):
            p, p1 = head, head.next
            while p1 != postTail:
                assert(p1)
                p2 = p1
                p1 = p1.next
                p2.next = p
                p = p2

            head.next = postTail
            return (p, head)

        if k <= 1 or head == None:
            return head

        h0 = p1 = ListNode(-1, head)
        p2 = head
        while p1:
            i = 0
            for i in range(k):
                if p2 == None:
                    return h0.next
                p2 = p2.next
            assert(p1.next)
            p1.next, tail = reverseKNodes(p1.next, p2)
            p1 = tail

        return h0.next


if __name__ == '__main__':
    def unitTest(sol):
        h1 = ListNodeUtil.createLinkedList([1, 2, 3, 4, 5])
        h2 = sol.reverseKGroup(h1, 2)
        r = ListNodeUtil.toArrayList(h2)
        print(r)
        assert(r == [2, 1, 4, 3, 5])

        h1 = ListNodeUtil.createLinkedList([1, 2, 3, 4, 5])
        h2 = sol.reverseKGroup(h1, 3)
        r = ListNodeUtil.toArrayList(h2)
        print(r)
        assert(r == [3, 2, 1, 4, 5])

    unitTest(Solution())
    unitTest(Solution1())
