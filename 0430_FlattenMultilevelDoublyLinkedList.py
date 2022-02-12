# You are given a doubly linked list, which contains nodes that
# have a next pointer, a previous pointer, and an additional child
# pointer. This child pointer may or may not point to a separate
# doubly linked list, also containing these special nodes. These
# child lists may have one or more children of their own, and so on,
# to produce a multilevel data structure as shown in the example below.

# Given the head of the first level of the list, flatten the list so
# that all the nodes appear in a single-level, doubly linked list. Let
# a node with a child list. The nodes in the child list should appear
# curr be after curr and before curr.next in the flattened list.

# Return the head of the flattened list. The nodes in the list must have
# all of their child pointers set to null.

# Constraints:
#  - The number of Nodes will not exceed 1000.

# How the multilevel linked list is represented in test cases:
#  [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
#  means:
#  [1,    2,    3,    4,   5,   6,  null]
#               |
#  [null, null, 7,    8,   9,   10, null]
#                     |
#  [            null, 11,  12,  null] <- tailing null will be removed in serialization

# !!!Obviously this serialization/de-serialization model has issue!!!
# - if the node(4) has a child list, say [13, 14, null],
# - after serialization, we get:
#   [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,null,null,13,14,null,null,11,12]
# - after de-serialization, we get:
#  [1,    2,    3,    4,    5,    6,  null]
#               |
#  [null, null, 7,    8,    9,    10, null]
#                     |
#  [            null, null, null, 13, 14, null]
#                                     |
#  [                            null, 11,  12,  null]

# !!! the test case below will instead use multi-level list as input.

# Sample java implementation from LeetCode discuss forum:
# - code is a little hard to read
# - tail is an instance member field, not method local variable,
#   so it relies on some global state saved from last call.
# - all nodes are added via recursive invoking flatten(), this means
#   the recursive level will be the depth of deepest leaf.
"""
class Solution {
    Node tail = null;

    public Node flatten(Node head) {
        if(head == null) return null;

        head.prev = tail;
        tail = head;

        Node nextNode = head.next;

        head.next = flatten(head.child);
        head.child = null;

        tail.next = flatten(nextNode);

        return head;
    }
}
"""

from typing import List, Optional

# Definition for a Node.


class Node:
    def __init__(self, val=-1, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    @staticmethod
    def serialize(head: Optional['Node']):
        res = []
        while head:
            res.append(head.val)
            if head.child:
                res.append(Node.serialize(head))
            head = head.next
        return res

    @staticmethod
    def deserialize(nodes: list) -> 'Optional[Node]':
        if len(nodes) == 0:
            return None
        h = p = Node(val=nodes[0])
        for v in nodes[1:]:
            if isinstance(v, list):
                p.child = Node.deserialize(v)
            else:
                p.next = Node(val=v)
                p.next.prev = p
                p = p.next
        return h


# Recursion, depth only relies on the level of child.
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def flattenHelper(head: Node) -> Node:  # return tail node
            while head:
                tail = head
                if head.child:
                    t1 = flattenHelper(head.child)
                    t1.next = head.next
                    if head.next:
                        head.next.prev = t1
                    head.child.prev = head
                    head.next = head.child
                    head.child = None
                    tail = t1
                head = tail.next    #type:ignore
            return tail             #type:ignore
        
        if head:
            flattenHelper(head)
        return head


if __name__ == "__main__":
    def unitTest(sol):
        head1 = Node.deserialize([1, 2, 3, [7, 8, [11, 12], 9, 10], 4, 5, 6])
        head2 = sol.flatten(head1)
        r = Node.serialize(head2)
        print(r)
        assert r == [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]

        head1 = Node.deserialize([1, [3], 2])
        head2 = sol.flatten(head1)
        r = Node.serialize(head2)
        print(r)
        assert r == [1, 3, 2]

        head1 = Node.deserialize([])
        head2 = sol.flatten(head1)
        r = Node.serialize(head2)
        print(r)
        assert r == []

    unitTest(Solution())
