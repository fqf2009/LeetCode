# You are given a string s and an integer k. You can choose any
# character of the string and change it to any other uppercase 
# English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same 
# letter you can get after performing the above operations.
# Constraints:
#   1 <= s.length <= 10^5
#   s consists of only uppercase English letters.
#   0 <= k <= s.length
from typing import Counter


# Sliding window - T/S: O(n), O(1)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cntr = Counter()
        left, res = 0, 0
        for i, ch in enumerate(s):  # i means expand the winndow
            cntr[ch] += 1
            # pick the most freq char, others are replaced
            # if replacement count > k, shrink the window
            while i - left + 1 - max(cntr.values()) > k: 
                cntr[s[left]] -= 1
                left += 1
            res = max(res, i - left + 1)

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.characterReplacement("ABAB", k = 2)
        print(r)
        assert r == 4

        r = sol.characterReplacement("AABABBA", k = 1)
        print(r)
        assert r == 4


    unitTest(Solution())
