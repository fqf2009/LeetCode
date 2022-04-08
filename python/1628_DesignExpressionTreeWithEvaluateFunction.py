# Given the postfix tokens of an arithmetic expression, build and return the binary
# expression tree that represents this expression.
# - Postfix notation is a notation for writing arithmetic expressions in which the
#   operands (numbers) appear before their operators. For example, the postfix tokens
#   of the expression 4*(5-(7+2)) are represented in the array
#   postfix = ["4","5","7","2","+","-","*"].
# The class Node is an interface you should use to implement the binary expression
# tree. The returned tree will be tested using the evaluate function, which is
# supposed to evaluate the tree's value. You should not remove the Node class;
# however, you can modify it as you wish, and you can define other classes to
# implement it if needed.
# - A binary expression tree is a kind of binary tree used to represent arithmetic
#   expressions. Each node of a binary expression tree has either zero or two
#   children. Leaf nodes (nodes with 0 children) correspond to operands (numbers),
#   and internal nodes (nodes with two children) correspond to the operators '+'
#   (addition), '-' (subtraction), '*' (multiplication), and '/' (division).
# It's guaranteed that no subtree will yield a value that exceeds 109 in absolute
# value, and all the operations are valid (i.e., no division by zero).
#
# Follow up: Could you design the expression tree such that it is more modular?
# For example, is your design able to support additional operators without making
# changes to your existing evaluate implementation?
#
# Constraints:
#   1 <= s.length < 100
#   s.length is odd.
#   s consists of numbers and the characters '+', '-', '*', and '/'.
#   If s[i] is a number, its integer representation is no more than 10^5.
#   It is guaranteed that s is a valid expression.
#   The absolute value of the result and intermediate values will not exceed 10^9.
#   It is guaranteed that no expression will include division by zero.
from abc import ABC, abstractmethod
from typing import List


class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass


class ValueNode(ABC):
    def __init__(self, value) -> None:
        super().__init__()
        self._value = value

    def evaluate(self) -> int:
        return self._value


class OperNode(Node):
    def __init__(self, left: Node, right: Node) -> None:
        super().__init__()
        self._left = left
        self._right = right

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node


class PlusNode(OperNode):
    def __init__(self, left: Node, right: Node) -> None:
        super().__init__(left, right)

    def evaluate(self) -> int:
        return self.left.evaluate() + self.right.evaluate()


class MinusNode(OperNode):
    def __init__(self, left: Node, right: Node) -> None:
        super().__init__(left, right)

    def evaluate(self) -> int:
        return self.left.evaluate() - self.right.evaluate()


class MultiplyNode(OperNode):
    def __init__(self, left: Node, right: Node) -> None:
        super().__init__(left, right)

    def evaluate(self) -> int:
        return self.left.evaluate() * self.right.evaluate()


class DivideNode(OperNode):
    def __init__(self, left: Node, right: Node) -> None:
        super().__init__(left, right)

    def evaluate(self) -> int:
        return self.left.evaluate() // self.right.evaluate()


# Stack
class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stk = []
        for s in postfix:
            if '0' <= s[-1] <= '9':
                stk.append(ValueNode(int(s)))
            else:
                right = stk.pop()
                left = stk.pop()
                if s[-1] == '+':
                    node = PlusNode(left, right)
                elif s[-1] == '-':
                    node = MinusNode(left, right)
                elif s[-1] == '*':
                    node = MultiplyNode(left, right)
                else:   # '/'
                    node = DivideNode(left, right)
                stk.append(node)

        return stk.pop()


if __name__ == '__main__':
    def unitTest(sol):
        obj = sol()
        expTree = obj.buildTree(["3", "4", "+", "2", "*", "7", "/"])
        r = expTree.evaluate()
        print(r)
        assert r == 2

        expTree = obj.buildTree(["4", "5", "2", "7", "+", "-", "*"])
        r = expTree.evaluate()
        print(r)
        assert r == -16

    unitTest(TreeBuilder)
