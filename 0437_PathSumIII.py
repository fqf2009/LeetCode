from lib.TreeUtil import TreeNode, TreeNodeUtil
from typing import Optional
from collections import Counter

# Given the root of a binary tree and an integer targetSum, return the number
# of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must
# go downwards (i.e., traveling only from parent nodes to child nodes).
# Constraints:
#   The number of nodes in the tree is in the range [0, 1000].
#   -109 <= Node.val <= 109
#   -1000 <= targetSum <= 1000


# DFS + Recursion + Memorization
# Time complexity:  O(M*N), where N is number of tree nodes, M is tree depth
# Space complexity: O(M)
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfsPathSum(root: Optional[TreeNode]) -> int:
            nPaths = 0
            if root != None:
                for i in range(len(pathCSum)):
                    pathCSum[i] += root.val
                pathCSum.append(root.val)
                counter = Counter(pathCSum)
                nPaths += counter[targetSum]
                nPaths += dfsPathSum(root.left)
                nPaths += dfsPathSum(root.right)
                pathCSum.pop()
                for i in range(len(pathCSum)):
                    pathCSum[i] -= root.val
            return nPaths

        # Cumulative sum of node.val in path, from each ancestor node to current node
        pathCSum = []
        return dfsPathSum(root)


if __name__ == '__main__':
    sol = Solution()

    root = TreeNodeUtil.fromBfsList([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    r = sol.pathSum(root, 8)
    print(r)
    assert(r == 3)

    root = TreeNodeUtil.fromBfsList([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    r = sol.pathSum(root, 22)
    print(r)
    assert(r == 3)
