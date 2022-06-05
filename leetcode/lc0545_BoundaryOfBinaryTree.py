# The boundary of a binary tree is the concatenation of the root, the
# left boundary, the leaves ordered from left-to-right, and the reverse
# order of the right boundary.

# The left boundary is the set of nodes defined by the following:
#  - The root node's left child is in the left boundary. If the root does not
#    have a left child, then the left boundary is empty.
#  - If a node in the left boundary and has a left child, then the left
#    child is in the left boundary.
#  - If a node is in the left boundary, has no left child, but has a right
#    child, then the right child is in the left boundary.
#  - The leftmost leaf is not in the left boundary.

# The right boundary is similar to the left boundary, except it is the
# right side of the root's right subtree. Again, the leaf is not part of
# the right boundary, and the right boundary is empty if the root does not
# have a right child.

# The leaves are nodes that do not have any children. For this problem,
# the root is not a leaf.
# Given the root of a binary tree, return the values of its boundary.

# Constraints:
#   The number of nodes in the tree is in the range [1, 10^4].
#   -1000 <= Node.val <= 1000
from lib.TreeUtil import TreeNode, TreeNodeUtil
from typing import List, Optional


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def leftBoundary(root: Optional[TreeNode]):
            if root and (root.left or root.right):
                res.append(root.val)  # pre-order
                if root.left:
                    leftBoundary(root.left)
                else:
                    leftBoundary(root.right)

        def rightBoundary(root: Optional[TreeNode]):
            if root and (root.left or root.right):
                if root.right:
                    rightBoundary(root.right)
                else:
                    rightBoundary(root.left)
                res.append(root.val)  # post-order (to reverse the result)

        def leaves(root: Optional[TreeNode]):
            if root:
                if not root.left and not root.right:
                    res.append(root.val)
                else:
                    leaves(root.left)
                    leaves(root.right)

        if root:
            res.append(root.val)
            leftBoundary(root.left)
            leaves(root.left)
            leaves(root.right)
            rightBoundary(root.right)

        return res


if __name__ == "__main__":

    def unit_test(solution):
        print(solution.__name__)
        sol = solution()

        root = TreeNodeUtil.fromBfsList([1, None, 2, 3, 4])
        r = sol.boundaryOfBinaryTree(root)
        print(r)
        assert r == [1, 3, 4, 2]

        root = TreeNodeUtil.fromBfsList([1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10])
        r = sol.boundaryOfBinaryTree(root)
        print(r)
        assert r == [1, 2, 4, 7, 8, 9, 10, 6, 3]

    unit_test(Solution)
