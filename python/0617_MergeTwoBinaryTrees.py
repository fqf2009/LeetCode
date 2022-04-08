# You are given two binary trees root1 and root2.

# Imagine that when you put one of them to cover the other, some
# nodes of the two trees are overlapped while the others are not.
# You need to merge the two trees into a new binary tree. The merge
# rule is that if two nodes overlap, then sum node values up as the
# new value of the merged node. Otherwise, the NOT None node will
# be used as the node of the new tree.

# Return the merged tree.
# Note: The merging process must start from the root nodes of both trees.

# Constraints:
#  - The number of nodes in both trees is in the range [0, 2000].

from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil

# DFS + Recursion
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        if not root1:
            root1 = TreeNode(0) # dummy node for less coding
        if not root2:
            root2 = TreeNode(0) # dummy node for less coding
        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)

        return root


if __name__ == "__main__":
    def unitTest(sol):
        root1 = TreeNodeUtil.fromBfsList([1, 3, 2, 5])
        root2 = TreeNodeUtil.fromBfsList([2, 1, 3, None, 4, None, 7])
        root = sol.mergeTrees(root1, root2)
        r = TreeNodeUtil.toBfsList(root)
        print(r)
        assert r == [3, 4, 5, 5, 4, None, 7]

        root1 = TreeNodeUtil.fromBfsList([1])
        root2 = TreeNodeUtil.fromBfsList([1, 2])
        root = sol.mergeTrees(root1, root2)
        r = TreeNodeUtil.toBfsList(root)
        print(r)
        assert r == [2, 2]

    unitTest(Solution())
