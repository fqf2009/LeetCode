# Given a binary tree root and an integer target, delete all
# the leaf nodes with value target.

# Note that once you delete a leaf node with value target, if
# its parent node becomes a leaf node and has the value target,
# it should also be deleted (you need to continue doing that
# until you cannot).

# Constraints:
#   The number of nodes in the tree is in the range [1, 3000].
#   1 <= Node.val, target <= 1000
from lib.TreeUtil import TreeNode, TreeNodeUtil
from typing import Optional


# DFS + Recursion + Tree: T/S - O(n)/O(n)
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfsClean(root: TreeNode) -> bool:
            if root.left and dfsClean(root.left):
                root.left = None
            if root.right and dfsClean(root.right):
                root.right = None
            return root.val == target and not root.left and not root.right
        
        return None if root and dfsClean(root) else root


if __name__ == '__main__':
    def unitTest(sol):
        root = TreeNodeUtil.fromBfsList([1, 2, 3, 2, None, 2, 4])
        target = 2
        r = TreeNodeUtil.toBfsList(sol.removeLeafNodes(root, target))
        print(r)
        assert r == [1, None, 3, None, 4]

        root = TreeNodeUtil.fromBfsList([1, 3, 3, 3, 2])
        target = 3
        r = TreeNodeUtil.toBfsList(sol.removeLeafNodes(root, target))
        print(r)
        assert r == [1, 3, None, None, 2]

        root = TreeNodeUtil.fromBfsList([1, 2, None, 2, None, 2])
        target = 2
        r = TreeNodeUtil.toBfsList(sol.removeLeafNodes(root, target))
        print(r)
        assert r == [1]

    unitTest(Solution())
