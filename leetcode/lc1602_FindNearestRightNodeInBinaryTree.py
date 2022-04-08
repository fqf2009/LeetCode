# Given the root of a binary tree and a node u in the tree,
# return the nearest node on the same level that is to the
# right of u, or return null if u is the rightmost node in
# its level.

# Constraints:
#   The number of nodes in the tree is in the range [1, 10^5].
#   1 <= Node.val <= 10^5
#   All values in the tree are distinct.
#   u is a node in the binary tree rooted at root.
from collections import deque
from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


# BFS + Queue: O(n)
# - Check when poping up node from queue
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        que = deque([(root, 1)])
        while len(que) > 0:
            node, level = que.popleft()
            if node is u:
                return que[0][0] if len(que) > 0 and que[0][1] == level else None
            if node.left:
                que.append((node.left, level+1))    #type:ignore
            if node.right:
                que.append((node.right, level+1))   #type:ignore

        return None


# BFS + Queue: O(n)
# - Check before pushing node into queue
class Solution1:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        if root is u:
            return None
        que = deque([(root, 1)])
        found = False
        uLevel = -1
        while len(que) > 0:
            node, level = que.popleft()
            if found and level != uLevel - 1: return None
            for node1 in (node.left, node.right):
                if not node1: continue
                if found:
                    return node1 if level == uLevel - 1 else None
                if node1 is u:
                    found = True
                    uLevel = level + 1
                que.append((node1, level+1))    #type:ignore
        
        return None


if __name__ == '__main__':
    def unit_test(sol):
        root = TreeNodeUtil.fromBfsList([1, 2, 3, None, 4, 5, 6])
        node = TreeNodeUtil.dfsFind(root, 4)
        right = TreeNodeUtil.dfsFind(root, 5)
        r = sol.findNearestRightNode(root, node)
        print(r.val)
        assert r is right

        root = TreeNodeUtil.fromBfsList([3, None, 4, 2])
        node = TreeNodeUtil.dfsFind(root, 2)
        r = sol.findNearestRightNode(root, node)
        print(r)
        assert r is None

        root = TreeNodeUtil.fromBfsList([3])
        node = TreeNodeUtil.dfsFind(root, 3)
        r = sol.findNearestRightNode(root, node)
        print(r)
        assert r is None

    unit_test(Solution())
    unit_test(Solution1())
