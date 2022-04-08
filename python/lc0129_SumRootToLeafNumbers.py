# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated
# so that the answer will fit in a 32-bit integer.
# A leaf node is a node with no children.
# Constraints:
#   The number of nodes in the tree is in the range [1, 1000].
#   0 <= Node.val <= 9
#   The depth of the tree will not exceed 10.
from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs_sum(node: Optional[TreeNode], path_val: int) -> int:
            if not node:
                return 0
            path_val = path_val * 10 + node.val

            if node.left or node.right:
                return dfs_sum(node.left, path_val) + dfs_sum(node.right, path_val)
            else:
                return path_val

        return dfs_sum(root, 0)


# Tree, Recursion, DFS: O(n)
class Solution1:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfsSumNumbers(node: TreeNode, path_val: int) -> int:
            path_val = path_val * 10 + node.val
            res1, res2 = 0, 0
            if node.left == None and node.right == None:
                return path_val
            if node.left:
                res1 = dfsSumNumbers(node.left, path_val)
            if node.right:
                res2 = dfsSumNumbers(node.right, path_val)
            return res1 + res2

        if not root:
            return 0
        return dfsSumNumbers(root, 0)


if __name__ == "__main__":

    def unit_test(sol):
        r1 = TreeNodeUtil.fromBfsList([1, 2, 3])
        s = sol.sumNumbers(r1)
        print(s)
        assert s == 25

        r1 = TreeNodeUtil.fromBfsList([4, 9, 0, 5, 1])
        s = sol.sumNumbers(r1)
        print(s)
        assert s == 1026

    unit_test(Solution())
