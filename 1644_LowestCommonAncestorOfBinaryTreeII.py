# Given the root of a binary tree, return the lowest common ancestor (LCA)
# of two given nodes, p and q. If either node p or q does not exist in the 
# tree, return null. All values of the nodes in the tree are unique.
#
# According to the definition of LCA on Wikipedia: "The lowest common 
# ancestor of two nodes p and q in a binary tree T is the lowest node 
# that has both p and q as descendants (where we allow a node to be a 
# descendant of itself)". A descendant of a node x is a node y that is
# on the path from node x to some leaf node.
# Constraints:
#   The number of nodes in the tree is in the range [1, 10^4].
#   -10^9 <= Node.val <= 10^9
#   All Node.val are unique.
#   p != q
from typing import Optional
from lib.TreeUtil import TreeNode, TreeNodeUtil


# Binary Tree + DFS - T/S: O(n), O(n)
# - Alternative approach, refer to: 1676_LowestCommonAncestorOfBinaryTreeIV
#   not that good like 1678 one, because nodes might not be in tree.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', 
                             p: 'TreeNode', q: 'TreeNode') -> Optional['TreeNode']:
        target = set([p, q])
        found = []
        def dfsLCA(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if root:
                leftLCA = dfsLCA(root.left)
                if len(found) == 2:
                    return leftLCA      # to improve performance

                rightLCA = dfsLCA(root.right)
                if leftLCA and rightLCA:    # check this before the following one
                    return root

                # if len(found) == 2:         # no need, and must first check the above one
                #     return rightLCA

                if root in target:
                    found.append(root)
                    return root

                if leftLCA: return leftLCA

                if rightLCA: return rightLCA

            return None

        lca = dfsLCA(root)
        return lca if len(found) == 2 else None


# Binary Tree + DFS - T/S: O(n), O(n)
class Solution1:
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
    unitTest(Solution1())
