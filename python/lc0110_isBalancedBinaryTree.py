from lib.TreeUtil import TreeNode, TreeNodeUtil
from typing import Optional

# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ 
# in height by no more than 1.

# Recursion
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def heightAndBalance(root: Optional[TreeNode]) -> tuple:
            if root == None:
                return (0, True)
            h1, b1 = heightAndBalance(root.left)
            if not b1:
                return (h1 + 1, b1)
            h2, b2 = heightAndBalance(root.right)
            return (max(h1, h2) + 1, abs(h1 - h2) <= 1 and b2)

        return heightAndBalance(root)[1]


# test case
if __name__ == "__main__":
    root = TreeNodeUtil.fromBfsList([3, 9, 20, None, None, 15, 7])
    r = Solution().isBalanced(root)
    print(r)
    assert(r == True)

    root = TreeNodeUtil.fromBfsList([1, 2, 2, 3, 3, None, None, 4, 4])
    r = Solution().isBalanced(root)
    print(r)
    assert(r == False)

    root = TreeNodeUtil.fromBfsList([])
    r = Solution().isBalanced(root)
    print(r)
    assert(r == True)
