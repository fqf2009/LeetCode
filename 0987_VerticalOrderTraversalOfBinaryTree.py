# Given the root of a binary tree, calculate the vertical order
# traversal of the binary tree.
#
# For each node at position (row, col), its left and right
# children will be at positions (row + 1, col - 1) and
# (row + 1, col + 1) respectively. The root of the tree is at (0, 0).
#
# The vertical order traversal of a binary tree is a list of
# top-to-bottom orderings for each column index starting from the
# leftmost column and ending on the rightmost column. There may be
# multiple nodes in the same row and same column. In such a case,
# sort these nodes by their values.
#
# Return the vertical order traversal of the binary tree.
# Constraints:
#   The number of nodes in the tree is in the range [1, 1000].
#   0 <= Node.val <= 1000
from ast import List
from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


# DFS
# - Time complexity: O(n*log(k)*log(n/k)), where k = number of columns in the tree
#   - DFS: O(n)
#   - Sort columns: k*(log(k))
#   - Sort rows:    (n/k)*log(n/k)
#   - Sort nodes:   if the tree is huge, this needs to be considered,
#                   however, k will be much smaller than n. 
# - Space complexity: O(n)
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]): # -> List[List[int]]:
        col_map = {}
        def dfsTraversal(root: Optional[TreeNode], row: int, col: int):
            if not root: return
            col_map.setdefault(col, dict()).setdefault(row, list()).append(root.val)
            dfsTraversal(root.left, row+1, col-1)
            dfsTraversal(root.right, row+1, col+1)

        dfsTraversal(root, 0, 0)

        res = []
        for _, row_map in sorted(col_map.items()):
            row_list = []
            for _, node_list in sorted(row_map.items()):
                row_list.extend(sorted(node_list))
            res.append(row_list)

        return res


if __name__ == "__main__":

    def unit_test(sol):
        root = TreeNodeUtil.fromBfsList([3, 9, 20, None, None, 15, 7])
        r = sol.verticalTraversal(root)
        print(r)
        assert r == [[9], [3, 15], [20], [7]]

        root = TreeNodeUtil.fromBfsList([1, 2, 3, 4, 5, 6, 7])
        r = sol.verticalTraversal(root)
        print(r)
        assert r == [[4], [2], [1, 5, 6], [3], [7]]

        root = TreeNodeUtil.fromBfsList([1, 2, 3, 4, 6, 5, 7])
        r = sol.verticalTraversal(root)
        print(r)
        assert r == [[4], [2], [1, 5, 6], [3], [7]]

    unit_test(Solution())
