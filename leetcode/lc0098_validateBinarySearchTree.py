from typing import List, Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# - The left subtree of a node contains only nodes with keys less than the node's key.
# - The right subtree of a node contains only nodes with keys greater than the node's key.
# - Both the left and right subtrees must also be binary search trees.

# Constraints:
#   The number of nodes in the tree is in the range [1, 104].
#   -231 <= Node.val <= 231 - 1

# DFS, recursive
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfsValidBST(root: TreeNode):
            if root.left != None:
                leftMin, leftMax, valid = dfsValidBST(root.left)
                if not valid or leftMax >= root.val:
                    return (leftMin, leftMax, False)
            else:
                leftMin = root.val

            if root.right != None:
                rightMin, rightMax, valid = dfsValidBST(root.right)
                if not valid or rightMin <= root.val:
                    return (rightMin, rightMax, False)
            else:
                rightMax = root.val

            return (leftMin, rightMax, True)

        assert(root != None)
        return dfsValidBST(root)[2]


if __name__ == '__main__':
    sol = Solution()

    root = TreeNodeUtil.fromBfsList([2, 1, 3])
    r = sol.isValidBST(root)
    print(r)
    assert(r == True)

    root = TreeNodeUtil.fromBfsList([5, 1, 4, None, None, 3, 6])
    r = sol.isValidBST(root)
    print(r)
    assert(r == False)
