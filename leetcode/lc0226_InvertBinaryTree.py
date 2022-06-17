# Given the root of a binary tree, invert the tree, and return its root.
# Constraints:
#   The number of nodes in the tree is in the range [0, 100].
#   -100 <= Node.val <= 100
from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


class Solution1:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            # Wrong! need temp variable
            # root.left = self.invertTree(root.right)
            # root.right = self.invertTree(root.left)
            temp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(temp)

        return root


if __name__ == '__main__':
    def unitTest(sol):
        root = TreeNodeUtil.fromBfsList([4,2,7,1,3,6,9])
        r = TreeNodeUtil.toBfsList(sol.invertTree(root))
        print(r)
        assert r == [4,7,2,9,6,3,1]

        root = TreeNodeUtil.fromBfsList([2,1,3])
        r = TreeNodeUtil.toBfsList(sol.invertTree(root))
        print(r)
        assert r == [2,3,1]

        root = TreeNodeUtil.fromBfsList([])
        r = TreeNodeUtil.toBfsList(sol.invertTree(root))
        print(r)
        assert r == []

    unitTest(Solution())
    unitTest(Solution1())
