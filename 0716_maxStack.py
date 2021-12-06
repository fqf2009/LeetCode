# A stack to remember max value ever pushed into.
# Each time an item is saved, the max value by far is also saved together.
# space usage is doubled. time complexity is O(n) for popMax, and O(1) for others.
class MaxStack(list):
    def __init__(self):
        super().__init__()

    def assertNonEmptyStack(self) -> None:
        if len(self) == 0:
            raise Exception("Error: Empty MaxStack.")

    def push(self, x: int) -> None:
        if len(self) > 0:
            m = max(x, self[-1][1])
        else:
            m = x
        self.append((x, m))

    def pop(self) -> int:
        self.assertNonEmptyStack()
        return super().pop()[0]

    def top(self) -> int:
        self.assertNonEmptyStack()
        return self[-1][0]

    def peekMax(self) -> int:
        self.assertNonEmptyStack()
        return self[-1][1]

    def popMax(self) -> int:
        self.assertNonEmptyStack()
        m = self[-1][1]
        s = []
        while self[-1][0] != m:
            s.append(self.pop())
        list.pop(self)
        # map() is implemented lazily in python 3
        list(map(self.push, reversed(s)))
        return m


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()


if __name__ == "__main__":
    ### test case
    inputs = [
        [
            "MaxStack",
            "push",
            "push",
            "push",
            "top",
            "popMax",
            "top",
            "peekMax",
            "pop",
            "top",
        ],
        [[], [5], [1], [5], [], [], [], [], [], []],
    ]
    expected = [None, None, None, None, 5, 5, 1, 5, 1, 5]
    outputs = [None]
    obj = globals()[inputs[0][0]](*inputs[1][0])
    for i in range(1, len(inputs[0])):
        outputs.append(getattr(obj, inputs[0][i])(*inputs[1][i]))
    print(outputs)
    assert outputs == expected

    ### test case
    inputs = [["MaxStack", "push", "push", "popMax", "peekMax"], [[], [5], [1], [], []]]
    expected = [None, None, None, 5, 1]
    outputs = [None]

    obj = globals()[inputs[0][0]](*inputs[1][0])
    for i in range(1, len(inputs[0])):
        outputs.append(getattr(obj, inputs[0][i])(*inputs[1][i]))
    print(outputs)
    assert outputs == expected
