# In a binary tree, a lonely node is a node that is the only
# child of its parent node. The root of the tree is not lonely
# because it does not have a parent node.

# Given the root of a binary tree, return an array containing
# the values of all lonely nodes in the tree. Return the list
# in any order.
from lib.TreeUtil import TreeNode, TreeNodeUtil
from typing import Optional, List


# DFS: O(n)
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        def dfsCollect(node: TreeNode, siblings: int):
            if siblings == 1:
                lonelyNodes.append(node.val)
            if node.left and node.right:
                dfsCollect(node.left, 2)
                dfsCollect(node.right, 2)
            elif node.left:
                dfsCollect(node.left, 1)
            elif node.right:
                dfsCollect(node.right, 1)

        lonelyNodes = []
        if root:
            dfsCollect(root, 2)
        return lonelyNodes


if __name__ == '__main__':
    def unit_test(sol):
        root = TreeNodeUtil.fromBfsList([1, 2, 3, None, 4])
        r = sol.getLonelyNodes(root)
        print(r)
        assert r == [4]

        root = TreeNodeUtil.fromBfsList([7, 1, 4, 6, None, 5, 3, None, 
                                         None, None, None, None, 2])
        r = sol.getLonelyNodes(root)
        print(r)
        assert r == [6, 2]

        root = TreeNodeUtil.fromBfsList([11, 99, 88, 77, None, None, 66, 55, 
                                         None, None, 44, 33, None, None, 22])
        r = sol.getLonelyNodes(root)
        print(r)
        assert r == [77, 55, 33, 66, 44, 22]

    unit_test(Solution())
