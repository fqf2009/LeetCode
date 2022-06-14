# Given two integer arrays preorder and inorder where preorder is the
# preorder traversal of a binary tree and inorder is the inorder
# traversal of the same tree, construct and return the binary tree.
# Constraints:
#   1 <= preorder.length <= 3000
#   inorder.length == preorder.length
#   -3000 <= preorder[i], inorder[i] <= 3000
#   preorder and inorder consist of unique values.
#   Each value of inorder also appears in preorder.
#   preorder is guaranteed to be the preorder traversal of the tree.
#   inorder is guaranteed to be the inorder traversal of the tree.
from typing import List, Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preStart, inStart, inEnd) -> Optional[TreeNode]:
            if inStart > inEnd:
                return None
            root = TreeNode(preorder[preStart])
            mid = inPos[root.val]
            root.left = build(preStart + 1, inStart, mid - 1)
            leftSize = mid - inStart
            root.right = build(preStart + 1 + leftSize, mid + 1, inEnd)
            return root

        inPos = {v: i for i, v in enumerate(inorder)}
        return build(0, 0, len(preorder) - 1)


if __name__ == "__main__":

    def unitTest(sol):
        preorder = [3, 9, 1, 2, 20, 15, 7]
        inorder = [1, 9, 2, 3, 15, 20, 7]
        expected = [3, 9, 20, 1, 2, 15, 7]
        node = sol.buildTree(preorder, inorder)
        output = TreeNodeUtil.toBfsList(node)
        print(output)
        assert output == expected

        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        expected = [3, 9, 20, None, None, 15, 7]
        node = sol.buildTree(preorder, inorder)
        output = TreeNodeUtil.toBfsList(node)
        print(output)
        assert output == expected

        preorder = [-1]
        inorder = [-1]
        expected = [-1]
        node = sol.buildTree(preorder, inorder)
        output = TreeNodeUtil.toBfsList(node)
        print(output)
        assert output == expected

        preorder = [1, 2]
        inorder = [2, 1]
        expected = [1, 2]
        node = sol.buildTree(preorder, inorder)
        output = TreeNodeUtil.toBfsList(node)
        print(output)
        assert output == expected

    unitTest(Solution())
