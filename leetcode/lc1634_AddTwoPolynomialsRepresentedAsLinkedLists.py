# A polynomial linked list is a special type of linked list where every
# node represents a term in a polynomial expression.
# Each node has three attributes:
#  - coefficient: an integer representing the number multiplier of the term.
#    The coefficient of the term 9x4 is 9.
#  - power: an integer representing the exponent. The power of the term 9x^4 is 4.
#  - next: a pointer to the next node in the list, or null if it is the last node
#    of the list.
# The polynomial linked list must be in its standard form: the polynomial
# must be in strictly descending order by its power value. Also, terms with a
# coefficient of 0 are omitted.
#
# Given two polynomial linked list heads, poly1 and poly2, add the polynomials
# together and return the head of the sum of the polynomials.
#
# PolyNode format:
#   The input/output format is as a list of n nodes, where each node is
#   represented as its [coefficient, power]. For example, the polynomial
#   5x^3 + 4x - 7 would be represented as: [[5,3],[4,1],[-7,0]].

# Constraints:
#   0 <= n <= 10^4
#   -10^9 <= PolyNode.coefficient <= 10^9
#   PolyNode.coefficient != 0
#   0 <= PolyNode.power <= 10^9
#   PolyNode.power > PolyNode.next.power

from typing import List, Optional


class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next: Optional[PolyNode] = next

    @staticmethod
    def fromList(poly: List[List[int]]) -> Optional['PolyNode']:
        node = None
        for c, p in poly[::-1]:
            node = PolyNode(c, p, node)
        return node

    @staticmethod
    def toList(node) -> List[List[int]]:
        res = []
        while node:
            res.append([node.coefficient, node.power])
            node = node.next

        return res


class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> Optional['PolyNode']:
        head = p = PolyNode()
        while poly1 or poly2:
            c1 = poly1.coefficient if poly1 else 0
            p1 = poly1.power if poly1 else -1
            c2 = poly2.coefficient if poly2 else 0
            p2 = poly2.power if poly2 else -1
            if p1 > p2:
                p.next = PolyNode(c1, p1)
                p = p.next
                poly1 = poly1.next  #type:ignore
            elif p1 < p2:
                p.next = PolyNode(c2, p2)
                p = p.next
                poly2 = poly2.next  #type:ignore
            else:
                if c1 + c2 != 0:
                    p.next = PolyNode(c1 + c2, p1)
                    p = p.next
                poly1 = poly1.next  #type:ignore
                poly2 = poly2.next  #type:ignore

        return head.next


if __name__ == "__main__":
    def unitTest(sol):
        poly1 = PolyNode.fromList([[1, 1]])
        poly2 = PolyNode.fromList([[1, 0]])
        r = PolyNode.toList(sol.addPoly(poly1, poly2))
        print(r)
        assert r == [[1, 1], [1, 0]]

        poly1 = PolyNode.fromList([[2, 2], [4, 1], [3, 0]])
        poly2 = PolyNode.fromList([[3, 2], [-4, 1], [-1, 0]])
        r = PolyNode.toList(sol.addPoly(poly1, poly2))
        print(r)
        assert r == [[5, 2], [2, 0]]

        poly1 = PolyNode.fromList([[1, 2]])
        poly2 = PolyNode.fromList([[-1, 2]])
        r = PolyNode.toList(sol.addPoly(poly1, poly2))
        print(r)
        assert r == []

    unitTest(Solution())
