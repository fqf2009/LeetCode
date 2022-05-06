# You are given a nested list of integers nestedList. Each element is 
# either an integer or a list whose elements may also be integers or 
# other lists. Implement an iterator to flatten it.
# Implement the NestedIterator class:
#  - NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
#  - int next() Returns the next integer in the nested list.
#  - boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
# Your code will be tested with the following pseudocode:
#   initialize iterator with nestedList
#   res = []
#   while iterator.hasNext()
#       append iterator.next() to the end of res
#   return res
# If res matches the expected flattened list, then your code will be judged as correct.
# Constraints:
#   1 <= nestedList.length <= 500
#   The values of the integers in the nested list is in the range [-10^6, 10^6].
from typing import Generator


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger:
    def __init__(self, arg) -> None:
        if type(arg) ==  int:
            self.val = arg
        else:
            self.val = [NestedInteger(x) for x in arg]
        
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return type(self.val) ==  int

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return int(self.val)

    def getList(self) -> list['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return list(self.val)


# Generator
# T/S: O(1), O(D), where D is the depth of nested list
class NestedIterator:
    def __init__(self, nestedList: ['NestedInteger']):  # type: ignore
        self._generator = self._int_generator(nestedList)
        self._peek = None

    def _int_generator(self, nested_list: ['NestedInteger']) -> 'Generator[int]':  # type: ignore
        for ni in nested_list:
            if ni.isInteger():
                yield ni.getInteger()
            else:
                yield from self._int_generator(ni.getList())

    def next(self) -> int:
        if self.hasNext():
            res, self._peek = self._peek, None
            return res      # type: ignore
        else:
            raise StopIteration(self)

    def hasNext(self) -> bool:
        if self._peek is not None: return True
        try:
            self._peek = next(self._generator)
            return True
        except:
            return False


# Iterator using Stack
# T/S: O(1), O(D), where D is the depth of nested list
class NestedIterator1:
    def __init__(self, nestedList: ['NestedInteger']):  # type: ignore
        self.stack = []
        self.stack.append([nestedList, 0])
    
    def next(self) -> int:
        if self.hasNext():
            return self.stack.pop()[0]
        else:
            raise StopIteration(self)

    def _find_next(self) -> bool:
        if not self.stack: return False

        if isinstance(self.stack[-1][0], int):
            return True

        ni, i = self.stack.pop()
        if isinstance(ni, NestedInteger):
            if ni.isInteger():
                self.stack.append([ni.getInteger(), 0])
                return True
            else:
                self.stack.append([ni.getList(), 0])
                return self._find_next()
        else: # ni is list
            if i < len(ni) - 1:
                self.stack.append([ni, i + 1])

            if i < len(ni):
                if ni[i].isInteger():
                    self.stack.append([ni[i].getInteger(), 0])
                    return True
                else:
                    self.stack.append([ni[i].getList(), 0])

        return self._find_next()


    def hasNext(self) -> bool:
        return self._find_next()


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# Example 1:
# Input: nestedList = [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false, the
#              order of elements returned by next should be: [1,1,2,1,1].

# Example 2:
# Input: nestedList = [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false, the 
#              order of elements returned by next should be: [1,4,6].

if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('nestedIterator',), [(NestedIterator,), (NestedIterator1,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ([[1,1],2,[1,1]], [1,1,2,1,1]),
            ([1,[4,[6]]], [1,4,6]),
            ([[]], []),
            ([[[]]], []),
            ([[[], []]], []),
        ])
        def test_NestedIterator(self, lst, expected):
            nestedList = [NestedInteger(x) for x in lst]
            i, v = self.nestedIterator(nestedList), []      # type:ignore
            while i.hasNext(): v.append(i.next())
            self.assertEqual(v, expected)

    main()
