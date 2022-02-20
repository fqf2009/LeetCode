# A path in a binary tree is a sequence of nodes where each
# pair of adjacent nodes in the sequence has an edge connecting
# them. A node can only appear in the sequence at most once. Note
# that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any
# non-empty path.

# Constraints:
#   The number of nodes in the tree is in the range [1, 3 * 10^4].
#   -1000 <= Node.val <= 1000
from lib.TreeUtil import TreeNode, TreeNodeUtil
from typing import List, Optional, Tuple
from functools import cache


# DFS: O(n)
# - the helper function dfs(), returns a tuple of two integers:
#   res[0] is the max sum of extendable path - parent node can extend this path
#   res[1] is the max sum of non-extendable path - parent node cannot extend this path
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> Tuple[int, int]:
            if not root: return (-2**31, -2**31)
            ls = dfs(root.left)
            rs = dfs(root.right)
            maxExtendable =  max(ls[0], rs[0], 0) + root.val
            maxNonExtendable = max(max(ls), max(rs), ls[0] + rs[0] + root.val, maxExtendable)
            return (maxExtendable, maxNonExtendable)

        return max(dfs(root))


if __name__ == '__main__':
    def unitTest(sol):
        root = TreeNodeUtil.fromBfsList([-2,1])
        r = sol.maxPathSum(root)
        print(r)
        assert r == 1

        root = TreeNodeUtil.fromBfsList([1, 2, 3])
        r = sol.maxPathSum(root)
        print(r)
        assert r == 6

        root = TreeNodeUtil.fromBfsList([-3])
        r = sol.maxPathSum(root)
        print(r)
        assert r == -3

        root = TreeNodeUtil.fromBfsList([-10, 9, 20, None, None, 15, 7])
        r = sol.maxPathSum(root)
        print(r)
        assert r == 42

    unitTest(Solution())
