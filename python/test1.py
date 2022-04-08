from typing import List, Optional
from lib.ListUtil import ListNode, ListNodeUtil
from functools import cache


class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        q, r = divmod(n, 3)
        if r == 0:
            r = 1
        elif r == 1:
            r = 4
            q -= 1
        return 3**q * r


from typing import List
if __name__ == '__main__':
    def unit_test(sol):
        r = sol.integerBreak(10)
        print(r)
        assert r == 36

        r = sol.integerBreak(6)
        print(r)
        assert r == 9

    unit_test(Solution())
