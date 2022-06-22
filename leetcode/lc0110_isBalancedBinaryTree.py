from lib.TreeUtil import TreeNode, TreeNodeUtil
from typing import Optional

# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ 
# in height by no more than 1.

# Recursion
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(root: Optional[TreeNode]) -> tuple:
            if root == None: return (True, 0)   # balanced and height

            b1, h1 = balanced(root.left)
            if not b1: return (b1, -1)

            b2, h2 = balanced(root.right)
            if not b2: return (b2, -1)

            return (abs(h1 - h2) <= 1, max(h1, h2) + 1)

        return balanced(root)[0]


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
