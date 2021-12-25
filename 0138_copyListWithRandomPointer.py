from typing import Optional, List

# A linked list of length n is given such that each node contains an additional
# random pointer, which could point to any node in the list, or None.
# Construct a deep copy of the list. The deep copy should consist of exactly n
# brand new nodes, where each new node has its value set to the value of its
# corresponding original node. Both the next and random pointer of the new nodes
# should point to new nodes in the copied list such that the pointers in the original
# list and copied list represent the same list state. None of the pointers in the new
# list should point to nodes in the original list.
# For example, if there are two nodes X and Y in the original list, where X.random --> Y,
# then for the corresponding two nodes x and y in the copied list, x.random --> y.
# Return the head of the copied linked list.


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


# First pass, copy the list nodes, with each new node being inserted just after original node.
#   From: A -> B -> C ...
#   To  : A -> a -> B -> b -> C -> c ...
# Sedond pass, compute random value for new nodes.
# Third pass, detatch new nodes from original list.
#   To  : A -> B -> C ...
#       : a -> b -> c
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        p = head
        while p:
            p.next = Node(p.val, p.next)
            p = p.next.next

        p = head
        while p:
            assert(p.next)
            if p.random:
                p.next.random = p.random.next
            p = p.next.next

        headNew = head.next
        p, p1 = head, head.next
        while p:
            assert(p1)
            p.next = p1.next
            p = p1.next
            if p:
                p1.next = p.next
                p1 = p.next

        return headNew


if __name__ == '__main__':
    sol = Solution()

    h0 = Node.arrayToRandList([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    h1 = sol.copyRandomList(h0)
    r = Node.randListToArray(h1)
    print(r)
    assert(r == [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])

    h0 = Node.arrayToRandList([[1, 1], [2, 1]])
    h1 = sol.copyRandomList(h0)
    r = Node.randListToArray(h1)
    print(r)
    assert(r == [[1, 1], [2, 1]])

    h0 = Node.arrayToRandList([[3, None], [3, 0], [3, None]])
    h1 = sol.copyRandomList(h0)
    r = Node.randListToArray(h1)
    print(r)
    assert(r == [[3, None], [3, 0], [3, None]])
