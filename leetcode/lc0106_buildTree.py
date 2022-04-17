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
        def build(in_start: int, post_start: int, post_end: int) -> Optional[TreeNode]:
            if post_start > post_end: return None
            if post_start == post_end: return TreeNode(postorder[post_start])

            root = TreeNode(postorder[post_end])
            in_root_pos = in_pos[root.val]
            left_cnt = in_root_pos - in_start   # left tree size, use this to split postorder tree
            root.left = build(in_start, post_start, post_start + left_cnt - 1)
            root.right = build(in_root_pos + 1, post_start + left_cnt, post_end - 1)
            return root

        in_pos = {v:i for i, v in enumerate(inorder)}   # map node value to pos in inorder list
        return build(0, 0, len(postorder) - 1)


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
