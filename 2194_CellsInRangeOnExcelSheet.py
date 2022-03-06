from typing import List, Optional
from lib.ListUtil import ListNode, ListNodeUtil
from functools import cache


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1, c2 = s[0], s[3]
        r1, r2 = s[1], s[4]
        res = []
        for i in range(ord(c1), ord(c2)+1):
            for j in range(ord(r1), ord(r2)+1):
                res.append(chr(i) + chr(j))
        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.cellsInRange("K1:L2")
        print(r)
        assert r == ["K1", "K2", "L1", "L2"]

        r = sol.cellsInRange(s="A1:F1")
        print(r)
        assert r == ["A1", "B1", "C1", "D1", "E1", "F1"]

    unitTest(Solution())
