# Design a stack that supports push, pop, top, and retrieving the minimum 
# element in constant time.
# Implement the MinStack class:
#   MinStack() initializes the stack object.
#   void push(int val) pushes the element val onto the stack.
#   void pop() removes the element on the top of the stack.
#   int top() gets the top element of the stack.
#   int getMin() retrieves the minimum element in the stack.
# Constraints:
#   -2^31 <= val <= 2^31 - 1
#   Methods pop, top and getMin operations will always be called on non-empty stacks.
#   At most 3 * 104 calls will be made to push, pop, top, and getMin.


# Stack with (val, min) pairs
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.getMin())))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Two stacks
class MinStack1:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        elif val <= self.getMin():
            self.minstack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.getMin():
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


if __name__ == "__main__":
    def unit_test(minstack):
        stk = minstack()

        inputs = [["push","push","push","getMin","pop","top","getMin"],
                    [[-2],[0],[-3],[],[],[],[]]]
        expected = [None, None, None, -3, None, 0, -2]
        outputs = []
        for i in range(len(inputs[0])):
            outputs.append(getattr(stk, inputs[0][i])(*inputs[1][i]))
        print(outputs)
        assert outputs == expected

    unit_test(MinStack)
    unit_test(MinStack1)
