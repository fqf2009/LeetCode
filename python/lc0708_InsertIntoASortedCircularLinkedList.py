# Given a Circular Linked List node, which is sorted in ascending order,
# write a function to insert a value insertVal into the list such that it
# remains a sorted circular list. The given node can be a reference to any
# single node in the list and may not necessarily be the smallest value in
# the circular list.
# If there are multiple suitable places for insertion, you may choose any
# place to insert the new value. After the insertion, the circular list
# should remain sorted.
# If the list is empty (i.e., the given node is null), you should create
# a new single circular list and return the reference to that single node.
# Otherwise, you should return the originally given node.
# Constraints:
#   The number of nodes in the list is in the range [0, 5 * 10^4].
#   -10^6 <= Node.val, insertVal <= 10^6
from lib.ListUtil import ListNode as Node, ListNodeUtil
from typing import Optional


# Linked List: T/S: O(n), O(1)
# - consider all special situations or edge cases:
#   - empty list:    head is None
#   - only one node: head.next == head
#   - insert between two nodes: p.val <= insertVal <= p.next.val
#   - insert before head (or after tail, the same thing):
#       p.val > p.next.val, and (insertVal <= p.next.val or insertVal >= p.val)
#   - all nodes have the same value, but not the same as insertVal:
#       loop through entire linked list (do...while...), still no way to insert,
#       when p == head again, insert it.
class Solution:
    def insert(self, head: "Optional[Node]", insertVal: int) -> "Node":
        if not head:
            head = Node(val=insertVal)
            head.next = head    # !!!
            return head

        if head.next == head:
            head.next = Node(val=insertVal, next=head)
            return head

        p = head
        while True:
            assert p.next
            if p.val <= insertVal <= p.next.val:
                p.next = Node(val=insertVal, next=p.next)
                break

            if p.val > p.next.val and (insertVal <= p.next.val or insertVal >= p.val):
                p.next = Node(val=insertVal, next=p.next)
                break

            p = p.next
            if p == head:   # like: do...while..., to handle: all nodes with same value
                p.next = Node(val=insertVal, next=p.next)
                break

        return head


if __name__ == "__main__":

    def unit_test(sol):
        head = ListNodeUtil.createCyclicList([3, 4, 1], 0)
        h1 = sol.insert(head, 2)
        r = ListNodeUtil.toArrayList(h1)
        print(r)
        assert r == [3, 4, 1, 2]

        head = ListNodeUtil.createCyclicList([2, 2, 2], 0)
        h1 = sol.insert(head, 2)
        r = ListNodeUtil.toArrayList(h1)
        print(r)
        assert r == [2, 2, 2, 2]

        head = ListNodeUtil.createCyclicList([1], 0)
        h1 = sol.insert(head, 0)
        r = ListNodeUtil.toArrayList(h1)
        print(r)
        assert r == [1, 0]

        h1 = sol.insert(None, 1)
        assert h1.next.next == h1   # type:ignore   # new head must point back to itself
        r = ListNodeUtil.toArrayList(h1)
        print(r)
        assert r == [1]

    unit_test(Solution())
