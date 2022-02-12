# A linked list of length n is given such that each node contains an additional
# random pointer, which could point to any node in the list, or None.

# Construct a deep copy of the list. The deep copy should consist of exactly n
# brand new nodes, where each new node has its value set to the value of its
# corresponding original node. Both the next and random pointer of the new nodes
# should point to new nodes in the copied list such that the pointers in the original
# list and copied list represent the same list state. None of the pointers in the new
# list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where
# X.random --> Y, then for the corresponding two nodes x and y in the copied list,
# x.random --> y. 

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. 
# Each node is represented as a pair of [val, random_index] where:
#  - val: an integer representing Node.val
#  - random_index: the index of the node (range from 0 to n-1) that the random 
#    pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.
# Constraints:
#   0 <= n <= 1000

from typing import Optional, List


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    @staticmethod
    def arrayToRandList(arr: List[List[int]]) -> Optional['Node']:
        if len(arr) == 0:
            return None

        nodes = []
        for val, *_ in arr:
            nodes.append(Node(val))

        for i in range(len(arr)):
            if i < len(arr) - 1:
                nodes[i].next = nodes[i + 1]
            if arr[i][1] != None:
                nodes[i].random = nodes[arr[i][1]]

        return nodes[0]

    @staticmethod
    def randListToArray(head: Optional['Node']) -> List[List[int]]:
        nodes = {}
        p = head
        i = 0
        while p:
            nodes[p] = i
            p = p.next
            i += 1

        res = []
        p = head
        while p:
            idx = nodes[p.random] if p.random else None
            res.append([p.val, idx])
            p = p.next

        return res

# Deep copy already use space O(n), so why case about wasting another n space?
# - map original list of nodes in a dict, so each node has a number (i-th node)
# - duplicate nodes into list.
# - set random value for new nodes in list, based on info from dict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        oldNodes = {}   # waste a little space here
        p = head
        i = 0
        while p:
            oldNodes[p] = i
            p = p.next
            i += 1
        
        newNodes = []   # waste a little space here
        p = head
        dummyHead = p1 = Node(-1)
        while p:
            p1.next = Node(p.val)
            p1 = p1.next
            newNodes.append(p1)
            p = p.next

        p = head
        i = 0
        while p:
            if p.random:
                newNodes[i].random = newNodes[oldNodes[p.random]]
            p = p.next
            i += 1

        return dummyHead.next


# Algorithm: O(n)
#  - First pass, copy the list nodes, with each new node being inserted
#    just after original node.
#    From: A ->      B (r->A)             -> C      ...
#    To  : A -> a -> B (r->A) -> b (r->A) -> C -> c ...
#  - Sedond pass, compute random value for new nodes.
#    From: A -> a -> B (r->A) -> b (r->A) -> C -> c ...
#    To  : A -> a -> B (r->A) -> b (r->a) -> C -> c ...
#  - Third pass, detatch new nodes from original list.
#    To  : A -> B (r->A) -> C ...
#        : a -> b (r->a) -> c
class Solution1:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        p = head
        while p:
            p.next = Node(p.val, p.next)
            p = p.next.next

        p = head
        while p:
            assert p.next
            if p.random:
                p.next.random = p.random.next
            p = p.next.next

        headNew = head.next
        p, p1 = head, head.next
        while p:
            assert p1
            p.next = p1.next
            p = p.next
            if p:
                p1.next = p.next
                p1 = p1.next

        return headNew


if __name__ == '__main__':
    def unitTest(sol):
        h0 = Node.arrayToRandList([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]) #type:ignore
        h1 = sol.copyRandomList(h0)
        r = Node.randListToArray(h1)
        print(r)
        assert(r == [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])

        h0 = Node.arrayToRandList([[1, 1], [2, 1]])
        h1 = sol.copyRandomList(h0)
        r = Node.randListToArray(h1)
        print(r)
        assert(r == [[1, 1], [2, 1]])

        h0 = Node.arrayToRandList([[3, None], [3, 0], [3, None]]) #type:ignore
        h1 = sol.copyRandomList(h0)
        r = Node.randListToArray(h1)
        print(r)
        assert(r == [[3, None], [3, 0], [3, None]])

    unitTest(Solution())
    unitTest(Solution1())
