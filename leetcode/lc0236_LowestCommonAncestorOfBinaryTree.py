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
#   p and q will exist in the tree.   <-- important!!!
from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


# Binary Tree + DFS - T/S: O(n), O(n)
# *** Solution from: 1676_LowestCommonAncestorOfBinaryTreeIV
# Note this approach is only useful when all nodes are in the tree!
# Analysis:
# - if current_node in nodes, current_node could be LCA
# - if current_node is not in nodes, but left and right subtree have node in nodes,
#   then current_node could be LCA
# - if only left or right subtree has node in nodes, then only that left or right
#   subtree could be LCA
# - short-circuit for better performance, i.e., once encounter a node in nodes,
#   no need to further investigate its subtrees.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        target = set((p, q))
        def dfs_lca(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if not root or root in target:
                return root

            left_lca = dfs_lca(root.left)
            right_lca = dfs_lca(root.right)

            if left_lca and right_lca:
                return root
            if left_lca:
                return left_lca
            if right_lca:
                return right_lca

            return None

        return dfs_lca(root)     # type: ignore


# sub-function is not necessary
class Solution0:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if not root or root in (p, q): return root
            left_lca = self.lowestCommonAncestor(root.left, p, q)   # type: ignore
            right_lca = self.lowestCommonAncestor(root.right, p, q) # type: ignore

            if left_lca and right_lca:
                return root
            else:
                return left_lca if left_lca else right_lca


# Binary Tree + DFS - T/S: O(n), O(n)
class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path = []
        target = [p, q]
        lca_depth = 0   # lowest stack depth of path, between finding first and second node

        def dfsLCA(root: Optional[TreeNode]) -> bool:   # return True after finding both
            if root is None:
                return False

            nonlocal lca_depth
            path.append(root)
            if len(target) > 1:     # first stage (to find either node)
                if root.val == target[0].val:
                    del target[0]
                    lca_depth = len(path) - 1  # set initial LCA after finding one node
                elif root.val == target[1].val:
                    del target[1]
                    lca_depth = len(path) - 1
            else:                   # second stage (to find remaining node)
                if root.val == target[0].val:
                    return True

            if dfsLCA(root.left) or dfsLCA(root.right):
                return True
            
            path.pop()
            if len(target) == 1:
                lca_depth = min(lca_depth, len(path)-1)

            return False

        dfsLCA(root)
        return path[lca_depth]


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

        root = TreeNodeUtil.fromBfsList([1, 2])
        node1 = TreeNodeUtil.dfsFind(root, 1)
        node2 = TreeNodeUtil.dfsFind(root, 2)
        r = sol.lowestCommonAncestor(root, node1, node2)
        print(r.val)
        assert r.val == 1

    unitTest(Solution())
    unitTest(Solution0())
    unitTest(Solution1())
