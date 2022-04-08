# Given the root of a binary search tree, return a balanced binary search tree
# with the same node values. If there is more than one answer, return any of them.
# A binary search tree is balanced if the depth of the two subtrees of every
# node never differs by more than 1.
# Constraints:
#   The number of nodes in the tree is in the range [1, 104].
#   1 <= Node.val <= 105
from lib.TreeUtil import TreeNode, TreeNodeUtil
from typing import Optional


# BST - T/S: O(n), O(n)
# - generate a sorted list via a in-order traversal
# - then create a new BST recursively
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        def dfs(root: Optional[TreeNode]):
            if not root: return
            dfs(root.left)
            nodes.append(root)
            dfs(root.right)

        def buildBST(nodes) -> Optional[TreeNode]:
            if len(nodes) == 0: return None
            n = len(nodes)
            k = n // 2
            nodes[k].left = buildBST(nodes[:k])
            nodes[k].right = buildBST(nodes[k+1:])
            return nodes[k]

        dfs(root)
        return buildBST(nodes)  #type:ignore


if __name__ == '__main__':
    def unitTest(sol):
        root = TreeNodeUtil.fromBfsList([1, None, 2, None, 3, None, 4, None, None])
        root2 = sol.balanceBST(root)
        r = TreeNodeUtil.toBfsList(root2)
        print(r)
        assert r == [2, 1, 3, None, None, None, 4] or r == [3, 2, 4, 1] or r == [3, 1, 4, None, 2]

        root = TreeNodeUtil.fromBfsList([2, 1, 3])
        root2 = sol.balanceBST(root)
        r = TreeNodeUtil.toBfsList(root2)
        print(r)
        assert r == [2, 1, 3]

    unitTest(Solution())
