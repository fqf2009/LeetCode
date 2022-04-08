# An original string, consisting of lowercase English letters, can be encoded
# by the following steps:
#  - Arbitrarily split it into a sequence of some number of non-empty substrings.
#  - Arbitrarily choose some elements (possibly none) of the sequence, and replace
#    each with its length (as a numeric string).
#  - Concatenate the sequence as the encoded string.
# For example, one way to encode an original string "abcdefghijklmnop" might be:
#  - Split it as a sequence: ["ab", "cdefghijklmn", "o", "p"].
#  - Choose the second and third elements to be replaced by their lengths, 
#    respectively. The sequence becomes ["ab", "12", "1", "p"].
#  - Concatenate the elements of the sequence to get the encoded string: "ab121p".
# Given two encoded strings s1 and s2, consisting of lowercase English letters 
# and digits 1-9 (inclusive), return true if there exists an original string that
# could be encoded as both s1 and s2. Otherwise, return false.
# Note: The test cases are generated such that the number of consecutive digits 
# in s1 and s2 does not exceed 3.
# Constraints:
#   1 <= s1.length, s2.length <= 40
#   s1 and s2 consist of digits 1-9 (inclusive), and lowercase English letters only.
#   The number of consecutive digits in s1 and s2 does not exceed 3.


# DP
# idea from: https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/discuss/1629836/Pythonor-Top-down-DP-or-Steps-simplified-or-Commented-or-90.98-Time-or-72.42-Mem
# Analysis:
# - dp(i, j, lead) to check possibly equal for s1[i:], s2[j:], and
#   the lead is the number of char the s1[:i+1] lead over s1[:j+1].
# - the reason for lead is that both s1[:i+1] and s1[:j+1] can have digits.
# - only when lead == 0, and both s1[i] and s2[i] are not digit, they can be
#   compared, and then either move forward or return false (backtrack)
# - if s1[i] (or s2[j], similar) is digit, enumerate all the lengths combination
#   from prefix digits, perform dp(i+len(prefix), j, lead + lengths[k]) for each.
# - return True only when both i, j reach end of s1 and s2, and diff == 0 as well.
# - e.g.: s1 = "l123es", s2 = "44s"
#   dp(0, 0, 0)             => s2[0] = "4" => prefix = "44", lengths = [8, 44]
#   -> dp(0, 2, -8)         => s1[0] and s2[2] are not digits, but lead < 0
#      -> dp(1, 2, -7)      => s1[1] = "1" => prefix = "123", lengths = [6, 15, 24, 123]
#         -> dp(4, 2, -1)   => s1[4] and s2[2] are not digits, but lead < 0
#            -> dp(5, 2, 0) => s1[5] == s2[2]
#               -> dp(6, 3, 0) => i == len(s1) and j == len(s2) and lead == True
from functools import cache


class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        def prefix_digits_len(s: str):
            res = 0
            for ch in s:
                if not ch.isdigit():
                    break
                res += 1
            return res

        @cache
        def possible_lengths(s: str):
            res = {int(s)}
            for i in range(1, len(s)):
                res |= {x + y for x in possible_lengths(s[:i]) for y in possible_lengths(s[i:])}
            return res
        
        @cache
        def dp_match(i, j, lead):
            if i == len(s1) and j == len(s2):
                return lead == 0
            
            if i < len(s1) and s1[i].isdigit():
                prefix_len = prefix_digits_len(s1[i:])
                for substr_len in possible_lengths(s1[i: i + prefix_len]):
                    if dp_match(i + prefix_len, j, lead + substr_len):
                        return True
            elif j < len(s2) and s2[j].isdigit():
                prefix_len = prefix_digits_len(s2[j:])
                for substr_len in possible_lengths(s2[j: j + prefix_len]):
                    if dp_match(i, j + prefix_len, lead - substr_len):
                        return True
            elif lead == 0:
                if i == len(s1) or j == len(s2) or s1[i] != s2[j]:
                    return False
                return dp_match(i+1, j+1, 0)
            elif lead > 0:
                if j == len(s2): return False
                return dp_match(i, j+1, lead-1)
            else: # lead < 0
                if i == len(s1): return False
                return dp_match(i + 1, j, lead+1)

            return False

        return dp_match(0, 0, 0)


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.possiblyEquals(s1 = "internationalization", s2 = "i18n")
        print(r)
        assert r == True

        r = sol.possiblyEquals(s1 = "l123e", s2 = "44")
        print(r)
        assert r == True    # e.g.: ["l", "e", "et", "cod", "e"] v.s. ["leet", "code"]


        r = sol.possiblyEquals(s1 = "a5b", s2 = "c5b")
        print(r)
        assert r == False

    unit_test(Solution())
