# You are given a nested list of integers nestedList. Each element is either
# an integer or a list whose elements may also be integers or other lists.
# The depth of an integer is the number of lists that it is inside of. For 
# example, the nested list [1,[2,2],[[3],2],1] has each integer's value set 
# to its depth.
# Return the sum of each integer in nestedList multiplied by its depth.
# Constraints:
#   1 <= nestedList.length <= 50
#   The values of the integers in the nested list is in the range [-100, 100].
#   The maximum depth of any integer is less than or equal to 50.
from typing import List, Optional


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        if value is None:
            self._lst = []
            self._val = None
        else:
            self._lst = None
            self._val = value

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return self._val is not None
 
    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        if self._lst is None:   # alternative implementation is to raise exception
            self._lst = []
            self._val = None
        self._lst.append(elem)
 
    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        if not self.isInteger:  # alternative implementation is to raise exception
            self._lst = None
        self._val = value
 
    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return self._val
 
    def getList(self) -> Optional[List['NestedInteger']]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return self._lst


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def depthSumNI(ni: NestedInteger, depth: int) -> int:
            if ni.isInteger():
                return ni.getInteger() * depth    # type: ignore
            else:
                return sum(depthSumNI(x, depth+1) for x in ni.getList())   # type: ignore

        return sum(depthSumNI(ni, 1) for ni in nestedList)


if __name__ == '__main__':
    def unitTest(sol):
        ni1 = NestedInteger()
        ni1.add(NestedInteger(1))
        ni1.add(NestedInteger(1))
        ni2 = NestedInteger(2)
        ni3 = NestedInteger()
        ni3.add(NestedInteger(1))
        ni3.add(NestedInteger(1))
        nestedList = [ni1, ni2, ni3]
        r = sol.depthSum(nestedList)
        print(r)
        assert r == 10

        ni1 = NestedInteger(1)
        ni2 = NestedInteger()
        ni2.add(NestedInteger(4))
        ni21 = NestedInteger()
        ni21.add(NestedInteger(6))
        ni2.add(ni21)
        nestedList = [ni1, ni2]
        r = sol.depthSum(nestedList)
        print(r)
        assert r == 27

    unitTest(Solution())
