# You are given a string s consisting only of characters 'a' and 'b'​​​​.
# You can delete any number of characters in s to make s balanced.
# s is balanced if there is no pair of indices (i,j) such that i < j
# and s[i] = 'b' and s[j]= 'a'.
# Return the minimum number of deletions needed to make s balanced.
# Constraints:
#   1 <= s.length <= 10^5
#   s[i] is 'a' or 'b'​​.


# DP
# - dp[i], at pos i, min deletions to make string balanced
class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp, bcount = 0, 0
        for ch in s:
            if ch == 'a':               # either remove all previous 'b',
                dp = min(dp+1, bcount)  # or one more 'a' on prev balanced state
            else:
                bcount += 1     # encountered 'b' by far

        return dp


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.minimumDeletions("ababaaaabbbbbaaababbbbbbaaabbaababbabbbbaabbbbaabbabbabaabbbababaa")
        print(r)
        assert r == 25

        r = sol.minimumDeletions("aababbab")
        print(r)
        assert r == 2

        r = sol.minimumDeletions("bbaaaaabb")
        print(r)
        assert r == 2

    unitTest(Solution())
