# A binary expression tree is a kind of binary tree used to represent arithmetic
# expressions. Each node of a binary expression tree has either zero or two
# children. Leaf nodes (nodes with 0 children) correspond to operands (numbers),
# and internal nodes (nodes with 2 children) correspond to the operators '+'
# (addition), '-' (subtraction), '*' (multiplication), and '/' (division).
# For each internal node with operator o, the infix expression that it represents
# is (A o B), where A is the expression the left subtree represents and B is the
# expression the right subtree represents.
# You are given a string s, an infix expression containing operands, the operators
# described above, and parentheses '(' and ')'.
#
# Return any valid binary expression tree, which its in-order traversal reproduces
# s after omitting the parenthesis from it (see examples below).
#
# Please note that order of operations applies in s. That is, expressions in
# parentheses are evaluated first, and multiplication and division happen before
# addition and subtraction.
#
# Operands must also appear in the same order in both s and the in-order traversal
# of the tree.
#
# Constraints:
#   1 <= s.length <= 1000
#   s consists of digits and the characters '+', '-', '*', and '/'.
#   Operands in s are exactly 1 digit.
#   It is guaranteed that s is a valid expression.
from lib.TreeUtil import TreeNode as Node, TreeNodeUtil


# Stack
class Solution:
    def expTree(self, s: str) -> 'Node':
        stk = []

        def compactStk():
            node2 = stk.pop()
            op = stk.pop()
            node1 = stk.pop()
            stk.append(Node(val=op, left=node1, right=node2))

        for ch in s:
            if '0' <= ch <= '9':
                stk.append(Node(val=ch))
            elif ch == '(':
                stk.append('(')
            elif ch == '*' or ch == '/':
                if len(stk) > 2 and stk[-2] in ('*', '/'):
                    compactStk()
                stk.append(ch)
            elif ch == '+' or ch == '-':
                while len(stk) > 2 and stk[-2] in ('+', '-', '*', '/'):
                    compactStk()
                stk.append(ch)
            else:  # ')'
                while len(stk) > 2 and stk[-2] != '(':
                    compactStk()
                node1 = stk.pop()
                stk.pop()
                stk.append(node1)

        while len(stk) > 1:
            compactStk()

        return stk[0]


if __name__ == '__main__':
    def unitTest(sol):
        root = sol.expTree("3*(9-6*5)")
        r = TreeNodeUtil.toBfsList(root)
        print(r)
        assert r == ['*', '3', '-', None, None, '9', '*', None, None, '6', '5']

        root = sol.expTree("3*4-2*5")
        r = TreeNodeUtil.toBfsList(root)
        print(r)
        assert r == ['-', '*', '*', '3', '4', '2', '5']

        root = sol.expTree("2-3/(5*2)+1")
        r = TreeNodeUtil.toBfsList(root)
        print(r)
        assert r == ['+', '-', '1', '2', '/', None, None, None, None, '3', '*', None, None, '5', '2']

        root = sol.expTree("1+2+3+4+5")
        r = TreeNodeUtil.toBfsList(root)
        print(r)
        # have many different answers
        assert r == ['+', '+', '5', '+', '4', None, None, '+', '3', None, None, '1', '2']

    unitTest(Solution())
