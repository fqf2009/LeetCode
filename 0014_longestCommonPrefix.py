from typing import List

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = min(map(len, strs))
        for m in range(n):
            ch = strs[0][m]
            for i in range(1, len(strs)):
                if strs[i][m] != ch:
                    return strs[0][:m]
        return strs[0][:n]


if __name__ == '__main__':
    sol = Solution()

    r = sol.longestCommonPrefix(["flower", "flow", "flight"])
    print(r)
    assert(r == 'fl')

    r = sol.longestCommonPrefix(["dog", "racecar", "car"])
    print(r)
    assert(r == '')
