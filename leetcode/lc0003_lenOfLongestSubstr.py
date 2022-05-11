# Given a string s, find the length of the longest substring without repeating characters.
# Constraints:
#   0 <= s.length <= 5 * 10^4
#   s consists of English letters, digits, symbols and spaces.


# Two pointers, Dict - T/S: O(n), O(256) -> O(1)
# - just adjust first pointer, no need to iterate through list
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_pos = {}
        start, max_len = -1, 0
        for i, ch in enumerate(s):
            start = max(start, letter_pos.get(ch, -1))
            max_len = max(max_len, i - start)
            letter_pos[ch] = i

        return max_len


# Two pointers, Dict
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        maxLen, p = 0, -1
        for i, ch in enumerate(s):
            if ch not in letters:
                letters[ch] = i
                maxLen = max(i - p, maxLen)
            else:
                for j in range(p+1, letters[ch]):
                    del letters[s[j]]
                p = letters[ch]

        return maxLen


# Two pointers, Set
# - i points to current letter during the scan, j points to the pos before the beginning of str
# - if no repeating, add s[j] to a set
# - if repeating (already in set), move j forward and remove s[j] from set, until
#   s[j] == s[i], i.e., now j points to previous occurrence of s[i], so that (s[j+1], ..., s[i])  
#   is a new sub-str without repeating char.
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        maxLen, j = 0, -1
        for i, ch in enumerate(s):
            if ch not in letters:
                letters.add(ch)
                maxLen = max(i - j, maxLen)
            else:
                while s[j + 1] != ch:
                    j += 1
                    letters.remove(s[j])
                j += 1

        return maxLen


if __name__ == '__main__':
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,), (Solution1,), (Solution2,)])
    class TestSolution(TestCase):
        @parameterized.expand([
            ('abcabcbb', 3),
            ('bbbbb', 1),
            ('pwwkew', 3),
            (' ', 1),
        ])
        def test_lengthOfLongestSubstring(self, s, expected):
            sol = self.solution()       # type:ignore
            r = sol.lengthOfLongestSubstring(s)
            print(r)
            self.assertEqual(r, expected)

    main()
