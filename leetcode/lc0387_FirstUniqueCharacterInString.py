# Given a string s, find the first non-repeating character in it and
# return its index. If it does not exist, return -1.
# Constraints:
#   1 <= s.length <= 10^5
#   s consists of only lowercase English letters.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        letterPos = {}
        for i, ch in enumerate(s):
            letterPos[ch] = 10**6 if ch in letterPos else i

        res = min(letterPos.values())
        return res if res < 10**6 else -1


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.firstUniqChar("leetcode")
        print(r)
        assert r == 0

        r = sol.firstUniqChar("loveleetcode")
        print(r)
        assert r == 2

        r = sol.firstUniqChar("aabb")
        print(r)
        assert r == -1

    unitTest(Solution())
