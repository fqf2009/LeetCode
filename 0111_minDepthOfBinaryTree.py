from lib.TreeUtil import TreeNode, TreeNodeUtil
from typing import Optional
from collections import deque

# Given a binary tree, find its minimum depth. The minimum depth is the 
# number of nodes along the shortest path  the root node down to the 
# nearest leaf node. Note: A leaf is a node with no children.

# BFS - return result once the first leaf is met
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que = deque()
        que.append((root, 1))
        while len(que) > 0:
            node, level = que.popleft()
            if not node.left and not node.right:
                return level
            if node.left:
                que.append((node.left, level + 1))
            if node.right:
                que.append((node.right, level + 1))


# Recursion (DFS)
class Solution1:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        if root.left == None and root.right == None:
            return 1

        if root.left == None:
            return self.minDepth(root.right) + 1
        elif root.right == None:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


# test case
if __name__ == "__main__":
    root = TreeNodeUtil.fromBfsList([3, 9, 20, None, None, 15, 7])
    r = Solution().minDepth(root)
    print(r)
    assert(r == 2)

    root = TreeNodeUtil.fromBfsList([2, None, 3, None, 4, None, 5, None, 6])
    r = Solution().minDepth(root)
    print(r)
    assert(r == 5)
