# You are given an array of strings words and a string pref.
# Return the number of strings in words that contain pref as a prefix.
# A prefix of a string s is any leading contiguous substring of s.
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(1 for s in words if s.startswith(pref))


class Solution1:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for s in words:
            if s.startswith(pref):
                res += 1
        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.prefixCount(["pay","attention","practice","attend"], pref = "at")
        print(r)
        assert r == 2

        r = sol.prefixCount(["leetcode","win","loops","success"], pref = "code")
        print(r)
        assert r == 0
        
    unitTest(Solution())
    unitTest(Solution1())
