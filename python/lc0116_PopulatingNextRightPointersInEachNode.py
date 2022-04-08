# You are given a perfect binary tree where all leaves are on the same
# level, and every parent has two children. The binary tree has the
# following definition:
#   struct Node {
#     int val;
#     Node *left;
#     Node *right;
#     Node *next;
#   }
# Populate each next pointer to point to its next right node. If there
# is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.
# Constraints:
#  - The number of nodes in the tree is in the range [0, 2^12 - 1].
from typing import Optional, List
from collections import deque

# Definition for a Node.


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    @staticmethod
    def fromBfsList(nums: List[int]) -> Optional['Node']:
        if len(nums) == 0:
            return None
        root = Node(nums[0])
        dq = deque()
        dq.append(root)
        isLeft = True
        for n in nums[1:]:
            node = dq[0]
            if isLeft:
                if n != None:
                    node.left = Node(n)
                    dq.append(node.left)
            else:
                if n != None:
                    node.right = Node(n)
                    dq.append(node.right)
                dq.popleft()
            isLeft = not isLeft

        return root

    @staticmethod
    def toBfsNextList(root: Optional['Node']) -> list[object]:
        res = []
        head = root     # head of nodes in the same level
        while head:
            node = head
            while node:
                res.append(node.val)
                node = node.next
            res.append('#')
            head = head.left

        return res


# BFS - T/S: O(n), O(n)
# - when using queue to save child nodes, also save the level number
# - when pop-up node from queue, set next to the node of the same level
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        dq = deque()
        dq.append((root, 0))
        while len(dq) > 0:
            node, level = dq.popleft()
            node.next = dq[0][0] if len(dq) > 0 and dq[0][1] == level else None
            if node.left:
                dq.append((node.left, level + 1))
            if node.right:
                dq.append((node.right, level + 1))

        return root


if __name__ == "__main__":
    def unitTest(sol):
        root1 = Node.fromBfsList([1, 2, 3, 4, 5, 6, 7])
        root2 = sol.connect(root1)
        r = Node.toBfsNextList(root2)
        print(r)
        assert r == [1, '#', 2, 3, '#', 4, 5, 6, 7, '#']

        root1 = Node.fromBfsList([])
        root2 = sol.connect(root1)
        r = Node.toBfsNextList(root2)
        print(r)
        assert r == []

    unitTest(Solution())
