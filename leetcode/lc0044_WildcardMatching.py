# Given an input string (s) and a pattern (p), implement wildcard
# pattern matching with support for '?' and '*' where:
#   '?' Matches any single character.
#   '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

# Constraints:
#   0 <= s.length, p.length <= 2000
#   s contains only lowercase English letters.
#   p contains only lowercase English letters, '?' or '*'.
from functools import cache


# Backtracking
# Time: O(min(S,P)) in best case, O(S*log(P)) in average, O(S*P) in worst case
# Algorithm:
# - Assume s_len = len(s), p_len = len(p)
# - Use tow pointers i and j to loop over s and p
# - if s[i] = p[j], or p[j] = '?', continue the loop
# - if p[j] = '*', save i, j (i_save, j_star) for backtracking, in case
#   if it later fails. But now, first try let '*' match zero char, i.e.,
#   j += 1, i remains the same, loop;
# - if fails, check saved i_save, if exists, i = i_save + 1, continue loop
#   if no saved i_save, fail.
# - when i reaches s_len, check j, if j reaches p_len, or remaining char in p are
#   all '*', return true, otherwise false.
#
# Note: why only need to back track the most recent '*'?
# - assume: s = '…pqr…xy[y]…pqr…xyz'
#           p = '*pqr*xy[z]'
# - when the match fails at the chars in brackets, one possible fix is to backtrack
#   to the first *, not only the most recent *.
# - however, the second (the most recent in the case) can also fix the mismatch.
# - if a mismatch can be fixed with non-most-recent *, it can also be fixed by the 
#   most recent *.
# - if it cannot be fixed by the most recent *, there is no point in backtracking further.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        i_save = j_star = -1
        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                i_save = i
                j_star = j
                j += 1          # '*' match 0 char 
            elif j_star == -1:  # j >= len(p) or p[j] not in ['?', '*', s[i]]
                return False
            else:
                i = i_save + 1  # '*' match 1 more char 
                j = j_star + 1  # j_star will not change untill next '*'
                i_save = i      # i_save keep moving

        return j == len(p) or all(p[x] == '*' for x in range(j, len(p)))


# Recursion with Memoization: O(S*P)
# slight improvement: hash on int, not on string
class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        def removeDuplicateStar(p: str) -> str:
            res = []
            for ch in p:
                if ch == '*' and len(res) > 0 and res[-1] == '*':
                    continue
                res.append(ch)
            return ''.join(res)

        @cache
        def match(si: int, pi: int) -> bool:
            s, p = src[si:], pat[pi:]
            if len(s) == 0 and len(p) == 0:
                return True
            if p == '*':
                return True
            if len(s) == 0 or len(p) == 0:
                return False
            if s[0] == p[0] or p[0] == '?':
                return match(si+1, pi+1)
            if p[0] == '*':
                return match(si, pi+1) or match(si+1, pi)
            return False

        src = s
        pat = removeDuplicateStar(p)
        return match(0, 0)


# Recursion with Memoization
# T/S: O(S*P*(S+P)), O(S*P), where S=len(s), P=len(p)
# - assume dp[(s,p)] is a dict to map (s, p) to bool (match or not)
# - if dp[(s,p)] is set, return the value
# - if both s and p is empty, return True
# - if p=='*', set dp[(s,p)]=True, (Note '' and '*' matches)
# - if only one of p and s is empty, set dp=False (i.e., dp[(s,p)])
# - if s[0]==p[0] or p[0]=='?', dp=dp[s[1:], p[1:]]
# - if p[0]=='*', two possiblities:
#       dp=dp[s, p[1:]], i.e., '*' matches zero char in s. or,
#       dp=dp[s[1:], p], i.e., '*' matches one or more char in s.
# - if s[0] != p[0], dp=False
class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        def removeDuplicateStar(p: str) -> str:
            res = []
            for ch in p:
                if ch == '*' and len(res) > 0 and res[-1] == '*':
                    continue
                res.append(ch)
            return ''.join(res)

        @cache
        def match(s: str, p: str) -> bool:
            if len(s) == 0 and len(p) == 0:
                return True
            if p == '*':
                return True
            if len(s) == 0 or len(p) == 0:
                return False
            if s[0] == p[0] or p[0] == '?':
                return match(s[1:], p[1:])
            if p[0] == '*':
                return match(s, p[1:]) or match(s[1:], p)
            return False

        return match(s, removeDuplicateStar(p))


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.isMatch(s="", p="******")
        print(r)
        assert r == True

        r = sol.isMatch(s="aa", p="aa")
        print(r)
        assert r == True

        r = sol.isMatch(s="aa", p="a")
        print(r)
        assert r == False

        r = sol.isMatch(s="aa", p="?a")
        print(r)
        assert r == True

        r = sol.isMatch(s="aa", p="*aa")
        print(r)
        assert r == True

        r = sol.isMatch(s="aa", p="*")
        print(r)
        assert r == True

        r = sol.isMatch(s="aa", p="*a")
        print(r)
        assert r == True

        r = sol.isMatch(s="aa", p="*b")
        print(r)
        assert r == False

        r = sol.isMatch(s="cb", p="?a")
        print(r)
        assert r == False

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
