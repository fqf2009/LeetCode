# Given a binary search tree and a node p in it, find the in-order successor 
# of that node in BST. The successor of a node p is the node with the 
# smallest key greater than p.val.
# Note:
#   If the given node has no in-order successor in the tree, return None.
#   It's guaranteed that the values of the tree are unique.
# Constraints:
#   The number of nodes in the tree is in the range [1, 10^4].
#   -10^5 <= Node.val <= 10^5
#   All Nodes will have unique values.
from lib.TreeUtil import TreeNode, TreeNodeUtil
from typing import Optional, List


# DFS + Recursion
class Solution:
    def inorderSuccessor(self, root: Optional[TreeNode], p: TreeNode) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            node = self.inorderSuccessor(root.left, p)
            return node if node else root


if __name__ == '__main__':
    sol = Solution()

    root = TreeNodeUtil.fromBfsList([2, 1, 3])
    r = sol.inorderSuccessor(root, TreeNode(1))
    assert(r)
    print(r.val)
    assert(r.val == 2)

    root = TreeNodeUtil.fromBfsList([5, 3, 6, 2, 4, None, None, 1])
    r = sol.inorderSuccessor(root, TreeNode(6))
    assert(r == None)
    print(r)
