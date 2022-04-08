# You are given the root of a binary tree where each node has a value
# 0 or 1. Each root-to-leaf path represents a binary number starting 
# with the most significant bit.
#  - For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could 
#    represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the 
# path from the root to that leaf. Return the sum of these numbers.
# The test cases are generated so that the answer fits in a 32-bits integer.

from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil

# DFS + Recursion: O(n)
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def sumTree(root: TreeNode, parentValue: int) -> int:
            nodeValue = parentValue*2 + root.val
            if not root.left and not root.right:
                return nodeValue
            leftSum = sumTree(root.left, nodeValue) if root.left else 0
            rightSum = sumTree(root.right, nodeValue) if root.right else 0
            return leftSum + rightSum

        if root is None:
            return -1
        return sumTree(root, 0)

if __name__ == '__main__':
    sol = Solution()

    root = TreeNodeUtil.fromBfsList([1,0,1,0,1,0,1])
    r = sol.sumRootToLeaf(root)
    print(r)
    assert(r == 22)

    root = TreeNodeUtil.fromBfsList([0])
    r = sol.sumRootToLeaf(root)
    print(r)
    assert(r == 0)
