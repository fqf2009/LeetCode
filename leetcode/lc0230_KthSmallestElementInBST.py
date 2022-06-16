# Given the root of a binary search tree, and an integer k,
# return the kth smallest value (1-indexed) of all the
# values of the nodes in the tree.
# Constraints:
#   The number of nodes in the tree is n.
#   1 <= k <= n <= 10^4
#   0 <= Node.val <= 10^4
# Follow up: If the BST is modified often (i.e., we can do insert
#            and delete operations) and you need to find the kth
#            smallest frequently, how would you optimize?
from lib.TreeUtil import TreeNode, TreeNodeUtil
from typing import Optional


# inorder traverse (recursive) - T/S: O(n), O(n)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        return inorder(root)[k - 1]


# inorder traverse (iterative) - T/S: O(h+k), O(h), where h = tree_height
class Solution1:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)  # if visit node here: pre-order
                node = node.left

            node = stack.pop()      # if visit node here: in-order
            k -= 1
            if k == 0:
                return node.val
            node = node.right

        return -1


if __name__ == "__main__":

    def unitTest(sol):
        root = TreeNodeUtil.fromBfsList([3, 1, 4, None, 2])
        r = sol.kthSmallest(root, 1)
        print(r)
        assert r == 1

        root = TreeNodeUtil.fromBfsList([5, 3, 6, 2, 4, None, None, 1])
        r = sol.kthSmallest(root, 3)
        print(r)
        assert r == 3

    unitTest(Solution())
    unitTest(Solution1())
