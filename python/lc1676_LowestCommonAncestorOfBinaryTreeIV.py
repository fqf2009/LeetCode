# Given the root of a binary tree and an array of TreeNode objects nodes, 
# return the lowest common ancestor (LCA) of all the nodes in nodes. All the 
# nodes will exist in the tree, and all values of the tree's nodes are unique.
# Extending the definition of LCA on Wikipedia: "The lowest common ancestor 
# of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has 
# every pi as a descendant (where we allow a node to be a descendant of 
# itself) for every valid i". A descendant of a node x is a node y that is on 
# the path from node x to some leaf node.
# Constraints:
#   The number of nodes in the tree is in the range [1, 10^4].
#   -10^9 <= Node.val <= 10^9
#   All Node.val are unique.
#   All nodes[i] will exist in the tree.
#   All nodes[i] are distinct.
from typing import Optional, List
from lib.TreeUtil import TreeNode, TreeNodeUtil


# Binary Tree + DFS - T/S: O(n), O(n)
# The more nodes, the better performance!
# Note this approach is only useful when all nodes are in the tree!
# Analysis:
# - if current_node in nodes, current_node could be LCA
# - if current_node is not in nodes, but left and right subtree have node in nodes,
#   then current_node could be LCA
# - if only left or right subtree has node in nodes, then only that left or right
#   subtree could be LCA
# - short-circuit for better performance!!! i.e., once encounter a node in nodes,
#   no need to further investigate its subtrees.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        target = set(nodes)
        def dfsLCA(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if not root or root in target:
                return root

            leftLCA = dfsLCA(root.left)
            rightLCA = dfsLCA(root.right)
            if leftLCA and rightLCA:
                return root
            if leftLCA:
                return leftLCA
            if rightLCA:
                return rightLCA

            return None

        return dfsLCA(root)     # type: ignore


# Binary Tree + DFS - T/S: O(n), O(n)
# - Bad performance due to visiting and collecting all the required nodes
class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        target = set(x.val for x in nodes)
        res = []            # [LCS]
        def dfsGather(root: TreeNode) -> set: # return values of nodes in this subtree
            subTreeVals = set()

            if root.left:
                leftVals = dfsGather(root.left)
                if len(res) > 0:
                    return leftVals
                subTreeVals = leftVals

            if root.right:
                rightVals = dfsGather(root.right)
                if len(res) > 0:
                    return rightVals
                subTreeVals = subTreeVals.union(rightVals)

            if root.val in target:
                subTreeVals.add(root.val)

            if len(subTreeVals) == len(target):
                res.append(root)

            return subTreeVals

        dfsGather(root)
        return res[0]


if __name__ == '__main__':
    def unitTest(sol):
        root = TreeNodeUtil.fromBfsList([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        node1 = TreeNodeUtil.dfsFind(root, 4)
        node2 = TreeNodeUtil.dfsFind(root, 7)
        r = sol.lowestCommonAncestor(root, [node1, node2])
        print(r.val)
        assert r.val == 2

        root = TreeNodeUtil.fromBfsList([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        node1 = TreeNodeUtil.dfsFind(root, 1)
        r = sol.lowestCommonAncestor(root, [node1])
        print(r.val)
        assert r.val == 1

        root = TreeNodeUtil.fromBfsList([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        node1 = TreeNodeUtil.dfsFind(root, 7)
        node2 = TreeNodeUtil.dfsFind(root, 6)
        node3 = TreeNodeUtil.dfsFind(root, 2)
        node4 = TreeNodeUtil.dfsFind(root, 4)
        r = sol.lowestCommonAncestor(root, [node1, node2, node3, node4])
        print(r.val)
        assert r.val == 5


    unitTest(Solution())
    unitTest(Solution1())
