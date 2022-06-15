# Given a binary search tree (BST), find the lowest common ancestor (LCA) of 
# two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor 
# is defined between two nodes p and q as the lowest node in T that has both p 
# and q as descendants (where we allow a node to be a descendant of itself).”
# Constraints:
#   The number of nodes in the tree is in the range [2, 10^5].
#   -10^9 <= Node.val <= 10^9
#   All Node.val are unique.
#   p != q
#   p and q will exist in the BST.
from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


# Binary Search Tree
# T/S: O(n), O(n) in worst case
#      O(log(n)), O(log(n)) in a balanced BST
class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        def dfsLCA(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
            if root is None:
                return None
            if p.val <= root.val <= q.val:
                return root
            elif p.val > root.val:      # to avoid unnecessary traversal
                return dfsLCA(root.right, p, q)
            else:   # q.val < root.val
                return dfsLCA(root.left, p, q)

        if p.val > q.val:
            p, q = q, p

        return dfsLCA(root, p, q)   # type: ignore


# Iterative
class Solution1:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        if p.val > q.val:
            p, q = q, p

        while root:
            if p.val <= root.val <= q.val:
                break
            root = root.right if p.val > root.val else root.left    # type: ignore

        return root


class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root.val == p.val or root.val == q.val or 
           p.val < root.val < q.val or q.val < root.val < p.val):
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)   # type: ignore
        return self.lowestCommonAncestor(root.right, p, q)      # type: ignore


if __name__ == "__main__":

    def unitTest(sol):
        root = TreeNodeUtil.fromBfsList([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        node1 = TreeNodeUtil.dfsFind(root, 3)
        node2 = TreeNodeUtil.dfsFind(root, 5)
        r = sol.lowestCommonAncestor(root, node1, node2)
        print(r.val)
        assert r.val == 4

        root = TreeNodeUtil.fromBfsList([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        node1 = TreeNodeUtil.dfsFind(root, 2)
        node2 = TreeNodeUtil.dfsFind(root, 8)
        r = sol.lowestCommonAncestor(root, node1, node2)
        print(r.val)
        assert r.val == 6

        root = TreeNodeUtil.fromBfsList([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        node1 = TreeNodeUtil.dfsFind(root, 2)
        node2 = TreeNodeUtil.dfsFind(root, 4)
        r = sol.lowestCommonAncestor(root, node1, node2)
        print(r.val)
        assert r.val == 2

        root = TreeNodeUtil.fromBfsList([2, 1])
        node1 = TreeNodeUtil.dfsFind(root, 2)
        node2 = TreeNodeUtil.dfsFind(root, 1)
        r = sol.lowestCommonAncestor(root, node1, node2)
        print(r.val)
        assert r.val == 2

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
