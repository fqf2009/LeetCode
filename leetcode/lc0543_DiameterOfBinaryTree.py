# Given the root of a binary tree, return the length of the
# diameter of the tree.
# The diameter of a binary tree is the length of the longest path between
# any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of
# edges between them.
# Constraints:
#   The number of nodes in the tree is in the range [1, 10^4].
#   -100 <= Node.val <= 100
from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


# Binary Tree + DFS: O(n)
# - Optimize: save max diameter during DFS visit, only return depth to parent node
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs_visit(root: Optional[TreeNode]) -> int:
            if not root: return -1
            depths = [dfs_visit(root.left), dfs_visit(root.right)]
            nonlocal diameter
            diameter = max(diameter, sum(d+1 for d in depths if d >= 0))
            return max(depths) + 1

        diameter = 0
        dfs_visit(root)
        return diameter


class Solution0:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfsVisit(root):     # return depth
            nonlocal res
            if not root: return 0
            ldepth = dfsVisit(root.left)
            rdepth = dfsVisit(root.right)
            res = max(res, ldepth + rdepth)
            return max(ldepth, rdepth) + 1

        dfsVisit(root)
        return res


# Binary Tree + DFS: O(n)
class Solution1:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth_and_diameter(root: Optional[TreeNode]) -> tuple[int, int]:
            if not root:
                return (-1, 0)
            left_depth, left_diameter = depth_and_diameter(root.left)
            right_depth, right_diameter = depth_and_diameter(root.right)
            diameter = max(left_depth + right_depth + 2, left_diameter, right_diameter)
            return (max(left_depth, right_depth) + 1, diameter)

        return depth_and_diameter(root)[1]


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,), (Solution0,), (Solution1,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([1, 2, 3, 4, 5], 3),
            ([1, 2], 1),
        ])
        def test_diameterOfBinaryTree(self, lst, expected):
            sol = self.solution()       # type:ignore
            root = TreeNodeUtil.fromBfsList(lst)
            r = sol.diameterOfBinaryTree(root)
            self.assertEqual(r, expected)

    main()
