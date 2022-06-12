# Given a string s, return the length of the longest substring
# that contains at most two distinct characters.
# Constraints:
#   1 <= s.length <= 105
#   s consists of English letters.


# Sliding window - T/S O(n), O(1)
# - remember last pos of every char in sliding window
# - when the number of distinct char in window exceeds 3, remove
#   the char with the smallest last pos from sliding window
# - the result is the largest length of sliding window
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        charPos = {}
        left, res = -1, 0
        for i, ch in enumerate(s):
            charPos[ch] = i
            if len(charPos) == 3:
                left, ch1 = min((pos, ch) for ch, pos in charPos.items())
                del charPos[ch1]
            res = max(res, i - left)

        return res


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.lengthOfLongestSubstringTwoDistinct("eceba")
        print(r)
        assert r == 3

        r = sol.lengthOfLongestSubstringTwoDistinct("ccaabbb")
        print(r)
        assert r == 5

        r = sol.lengthOfLongestSubstringTwoDistinct("aaa")
        print(r)
        assert r == 3

    unitTest(Solution())
