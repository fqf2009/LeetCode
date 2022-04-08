# A binary string is monotone increasing if it consists of some number of
# 0's (possibly none), followed by some number of 1's (also possibly none).
# You are given a binary string s. You can flip s[i] changing it from
# 0 to 1 or from 1 to 0.
# Return the minimum number of flips to make s monotone increasing.
# Constraints:
#   1 <= s.length <= 10^5
#   s[i] is either '0' or '1'.


# DP - T/S: O(n), O(1)
# Analysis:
# - dp1[i]: always turn 1 to 0, flips by far
#   dp2[i]: always turn 0 to 1, flips by far
# - dp1[i] = dp1[i-1] + int(s[i])
#   dp2[i] = min(dp2[i-1] + 1 - int(s[i]), dp1[i])
# - result is min(dp1[-1], dp2[-1])
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp1 = dp2 = 0
        for ch in s:
            dp1 += int(ch)
            dp2 = min(dp1, dp2 + 1 - int(ch))

        return min(dp1, dp2)


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.minFlipsMonoIncr("00110")
        print(r)
        assert r == 1

        r = sol.minFlipsMonoIncr('010110')
        print(r)
        assert r == 2

        r = sol.minFlipsMonoIncr('00011000')
        print(r)
        assert r == 2

    unitTest(Solution())
