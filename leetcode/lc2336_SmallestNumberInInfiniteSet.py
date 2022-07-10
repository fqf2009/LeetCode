# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
# Implement the SmallestInfiniteSet class:
#  - SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain
#    all positive integers.
#  - int popSmallest() Removes and returns the smallest integer contained in
#    the infinite set.
#  - void addBack(int num) Adds a positive integer num back into the infinite
#    set, if it is not already in the infinite set.
# Constraints:
#   1 <= num <= 1000
#   At most 1000 calls will be made in total to popSmallest and addBack.
from sortedcontainers import SortedList, SortedSet

class SmallestInfiniteSet2:
    def __init__(self):
        self.ss = SortedSet()
        self.minValue = 1

    def popSmallest(self) -> int:
        if not self.ss:
            res = self.minValue
            self.minValue += 1
        else:
            res = self.ss.pop(0)
        return res

    def addBack(self, num: int) -> None:
        if num < self.minValue:
            self.ss.add(num)


class SmallestInfiniteSet1:
    def __init__(self):
        self.ss = SortedList()
        self.minValue = 1

    def popSmallest(self) -> int:
        if not self.ss:
            res = self.minValue
            self.minValue += 1
        else:
            res = self.ss.pop(0)
        return res

    def addBack(self, num: int) -> None:
        if num < self.minValue and not self.ss.__contains__(num):
            self.ss.add(num)


class SmallestInfiniteSet:
    def __init__(self):
        self.refilled = set()
        self.minValue = 1

    def popSmallest(self) -> int:
        if self.refilled:
            res = min(self.refilled)
            self.refilled.remove(res)
        else:
            res = self.minValue
            self.minValue += 1
        return res

    def addBack(self, num: int) -> None:
        if num < self.minValue:
            self.refilled.add(num)


if __name__ == "__main__":
    def unit_test1(solution):
        print(solution.__name__)
        sol = solution()
        inputs = [
            ["addBack", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
             "addBack", "addBack", "popSmallest", "popSmallest", "popSmallest"],
            [[2], [], [], [], [], [1], [1], [], [], []],
        ]
        expected = [None, 1, 2, 3, 4, None, None, 1, 5, 6]
        outputs = []
        for i in range(len(inputs[0])):
            r = getattr(sol, inputs[0][i])(*inputs[1][i])
            outputs.append(r)
        print(outputs)
        assert outputs == expected

    unit_test1(SmallestInfiniteSet)
    unit_test1(SmallestInfiniteSet1)
    unit_test1(SmallestInfiniteSet2)
