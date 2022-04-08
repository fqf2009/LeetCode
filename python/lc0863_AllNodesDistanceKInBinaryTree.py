# Given the root of a binary tree, the value of a target node target, 
# and an integer k, return an array of the values of all nodes that 
# have a distance k from the target node.
# You can return the answer in any order.
# Constraints:
#   The number of nodes in the tree is in the range [1, 500].
#   0 <= Node.val <= 500
#   All the values Node.val are unique.
#   target is the value of one of the nodes in the tree.
#   0 <= k <= 1000
from collections import deque
from typing import List
from lib.TreeUtil import TreeNode, TreeNodeUtil


# DFS - T/S: O(n), O(n)
# - No need to visit the entire tee, may be better for big tree.
# Algorithm:
# - first DFS to find the target node;
# - from there collect nodes which are k depth beneath target node;
# - then return back one level up to its parent, and collect from
#   different branch for k-1 depths of nodes;
# - continue return back, up one level, do similar thing
# - seperate the finding and collecting tasks, to simplify the code.
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        def dfs_visit(root) -> int:     # after finding target, report the
            if root:                    # distance to target to ancestors
                if root == target:
                    dfs_collect(target, k)
                    return 1
                for node1, node2 in ((root.left, root.right), (root.right, root.left)):
                    distance = dfs_visit(node1)
                    if distance > 0:
                        if distance == k:
                            dfs_collect(root, 0)
                        elif distance < k:
                            dfs_collect(node2, k - distance - 1)
                        return distance + 1
            return 0

        def dfs_collect(root, depth):
            if root:
                if depth == 0:
                    res.append(root.val)
                else:
                    dfs_collect(root.left, depth - 1)
                    dfs_collect(root.right, depth - 1)

        dfs_visit(root)
        return res


# BFS - T/S: O(n), O(n)
# - add parent pointer to each node, so we can do BFS
class Solution1:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs_set_parent(root, parent = None):
            if root:
                root.parent = parent
                dfs_set_parent(root.left, root)
                dfs_set_parent(root.right, root)

        dfs_set_parent(root)
        dq = deque([(target, 0)])
        visited = set()
        res = []
        while dq:
            node, distance = dq.popleft()
            visited.add(node.val)
            if distance == k:
                res.append(node.val)
            else:
                for next in (node.left, node.right, node.parent):
                    if next and not next.val in visited:
                        dq.append((next, distance+1))  # type: ignore
        
        return res


if __name__ == '__main__':
    def unit_test(sol):
        root = TreeNodeUtil.fromBfsList([0,1,None,3,2])
        target = TreeNodeUtil.dfsFind(root, 2)
        r = sol.distanceK(root, target, k = 1)
        print(r)
        assert r == [1]

        root = TreeNodeUtil.fromBfsList([3,5,1,6,2,0,8,None,None,7,4])
        target = TreeNodeUtil.dfsFind(root, 5)
        r = sol.distanceK(root, target, k = 2)
        print(r)
        assert r == [7,4,1]

        root = TreeNodeUtil.fromBfsList([1])
        target = TreeNodeUtil.dfsFind(root, 1)
        r = sol.distanceK(root, target, k = 3)
        print(r)
        assert r == []

    unit_test(Solution())
    unit_test(Solution1())
