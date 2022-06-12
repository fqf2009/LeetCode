# Given a node in a binary search tree, return the in-order successor
# of that node in the BST. If that node has no in-order successor,
# return null.
# The successor of a node is the node with the smallest key greater
# than node.val.
# You will have direct access to the node but not to the root of
# the tree. Each node will have a reference to its parent node.
# Below is the definition for Node:
#   class Node {
#       public int val;
#       public Node left;
#       public Node right;
#       public Node parent;
#   }
# Constraints:
#   The number of nodes in the tree is in the range [1, 10^4].
#   -10^5 <= Node.val <= 10^5
#   All Nodes will have unique values.
from typing import Optional
from lib.TreeUtil import TreeNode as Node, TreeNodeUtil

# Definition for a Node.
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.parent = None


# Iteration
# - If node has right child, go right once, and go left (multiple times)
#   until a most left leaf.
# - If node has no right child, go to parent (multiple times), until
#   a bigger parent (ancestor), i.e. current path is at the left side
#   of that parent.
#   e.g.:
#           5
#          / \
#         3   6
#        / \
#       2   4
#      /
#     1
class Solution:
    def inorderSuccessor(self, node: "Node") -> "Optional[Node]":
        if node.right:
            res = node.right
            while res.left:
                res = res.left
        else:
            res = node.parent
            while res and res.val < node.val:
                res = res.parent

        return res


if __name__ == "__main__":

    def unit_test(sol):
        root = TreeNodeUtil.fromBfsList([2, 1, 3])
        node = TreeNodeUtil.dfsFind(root, 1)
        r = sol.inorderSuccessor(node)
        print(r.val)
        assert r and r.val == 2

        root = TreeNodeUtil.fromBfsList([5, 3, 6, 2, 4, None, None, 1])
        node = TreeNodeUtil.dfsFind(root, 4)
        r = sol.inorderSuccessor(node)
        print(r.val)
        assert r and r.val == 5

        root = TreeNodeUtil.fromBfsList([5, 3, 6, 2, 4, None, None, 1])
        node = TreeNodeUtil.dfsFind(root, 6)
        r = sol.inorderSuccessor(node)
        print(r)
        assert not r

    unit_test(Solution())
