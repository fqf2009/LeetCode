# Given the root of a binary tree, imagine yourself standing on the right side
# of it, return the values of the nodes you can see ordered from top to bottom.
# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
from typing import List, Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


# DFS - O(n)
# - the problem description is not very accurate, it actually only
#   want the node last visited at each level (depth), not the node
#   with biggest column index at each level.
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfsTravel(root: Optional[TreeNode], row: int):
            if not root:
                return
            if row >= len(res):
                res.append(root.val)
            else:
                res[row] = root.val
            dfsTravel(root.left, row + 1)
            dfsTravel(root.right, row + 1)

        dfsTravel(root, 0)
        return res


# DFS - O(n)
# - this is to get the node with biggest column index at each level.
class Solution1:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfsTravel(root: Optional[TreeNode], row: int, col: int):
            if not root:
                return
            if row >= len(res):
                res.append((root.val, col))
            elif col >= res[row][1]:  # same row and column, later visit wins
                res[row] = (root.val, col)
            dfsTravel(root.left, row + 1, col - 1)
            dfsTravel(root.right, row + 1, col + 1)

        dfsTravel(root, 0, 0)
        return [x for x, _ in res]


if __name__ == "__main__":

    def unit_test(sol):
        root = TreeNodeUtil.fromBfsList([0, 1, 2, None, 3, 4, None, None, 
                                         5, 9, None, None, 6, 10, None])
        r = sol.rightSideView(root)
        print(r)
        assert r == [0, 2, 4, 9, 10]
        # assert r == [0, 2, 4, 5, 6]   # for solution1

        root = TreeNodeUtil.fromBfsList([1, 2, 3, None, 5, 6])
        r = sol.rightSideView(root)
        print(r)
        assert r == [1, 3, 6]

        root = TreeNodeUtil.fromBfsList([1, 2, 3, None, 5, None, 4])
        r = sol.rightSideView(root)
        print(r)
        assert r == [1, 3, 4]

        root = TreeNodeUtil.fromBfsList([1, None, 3])
        r = sol.rightSideView(root)
        print(r)
        assert r == [1, 3]

        root = TreeNodeUtil.fromBfsList([])
        r = sol.rightSideView(root)
        print(r)
        assert r == []

    unit_test(Solution())
