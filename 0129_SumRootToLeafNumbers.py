from typing import List, Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil

# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated 
# so that the answer will fit in a 32-bit integer.
# A leaf node is a node with no children.

# Recursion, DFS
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfsSumNumbers(node: TreeNode, pathVal: int) ->int:
            pathVal = pathVal * 10 + node.val
            res1, res2 = 0, 0
            if node.left == None and node.right == None:
                return pathVal
            if node.left:
                res1 = dfsSumNumbers(node.left, pathVal)
            if node.right:
                res2 = dfsSumNumbers(node.right, pathVal)
            return res1 + res2

        if not root:
            return 0
        return dfsSumNumbers(root, 0)


if __name__ == '__main__':
    sol = Solution()

    r1 = TreeNodeUtil.fromBfsList([1,2,3])
    s = sol.sumNumbers(r1)
    print(s)
    assert(s == 25)

    r1 = TreeNodeUtil.fromBfsList([4,9,0,5,1])
    s = sol.sumNumbers(r1)
    print(s)
    assert(s == 1026)
