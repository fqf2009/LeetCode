# Let's define a function countUniqueChars(s) that returns the 
# number of unique characters on s.
#  - For example, calling countUniqueChars(s) if s = "LEETCODE" then
#    "L", "T", "C", "O", "D" are the unique characters since they 
#    appear only once in s, therefore countUniqueChars(s) = 5.
# Given a string s, return the sum of countUniqueChars(t) where t 
# is a substring of s.

# Notice that some substrings can be repeated so in this case you 
# have to count the repeated ones too.

# Constraints:
#   1 <= s.length <= 10^5
#   s consists of uppercase English letters only.


# DP - T/S: O(n), O(1)
# Analysis:
# - assume short code: c(s) for countUniqueChars(s),
#                      u(s) for uniqueLetterString(s)
# - e.g. for ABCB, we know u('ABC') = 10
#   some substrings from ABC can combine with 'B':
#      ABC (c=3)    BC (c=2)      C (c=1)
#   to ABCB, new substrings are:
#      ABCB (c=2),  BCB  (c=1),   CB (c=2),  B (c=1)
#   to ABCBB, new substrings are:
#      ABCBB (c=2), BCBB (c=1),   CBB (c=1), BB (c=0), B (c=1)
# - assume dp[i] is u(s[:i+1]), when adding a new char ch:
#   we only need two most recent left places where ch appeared,
#   asseume these two places are p1, p2, then approximately:
#   dp[i] = dp[i-1] - (p2 - p1) + (i - p2)
#   then, set p1, p2 = p2, i + 1
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        p1, p2 = [-1] * 26, [-1] * 26
        dp = 0
        res = 0
        for i, ch in enumerate(s):
            j = ord(ch) - ord('A')
            dp += - (p2[j] - p1[j]) + (i - p2[j])
            p1[j], p2[j] = p2[j], i
            res += dp

        return res


# What if we need to count distinct numbers of letters in all substring
# - Note the difference with the problem above:
#   for substring 'ABB', we count 1 unique char in above problem,
#   we count 2 (letter 'A', 'B') in this problem.
# - Assume:
#   dp[i] is distinct number of letters for all substring ending with s[i];
#   p[s[i]] (p[ch]) is char s[i]'s previous pos before position i;
# - all substring (ending with pos i), if starting pos is before (inclusive)
#   p[ch], ch is already counted, after p[ch], need to count it:
# - dp[i] = dp[i-1] + i - p[ch]
class Solution1:
    def countDistinctLettersInAllSubstring(self, s: str) -> int:
        p = [-1] * 26
        dp = 0
        res = 0
        for i, ch in enumerate(s):
            j = ord(ch) - ord('A')
            dp += i - p[j]
            res += dp
            p[j] = i

        return res


if __name__ == '__main__':
    def unitTest1(sol):
        r = sol.uniqueLetterString("A")
        print(r)
        assert r == 1

        r = sol.uniqueLetterString("AB")
        print(r)
        assert r == 4

        r = sol.uniqueLetterString("ABC")
        print(r)
        assert r == 10

        r = sol.uniqueLetterString("ABA")
        print(r)
        assert r == 8

        r = sol.uniqueLetterString("TEST")
        print(r)
        assert r == 18

        r = sol.uniqueLetterString("LEETCODE")
        print(r)
        assert r == 92

    def unitTest2(sol):
        r = sol.countDistinctLettersInAllSubstring("A")
        print(r)
        assert r == 1

        r = sol.countDistinctLettersInAllSubstring("AB")
        print(r)
        assert r == 4

        r = sol.countDistinctLettersInAllSubstring("ABC")
        print(r)
        assert r == 10

        r = sol.countDistinctLettersInAllSubstring("ABA")
        print(r)
        assert r == 9

        r = sol.countDistinctLettersInAllSubstring("TEST")
        print(r)
        assert r == 19

        r = sol.countDistinctLettersInAllSubstring("LEETCODE")
        print(r)
        assert r == 105

    unitTest1(Solution())
    unitTest2(Solution1())
