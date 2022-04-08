# You are given a string s containing lowercase English letters, 
# and a matrix shift, where shift[i] = [directioni, amounti]:
#  - directioni can be 0 (for left shift) or 1 (for right shift).
#  - amounti is the amount by which string s is to be shifted.
#  - A left shift by 1 means remove the first character of s and 
#    append it to the end.
#  - Similarly, a right shift by 1 means remove the last character 
#    of s and add it to the beginning.
# Return the final string after all operations.
from functools import reduce
from typing import List

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        nShift = reduce(lambda x, y: x + y , map(lambda x: (x[0]*2-1)*x[1], shift))
        n = len(s)
        nShift %= n
        if nShift == 0:
            return s
        else:
            return s[-nShift:] + s[:n-nShift]

if __name__ == '__main__':
    def unitTest(sol):
        r = sol.stringShift("joiazl", [[1,1],[1,6],[0,1],[1,3],[1,0],[0,3]])
        print(r)
        assert r == "joiazl"

        r = sol.stringShift(s = "abc", shift = [[0,1],[1,2]])
        print(r)
        assert r == "cab"

        r = sol.stringShift(s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]])
        print(r)
        assert r == "efgabcd"

    unitTest(Solution())
