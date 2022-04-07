# You need to construct a binary tree from a string consisting of
# parenthesis and integers.
# The whole input represents a binary tree. It contains an integer
# followed by zero, one or two pairs of parenthesis. The integer
# represents the root's value and a pair of parenthesis contains a
# child binary tree with the same structure.
# You always start to construct the left child node of the parent
# first if it exists.
# Constraints:
#   0 <= s.length <= 3 * 10^4
#   s consists of digits, '(', ')', and '-' only.
from typing import Optional, Tuple
from lib.TreeUtil import TreeNode, TreeNodeUtil


# Recursion
# - T/S: O(n), O(H), H = height of tree
#   in worst case scenario, e.g. skewed tree, H = n
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        def build_tree(i: int) -> Tuple[int, Optional[TreeNode]]:
            j = i
            while j < len(s):
                if s[j] != '-' and not s[j].isdigit():
                    break
                j += 1
            val = int(s[i:j])
            i = j
            node = TreeNode(val)
            if i < len(s) and s[i] == "(":
                i, node.left = build_tree(i + 1)
                i += 1  # skip ')'
            if i < len(s) and s[i] == "(":
                i, node.right = build_tree(i + 1)
                i += 1  # skip ')'

            return (i, node)
        
        return None if s == "" else build_tree(0)[1]


if __name__ == "__main__":

    def unit_test(sol):
        root = sol.str2tree("4")
        r = TreeNodeUtil.toBfsList(root)
        print(r)
        assert r == [4]
        
        root = sol.str2tree("4(2(3)(1))(6(5))")
        r = TreeNodeUtil.toBfsList(root)
        print(r)
        assert r == [4, 2, 6, 3, 1, 5]

        root = sol.str2tree("4(2(3)(1))(6(5)(7))")
        r = TreeNodeUtil.toBfsList(root)
        print(r)
        assert r == [4, 2, 6, 3, 1, 5, 7]

        root = sol.str2tree("-4(2(3)(1))(6(5)(7))")
        r = TreeNodeUtil.toBfsList(root)
        print(r)
        assert r == [-4, 2, 6, 3, 1, 5, 7]

    unit_test(Solution())
