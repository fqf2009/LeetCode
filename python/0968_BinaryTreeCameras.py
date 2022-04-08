# You are given the root of a binary tree. We install cameras on
# the tree nodes where each camera at a node can monitor its parent,
# itself, and its immediate children.
# Return the minimum number of cameras needed to monitor all nodes
# of the tree.
# Constraints:
#   The number of nodes in the tree is in the range [1, 1000].
from lib.TreeUtil import TreeNode, TreeNodeUtil
from typing import Optional


# Greedy: O(n)
# - if a node has children that are not covered by a camera, then we
#   must place a camera here.
# - if a node has no parent and it is not covered, then we must
#   place a camera here.
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], parent: Optional[TreeNode] = None) -> int:
            if not node:
                return 0
            camera = dfs(node.left, node) + dfs(node.right, node)
            if (node.left not in covered or node.right not in covered or
               (node not in covered and not parent)):
                covered.update({node.left, node.right, node, parent})  # type:ignore
                return camera + 1
            return camera

        covered = {None}
        return dfs(root)


if __name__ == '__main__':
    def unitTest(sol):
        root = TreeNodeUtil.fromBfsList([0, None, 0, None, 0, None, 0])
        r = sol.minCameraCover(root)
        print(r)
        assert r == 2

        root = TreeNodeUtil.fromBfsList([0, 0, None, 0, 0])
        r = sol.minCameraCover(root)
        print(r)
        assert r == 1

        root = TreeNodeUtil.fromBfsList([0, 0, None, 0, None, 0, None, None, 0])
        r = sol.minCameraCover(root)
        print(r)
        assert r == 2

    unitTest(Solution())
