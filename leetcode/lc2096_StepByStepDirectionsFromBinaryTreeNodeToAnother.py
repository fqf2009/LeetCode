# You are given the root of a binary tree with n nodes. Each node is uniquely
# assigned a value from 1 to n. You are also given an integer startValue
# representing the value of the start node s, and a different integer
# destValue representing the value of the destination node t.
# Find the shortest path starting from node s and ending at node t. Generate
# step-by-step directions of such path as a string consisting of only the
# uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:
#   'L' means to go from a node to its left child node.
#   'R' means to go from a node to its right child node.
#   'U' means to go from a node to its parent node.
# Return the step-by-step directions of the shortest path from node s to node t.
# Constraints:
#   The number of nodes in the tree is n.
#   2 <= n <= 10^5
#   1 <= Node.val <= n
#   All the values in the tree are unique.
#   1 <= startValue, destValue <= n
#   startValue != destValue
from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


# Binary Tree + DFS - T/S: O(n), O(n)
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfsPath(root: Optional[TreeNode], target: int, path: list[str]) -> bool:
            if not root:
                return False

            if root.val == target:
                return True

            if root.left:
                path.append("L")
                if dfsPath(root.left, target, path):
                    return True
                path.pop()

            if root.right:
                path.append("R")
                if dfsPath(root.right, target, path):
                    return True
                path.pop()

            return False

        path1, path2 = [], []
        dfsPath(root, startValue, path1)
        dfsPath(root, destValue, path2)
        sameDirection = 0
        for move1, move2 in zip(path1, path2):
            if move1 != move2:
                break
            sameDirection += 1

        res = ["U"] * (len(path1) - sameDirection)
        res.extend(path2[sameDirection:])
        return "".join(res)


if __name__ == "__main__":

    def unitTest(sol):
        root = TreeNodeUtil.fromBfsList([5, 1, 2, 3, None, 6, 4])
        r = sol.getDirections(root, 3, 6)
        print(r)
        assert r == "UURL"

        root = TreeNodeUtil.fromBfsList([5, 1, 2, 3, None, 6, 4])
        r = sol.getDirections(root, 6, 3)
        print(r)
        assert r == "UULL"

        root = TreeNodeUtil.fromBfsList([2, 1])
        r = sol.getDirections(root, 2, 1)
        print(r)
        assert r == "L"

        root = TreeNodeUtil.fromBfsList([2, 1])
        r = sol.getDirections(root, 1, 2)
        print(r)
        assert r == "U"

        root = TreeNodeUtil.fromBfsList([1, 2])
        r = sol.getDirections(root, 2, 2)   # works if start and dest are the same
        print(r)
        assert r == ""

    unitTest(Solution())
