from lib.TreeUtil import TreeNode, TreeNodeUtil
from typing import Optional

# Given the root of a binary tree, return its maximum depth. A binary tree's 
# maximum depth is the number of nodes along the longest path from the root 
# node down to the farthest leaf node.

 # Recursion
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# test case
if __name__ == "__main__":
    root = TreeNodeUtil.fromBfsList([3, 9, 20, None, None, 15, 7])
    r = Solution().maxDepth(root)
    print(r)
    assert(r == 3)

    root = TreeNodeUtil.fromBfsList([1, None, 2])
    r = Solution().maxDepth(root)
    print(r)
    assert(r == 2)

    root = TreeNodeUtil.fromBfsList([])
    r = Solution().maxDepth(root)
    print(r)
    assert(r == 0)

    root = TreeNodeUtil.fromBfsList([0])
    r = Solution().maxDepth(root)
    print(r)
    assert(r == 1)
