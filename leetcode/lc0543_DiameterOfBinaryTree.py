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
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth_and_diameter(root: Optional[TreeNode]) -> tuple[int, int]:
            if not root:
                return (-1, 0)
            left_depth, left_diameter = depth_and_diameter(root.left)
            right_depth, right_diameter = depth_and_diameter(root.right)
            depth = max(left_depth, right_depth) + 1
            diameter = max(left_depth + right_depth + 2, left_diameter, right_diameter)
            return (depth, diameter)

        return depth_and_diameter(root)[1]


if __name__ == "__main__":

    def unit_test(sol):
        root = TreeNodeUtil.fromBfsList([1, 2, 3, 4, 5])
        r = sol.diameterOfBinaryTree(root)
        print(r)
        assert r == 3

        root = TreeNodeUtil.fromBfsList([1, 2])
        r = sol.diameterOfBinaryTree(root)
        print(r)
        assert r == 1

    unit_test(Solution())
