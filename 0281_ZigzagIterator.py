# Given two vectors of integers v1 and v2, implement an iterator 
# to return their elements alternately.
# Implement the ZigzagIterator class:
# ZigzagIterator(List<int> v1, List<int> v2) initializes the object
# with the two vectors v1 and v2.
# boolean hasNext() returns true if the iterator still has elements, 
# and false otherwise.
# int next() returns the current element of the iterator and moves 
# the iterator to the next element.

# Constraints:
#   0 <= v1.length, v2.length <= 1000
#   1 <= v1.length + v2.length <= 2000
#   -231 <= v1[i], v2[i] <= 231 - 1

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

from typing import List

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.p1 = 0
        self.p2 = 0

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration
        if self.p1 < len(self.v1) and (self.p1 <= self.p2 or self.p2 >= len(self.v2)):
            res = self.v1[self.p1]
            self.p1 += 1
        else:
            res = self.v2[self.p2]
            self.p2 += 1
        return res

    def hasNext(self) -> bool:
        return self.p1 + self.p2 < len(self.v1) + len(self.v2)

if __name__ == '__main__':
    def unit_test():
        v1 = [1,2]
        v2 = [3,4,5,6]
        i, v = ZigzagIterator(v1, v2), []
        while i.hasNext(): v.append(i.next())
        print (v)
        assert v == [1,3,2,4,5,6]

        v1 = [1]
        v2 = []
        i, v = ZigzagIterator(v1, v2), []
        while i.hasNext(): v.append(i.next())
        print (v)
        assert v == [1]

        v1 = []
        v2 = [1]
        i, v = ZigzagIterator(v1, v2), []
        while i.hasNext(): v.append(i.next())
        print (v)
        assert v == [1]

        v1 = []
        v2 = []
        i, v = ZigzagIterator(v1, v2), []
        while i.hasNext(): v.append(i.next())
        print (v)
        assert v == []

    unit_test()
