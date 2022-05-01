# The appeal of a string is the number of distinct characters found in the string.
# For example, the appeal of "abbca" is 3 because it has 3 distinct characters: 'a', 'b', and 'c'.
# Given a string s, return the total appeal of all of its substrings.
# A substring is a contiguous sequence of characters within a string.
# Constraints:
#   1 <= s.length <= 10^5
#   s consists of lowercase English letters.


# DP -  T/S: O(n), O(1)
# Analysis:
# - assume dp[i] is appeal of all substrings ending with pos i.
#   dp[i] = dp[i-1] + (i - prev_pos_of_current_char)
class Solution:
    def appealSum(self, s: str) -> int:
        res, dp = 0, 0
        pos = {}
        for i, ch in enumerate(s):
            dp += i - pos.get(ch, -1)
            pos[ch] = i
            res += dp

        return res

if __name__ == '__main__':
    def unit_test(sol):
        r = sol.appealSum("abbca")
        print(r)
        assert r == 28

        r = sol.appealSum("code")
        print(r)
        assert r == 20

    unit_test(Solution())
