# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# - The left subtree of a node contains only nodes with keys less than the node's key.
# - The right subtree of a node contains only nodes with keys greater than the node's key.
# - Both the left and right subtrees must also be binary search trees.
# Constraints:
#   The number of nodes in the tree is in the range [1, 10^4].
#   -231 <= Node.val <= 231 - 1
import math
from typing import List, Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


# DFS, recursive
# - simplify the code:
#   just to make sure sub tree is in the range defined by parent/ancestor node
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs_valid(root: Optional[TreeNode], lo = -math.inf, hi = math.inf):
            if not root: return True
            if not lo < root.val < hi: return False

            return ( dfs_valid(root.left, lo, root.val) and     # inherit old boundry and add new boundry
                     dfs_valid(root.right, root.val, hi) )

        return dfs_valid(root)


# DFS, recursive
# - it is a little bit unnecessary to return min, max from sub tree 
class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfsValidBST(root: TreeNode):
            if root.left != None:
                leftMin, leftMax, valid = dfsValidBST(root.left)
                if not valid or leftMax >= root.val:
                    return (leftMin, leftMax, False)
            else:
                leftMin = root.val

            if root.right != None:
                rightMin, rightMax, valid = dfsValidBST(root.right)
                if not valid or rightMin <= root.val:
                    return (rightMin, rightMax, False)
            else:
                rightMax = root.val

            return (leftMin, rightMax, True)

        assert(root != None)
        return dfsValidBST(root)[2]


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,), (Solution1,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([2, 1, 3], True),
            ([5, 1, 4, None, None, 3, 6], False),
        ])
        def test_maximumProduct(self, nums, expected):
            sol = self.solution()       # type:ignore
            root = TreeNodeUtil.fromBfsList(nums)
            r = sol.isValidBST(root)
            self.assertEqual(r, expected)

    main()
