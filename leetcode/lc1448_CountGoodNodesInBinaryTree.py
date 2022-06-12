# Given a binary tree root, a node X in the tree is named good if in
# the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.
# Constraints:
#   The number of nodes in the binary tree is in the range [1, 10^5].
#   Each node's value is between [-10^4, 10^4].
from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: Optional[TreeNode], maxVal: int) -> int:
            if not root:
                return 0
            res = 0
            if root.val >= maxVal:
                res = 1
                maxVal = root.val
            return res + dfs(root.left, maxVal) + dfs(root.right, maxVal)

        return dfs(root, -(10**5))


if __name__ == "__main__":

    def unit_test(sol):
        root = TreeNodeUtil.fromBfsList([3, 1, 4, 3, None, 1, 5])
        r = sol.goodNodes(root)
        print(r)
        assert r == 4

        root = TreeNodeUtil.fromBfsList([3, 3, None, 4, 2])
        r = sol.goodNodes(root)
        print(r)
        assert r == 3

        root = TreeNodeUtil.fromBfsList([1])
        r = sol.goodNodes(root)
        print(r)
        assert r == 1

    unit_test(Solution())
