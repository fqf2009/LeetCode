# You are given a binary string s and a positive integer k.
# Return the length of the longest subsequence of s that 
# makes up a binary number less than or equal to k.
# Note:
# - The subsequence can contain leading zeroes.
# - The empty string is considered to be equal to 0.
# - A subsequence is a string that can be derived from another string 
#   by deleting some or no characters without changing the order 
#   of the remaining characters.
# Constraints:
#   1 <= s.length <= 1000
#   s[i] is either '0' or '1'.
#   1 <= k <= 10^9


# - from right to left, add each bit, if the value of those
#   bits is no greater than k, count them, otherwise, only
#   count 0's
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        res = 0
        val = 0
        power = 1
        for ch in reversed(s):
            if ch == '1':
                val += power
                if val <= k:
                    res += 1
            else:
                res += 1
            power *= 2

        return res


class Solution1:
    def longestSubsequence(self, s: str, k: int) -> int:
        res, val, power = 0, 0, 1
        for ch in reversed(s):
            val += power * int(ch)
            power *= 2
            res += 1 if (ch == '0' or val <= k) else 0

        return res


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.longestSubsequence(s = "1001010", k = 5)
        print(r)
        assert r == 5

        r = sol.longestSubsequence("00101001", k = 1)
        print(r)
        assert r == 6

        r = sol.longestSubsequence("00101001", k = 9)
        print(r)
        assert r == 7

    unit_test(Solution())
    unit_test(Solution1())
