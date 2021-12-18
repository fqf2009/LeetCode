# Definition for a binary tree node.
from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil

# Given two integer arrays inorder and postorder where inorder is the inorder 
# traversal of a binary tree and postorder is the postorder traversal of the 
# same tree, construct and return the binary tree.
# Note: inorder and postorder consist of unique values.

# Recursion
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        def buildTreeHelper(inStart: int, postStart: int, postEnd: int) -> Optional[TreeNode]:
            if postStart > postEnd:
                return None
            elif postStart == postEnd:
                return TreeNode(postorder[postStart])
            else:
                res = TreeNode(postorder[postEnd])
                inMid = inPos[res.val]
                leftLen = inMid - inStart # left tree size, use this to split postorder tree
                res.left = buildTreeHelper(inStart, postStart, postStart + leftLen - 1)
                res.right = buildTreeHelper(inMid + 1, postStart + leftLen, postEnd - 1)
                return res

        # map each node's value to its position in inorder list
        inPos = {}
        for i in range(len(inorder)):
            inPos[inorder[i]] = i
        
        return buildTreeHelper(0, 0, len(postorder) - 1)


if __name__ == "__main__":
    obj = Solution()

    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    expected = [3, 9, 20, None, None, 15, 7]
    node = obj.buildTree(inorder, postorder)
    output = TreeNodeUtil.toBfsList(node)
    print(output)
    assert output == expected

    inorder = [-1]
    postorder = [-1]
    expected = [-1]
    node = obj.buildTree(inorder, postorder)
    output = TreeNodeUtil.toBfsList(node)
    print(output)
    assert output == expected
