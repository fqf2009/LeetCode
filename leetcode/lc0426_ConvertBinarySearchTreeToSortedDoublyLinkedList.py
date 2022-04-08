# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
# You can think of the left and right pointers as synonymous to the predecessor
# and successor pointers in a doubly-linked list. For a circular doubly linked
# list, the predecessor of the first element is the last element, and the
# successor of the last element is the first element.
# We want to do the transformation in place. After the transformation, the
# left pointer of the tree node should point to its predecessor, and the
# right pointer should point to its successor. You should return the pointer
# to the smallest element of the linked list.
# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
#   -1000 <= Node.val <= 1000
#   All the values of the tree are unique.
from typing import List, Optional, Tuple
from lib.TreeUtil import TreeNode as Node, TreeNodeUtil


# Binary Search Tree + DFS: O(n)
class Solution:
    def treeToDoublyList(self, root: "Optional[Node]") -> "Optional[Node]":
        def dfsTravel(root: Node) -> Tuple[Node, Node]:  # (smallest, largest)
            if root.left:
                left1, left2 = dfsTravel(root.left)
                left2.right = root
                root.left = left2
                smallest = left1
            else:
                smallest = root

            if root.right:
                right1, right2 = dfsTravel(root.right)
                right1.left = root
                root.right = right1
                largest = right2
            else:
                largest = root

            return (smallest, largest)

        if not root:
            return None
        smallest, largest = dfsTravel(root)
        smallest.left = largest
        largest.right = smallest

        return smallest

    def linkedListToList(self, head: Optional[Node]) -> List[int]:
        if not head:
            return []

        res = []
        p = head
        while p:
            res.append(p.val)
            p = p.right
            if p == head:
                break

        return res


if __name__ == "__main__":

    def unit_test(sol):
        root = TreeNodeUtil.fromBfsList([4, 2, 5, 1, 3])
        head = sol.treeToDoublyList(root)
        r = sol.linkedListToList(head)
        print(r)
        assert r == [1, 2, 3, 4, 5]

        root = TreeNodeUtil.fromBfsList([2, 1, 3])
        head = sol.treeToDoublyList(root)
        r = sol.linkedListToList(head)
        print(r)
        assert r == [1, 2, 3]

    unit_test(Solution())
