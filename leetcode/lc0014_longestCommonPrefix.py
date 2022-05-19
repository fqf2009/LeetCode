# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Constraints:
#   1 <= strs.length <= 200
#   0 <= strs[i].length <= 200
#   1 <= strs.length
from typing import List


# solution from: os.path.commonprefix
class Solution2:
    def longestCommonPrefix(self, m: List[str]) -> str:
        s1 = min(m)
        s2 = max(m)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1


# Pythonic way
class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        # '*' to unpacks a list or tuple into position arguments;
        # note that each string itself is an iterable
        prefixLen = 0
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) != 1:
                return strs[0][:i]
            prefixLen += 1

        return strs[0][:prefixLen]


# Time complexity: O(n*m), n is len(strs), m is len(longest common prefix)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        n = min(map(len, strs))
        for m in range(n):
            ch = strs[0][m]
            for i in range(1, len(strs)):
                if strs[i][m] != ch:
                    return strs[0][:m]
        return strs[0][:n]


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.longestCommonPrefix(["flower", "flow", "flight"])
        print(r)
        assert(r == 'fl')

        r = sol.longestCommonPrefix(["flower", "flow", "fl"])
        print(r)
        assert(r == 'fl')

        r = sol.longestCommonPrefix(["dog", "racecar", "car"])
        print(r)
        assert(r == '')

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
