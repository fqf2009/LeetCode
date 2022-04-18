# Given a root of an N-ary tree, you need to compute the length of
# the diameter of the tree.
# The diameter of an N-ary tree is the length of the longest path
# between any two nodes in the tree. This path may or may not pass
# through the root.
# (Nary-Tree input serialization is represented in their level order
# traversal, each group of children is separated by the None value.)

# Constraints:
#   The depth of the n-ary tree is less than or equal to 1000.
#   The total number of nodes is between [1, 10^4].
from typing import Optional, List
from collections import deque
import heapq


# Definition for a Node.
class Node:
    def __init__(self, val=-1, children=None):
        self.val: int = val
        self.children: list = children if children is not None else []

    @staticmethod
    def fromBfsList(nums: List[Optional[int]]) -> Optional['Node']:
        n = len(nums)
        if n == 0:
            return None
        root = Node(nums[0])
        dq = deque([root])
        i = 2
        while i < n:
            node = dq.popleft()
            if i < n and nums[i] == None:
                i += 1
            while i < n and nums[i] != None:
                dq.append(Node(nums[i]))
                node.children.append(dq[-1])
                i += 1

        return root


# DFS + Recursion + N-Ary Tree, O(n)
# - Optimize: save max diameter during DFS visit, only return depth to parent node
class Solution:
    def diameter(self, root: 'Node') -> int:
        def dfs_visit(root: Node):
            depths = heapq.nlargest(2, [dfs_visit(node) for node in root.children])
            nonlocal diameter
            diameter = max(diameter, sum(depths) + len(depths))
            return depths[0] + 1 if depths else 0

        diameter = 0
        dfs_visit(root)
        return diameter


# DFS + Recursion + N-Ary Tree, O(n)
# - heapq.nlargest() is better than list.sort()
class Solution1:
    def diameter(self, root: 'Node') -> int:
        def depth_n_diameter(root: Node):
            n = len(root.children)
            if n == 0:
                return (0, 0)
            depths = []
            diameters = []
            for node in root.children:
                dd = depth_n_diameter(node)
                depths.append(dd[0])
                diameters.append(dd[1])
            if n == 1:
                return (depths[0]+1, max(depths[0]+1, diameters[0]))
            else:
                depths = heapq.nlargest(2, depths)
                return(depths[0]+1, max(depths[0]+depths[1]+2, max(diameters)))

        return depth_n_diameter(root)[1]


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,), (Solution1,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([3, None, 1, None, 5], 2),
            ([1, None, 3, 2, 4, None, 5, 6], 3),
            ([1, None, 2, None, 3, 4, None, 5, None, 6], 4),
            ([1, None, 2, 3, 4, 5, None, None, 6, 
              7, None, 8, None, 9, 10, None, None, 
              11, None, 12, None, 13, None, None, 14], 7),
        ])
        def test_diameter(self, lst, expected):
            sol = self.solution()       # type:ignore
            root = Node.fromBfsList(lst)
            r = sol.diameter(root)
            self.assertEqual(r, expected)

    main()
