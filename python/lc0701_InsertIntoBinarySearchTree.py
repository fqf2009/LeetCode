# You are given the root node of a binary search tree (BST) and a value to
# insert into the tree. Return the root node of the BST after the insertion.
# It is guaranteed that the new value does not exist in the original BST.
# Notice that there may exist multiple valid ways for the insertion, as long
# as the tree remains a BST after insertion. You can return any of them.

from typing import List, Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


# DFS + Recursive
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            if root.left:
                self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)
        else:
            if root.right:
                self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)

        return root

if __name__ == '__main__':
    def unitTest(sol):
        root = TreeNodeUtil.fromBfsList([4, 2, 7, 1, 3])
        root1 = sol.insertIntoBST(root, 5)
        r = TreeNodeUtil.toBfsList(root1)
        print(r)
        assert(r == [4, 2, 7, 1, 3, 5])

        root = TreeNodeUtil.fromBfsList([40, 20, 60, 10, 30, 50, 70])
        root1 = sol.insertIntoBST(root, 25)
        r = TreeNodeUtil.toBfsList(root1)
        print(r)
        assert(r == [40, 20, 60, 10, 30, 50, 70, None, None, 25])

        root = TreeNodeUtil.fromBfsList([4, 2, 7, 1, 3, None, None, None, None, None, None])
        root1 = sol.insertIntoBST(root, 5)
        r = TreeNodeUtil.toBfsList(root1)
        print(r)
        assert(r == [4, 2, 7, 1, 3, 5])

    unitTest(Solution())
