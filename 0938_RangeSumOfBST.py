# Given the root node of a binary search tree and two integers
# low and high, return the sum of values of all nodes with a
# value in the inclusive range [low, high].
# Constraints:
# The number of nodes in the tree is in the range [1, 2 * 10^4].
#   1 <= Node.val <= 10^5
#   1 <= low <= high <= 10^5
#   All Node.val are unique.
from typing import List, Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


# Tree + DFS
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        leftSum = self.rangeSumBST(root.left, low, high) if root.val > low else 0
        rightSum = self.rangeSumBST(root.right, low, high) if root.val < high else 0
        midVal = root.val if low <= root.val <= high else 0
        return leftSum + midVal + rightSum


if __name__ == '__main__':
    def unitTest(sol):
        root = TreeNodeUtil.fromBfsList([10, 5, 15, 3, 7, None, 18])
        r = sol.rangeSumBST(root, 7, 15)
        print(r)
        assert r == 32

        root = TreeNodeUtil.fromBfsList([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
        r = sol.rangeSumBST(root, 6, 10)
        print(r)
        assert r == 23

    unitTest(Solution())
