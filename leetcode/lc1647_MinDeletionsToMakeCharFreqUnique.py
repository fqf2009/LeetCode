# A string s is called good if there are no two different characters in s
# that have the same frequency.
# Given a string s, return the minimum number of characters you need to
# delete to make s good.
# The frequency of a character in a string is the number of times it
# appears in the string. For example, in the string "aab", the
# frequency of 'a' is 2, while the frequency of 'b' is 1.
# Constraints:
#   1 <= s.length <= 10^5
#   s contains only lowercase English letters.
from typing import Counter


# T/S: O(n + k*log(k) + k), O(k), where k = unique_chars(s), k <= 26
class Solution:
    def minDeletions(self, s: str) -> int:
        freq_used = set()
        next_freq = len(s)
        res = 0
        for freq, _ in sorted(((freq, ch) for ch, freq in Counter(s).items()), reverse=True):
            for i in reversed(range(min(next_freq, freq) + 1)):
                if i not in freq_used:
                    if i > 0:
                        freq_used.add(i)
                    res += freq - i
                    next_freq = max(i - 1, 0)
                    break

        return res


# T/S: O(n + k^2), O(k), where k = unique_chars(s), k <= 26
# - It's fine to not sort
class Solution1:
    def minDeletions(self, s: str) -> int:
        freq_used = set()
        res = 0
        for freq in Counter(s).values():
            while freq > 0 and freq in freq_used:
                res += 1
                freq -= 1
            freq_used.add(freq)

        return res


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.minDeletions("aab")
        print(r)
        assert r == 0

        r = sol.minDeletions("aaabbbcc")
        print(r)
        assert r == 2

        r = sol.minDeletions("ceabaacb")
        print(r)
        assert r == 2

    unitTest(Solution())
    unitTest(Solution1())
