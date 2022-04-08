# A subsequence of a string is a new string that is formed 
# from the original string by deleting some (can be none) 
# of the characters without disturbing the relative positions 
# of the remaining characters. (i.e., "ace" is a subsequence 
# of "abcde" while "aec" is not).

# Given two strings source and target, return the minimum 
# number of subsequences of source such that their concatenation 
# equals target. If the task is impossible, return -1.

# Constraints:
#   1 <= source.length, target.length <= 1000
#   source and target consist of lowercase English letters.


# Two pointers
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        srcCharset = set(source)
        for ch in target:
            if ch not in srcCharset:
                return -1

        m, n = len(source), len(target)
        i, j, res = 0, 0, 0
        while j < n:
            if source[i] == target[j]:
                j += 1
            i += 1
            if i == m:
                res += 1
                i = 0

        return res + 1 if i > 0 else res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.shortestWay(source = "abc", target = "abcbc")
        print(r)
        assert r == 2

        r = sol.shortestWay(source = "abc", target = "acdbc")
        print(r)
        assert r == -1

        r = sol.shortestWay(source = "xyz", target = "xzyxz")
        print(r)
        assert r == 3

        r = sol.shortestWay(source = "aaaaa", target = "aaaaaaaaaaaaa")
        print(r)
        assert r == 3

    unitTest(Solution())
