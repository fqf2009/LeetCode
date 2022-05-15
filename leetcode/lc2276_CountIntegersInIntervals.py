# Given an empty set of intervals, implement a data structure that can:
#  - Add an interval to the set of intervals.
#  - Count the number of integers that are present in at least one interval.
# Implement the CountIntervals class:
#  - CountIntervals() Initializes the object with an empty set of intervals.
#  - void add(int left, int right) Adds the interval [left, right] to 
#    the set of intervals.
#  - int count() Returns the number of integers that are present in 
#    at least one interval.
# Note that an interval [left, right] denotes all the integers x where 
# left <= x <= right.
# Constraints:
#   1 <= left <= right <= 10^9
#   At most 10^5 calls in total will be made to add and count.
#   At least one call will be made to count.


from typing import Optional
from sortedcontainers import SortedList


# SortedList + Merge Interval: T/S: O(n*log(n)), O(n)
class CountIntervals1:
    def __init__(self):
        self.itvs = SortedList([[-1, -1]])
        self.cnt = 0

    def add(self, left: int, right: int) -> None:
        i = self.itvs.bisect_left([left, right])
        # previous item, i-1 < len(self.itvs)
        # also, only need check once, because no overlap
        if self.itvs[i - 1][1] >= left:
            left = self.itvs[i - 1][0]
            right = max(right, self.itvs[i - 1][1])
            self.cnt -= self.itvs[i - 1][1] - self.itvs[i - 1][0] + 1
            del self.itvs[i - 1]
            i -= 1  # previous item is gone, following items is moved forward

        while i < len(self.itvs):
            if self.itvs[i][0] <= right:  # following items
                right = max(right, self.itvs[i][1])
                self.cnt -= self.itvs[i][1] - self.itvs[i][0] + 1
                del self.itvs[i]
            else:
                break

        self.itvs.add([left, right])
        self.cnt += right - left + 1

    def count(self) -> int:
        return self.cnt


# Segment Tree? Time Limit Exceed!
# - This solution only expand segment or add segment, never combine segment
class Node:
    def __init__(self, low, high) -> None:
        self.low: int = low
        self.high: int = high
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class CountIntervals:
    def __init__(self):
        self.cnt = 0
        self.root = None

    def add(self, left: int, right: int) -> None:
        def add_to_node(node: Node, lo: int, hi: int):
            if lo < node.low:
                if node.left:
                    add_to_node(node.left, lo, min(hi, node.low - 1))
                elif hi < node.low:
                    node.left = Node(lo, hi)
                    self.cnt += hi - lo + 1
                else:
                    self.cnt += node.low - lo
                    node.low = lo

            if hi > node.high:
                if node.right:
                    add_to_node(node.right, max(lo, node.high + 1), hi)
                elif lo > node.high:
                    node.right = Node(lo, hi)
                    self.cnt += hi - lo + 1
                else:
                    self.cnt += hi - node.high
                    node.high = hi

        if self.root is None:
            self.root = Node(left, right)
            self.cnt += right - left + 1
        else:
            add_to_node(self.root, left, right)

    def count(self) -> int:
        return self.cnt


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
if __name__ == "__main__":

    def unit_test(sol):
        sol.add(2, 3)
        sol.add(7, 10)
        r = sol.count()
        print(r)
        assert r == 6

        sol.add(5, 8)
        r = sol.count()
        print(r)
        assert r == 8

    def unit_test2(sol):
        r = sol.count()
        print(r)
        assert r == 0

        sol.add(8, 43)
        sol.add(13, 16)
        sol.add(26, 33)
        sol.add(28, 36)
        sol.add(29, 37)
        r = sol.count()
        print(r)
        assert r == 36

        sol.add(34, 46)
        sol.add(10, 23)
        r = sol.count()
        print(r)
        assert r == 39

    unit_test(CountIntervals())
    unit_test(CountIntervals1())

    unit_test2(CountIntervals())
    unit_test2(CountIntervals1())

# ["CountIntervals","count","add","add","add","add","add","count","add","add"]
# [[],[],[8,43],[13,16],[26,33],[28,36],[29,37],[],[34,46],[10,23]]
