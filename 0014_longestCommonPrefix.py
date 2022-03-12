from typing import List

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Constraints:
#   1 <= strs.length

# Pythonic way
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        prefixLen = 0
        for chars in zip(*strs):    # '*' is the key, each string is an iterable
            if len(set(chars)) != 1:
                return strs[0][:prefixLen]
            prefixLen += 1
        return strs[0][:prefixLen]


# Time complexity: O(n*m), n is len(strs), m is len(longest common prefix)
class Solution1:
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
