# Given a binary tree, find the lowest common ancestor (LCA) of two given 
# nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common 
# ancestor is defined between two nodes p and q as the lowest node in 
# T that has both p and q as descendants (where we allow a node to be 
# a descendant of itself).”
# Constraints:
#   The number of nodes in the tree is in the range [2, 10^5].
#   -10^9 <= Node.val <= 10^9
#   All Node.val are unique.
#   p != q
#   p and q will exist in the tree.
from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


# Binary Tree + DFS - T/S: O(n), O(n)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path = []
        target = [p, q]
        res = [0]   # lowest stack depth of path, between finding first and second node
        def dfsLCA(root: Optional[TreeNode]) -> bool:   # return True after finding both
            if root is None:
                return False

            path.append(root)
            if len(target) > 1:     # first stage (to find either node)
                if root.val == target[0].val:
                    del target[0]
                    res[0] = len(path) - 1  # set initial LCA after finding one node
                elif root.val == target[1].val:
                    del target[1]
                    res[0] = len(path) - 1
            else:                   # second stage (to find remaining node)
                if root.val == target[0].val:
                    return True

            if dfsLCA(root.left) or dfsLCA(root.right):
                return True
            
            path.pop()
            if len(target) == 1:
                res[0] = min(res[0], len(path)-1)

            return False

        dfsLCA(root)
        return path[res[0]] if res[0] >= 0 else None


if __name__ == '__main__':
    def unitTest(sol):
        root = TreeNodeUtil.fromBfsList([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        node1 = TreeNodeUtil.dfsFind(root, 5)
        node2 = TreeNodeUtil.dfsFind(root, 1)
        r = sol.lowestCommonAncestor(root, node1, node2)
        print(r.val)
        assert r.val == 3

        root = TreeNodeUtil.fromBfsList([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        node1 = TreeNodeUtil.dfsFind(root, 5)
        node2 = TreeNodeUtil.dfsFind(root, 4)
        r = sol.lowestCommonAncestor(root, node1, node2)
        print(r.val)
        assert r.val == 5

        root = TreeNodeUtil.fromBfsList([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        node1 = TreeNodeUtil.dfsFind(root, 5)
        node2 = TreeNode(10)
        r = sol.lowestCommonAncestor(root, node1, node2)
        print(r)
        assert r is None

    unitTest(Solution())
