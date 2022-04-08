# Given two nodes of a binary tree p and q, return their lowest common
# ancestor (LCA).
# Each node will have a reference to its parent node. The definition
# for Node is below:
# class Node {
#     public int val;
#     public Node left;
#     public Node right;
#     public Node parent;
# }
# According to the definition of LCA on Wikipedia: "The lowest common
# ancestor of two nodes p and q in a tree T is the lowest node that
# has both p and q as descendants (where we allow a node to be a
# descendant of itself)."
# Constraints:
#   The number of nodes in the tree is in the range [2, 10^5].
#   -10^9 <= Node.val <= 10^9
#   All Node.val are unique.
#   p != q
#   p and q exist in the tree.
#
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.parent = None
from typing import Optional
from lib.TreeUtil import TreeNode as Node, TreeNodeUtil


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def levelOfNode(node: Optional[Node]) -> int:
            level = 0
            while node:
                node = node.parent
                level += 1
            return level

        level1, level2 = levelOfNode(p), levelOfNode(q)
        while level1 != level2:
            if level1 > level2:
                level1 -= 1
                p = p.parent    # type: ignore
            else:
                level2 -= 1
                q = q.parent    # type: ignore

        while p and q and p.val != q.val:
            p, q = p.parent, q.parent     # type: ignore

        return p


if __name__ == '__main__':
    def unitTest(sol):
        root = TreeNodeUtil.fromBfsList([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        node1 = TreeNodeUtil.dfsFind(root, 5)
        node2 = TreeNodeUtil.dfsFind(root, 1)
        r = sol.lowestCommonAncestor(node1, node2)
        print(r.val)
        assert r.val == 3

        root = TreeNodeUtil.fromBfsList([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        node1 = TreeNodeUtil.dfsFind(root, 5)
        node2 = TreeNodeUtil.dfsFind(root, 4)
        r = sol.lowestCommonAncestor(node1, node2)
        print(r.val)
        assert r.val == 5

        root = TreeNodeUtil.fromBfsList([1, 2])
        node1 = TreeNodeUtil.dfsFind(root, 1)
        node2 = TreeNodeUtil.dfsFind(root, 2)
        r = sol.lowestCommonAncestor(node1, node2)
        print(r.val)
        assert r.val == 1

    unitTest(Solution())
