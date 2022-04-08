# Given a string s, find the length of the longest substring without repeating characters.


# Two pointers, Dict
class Solution:
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
class Solution1:
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
    def unitTest(sol):
        n = sol.lengthOfLongestSubstring('abcabcbb')
        print(n)
        assert n == 3

        n = sol.lengthOfLongestSubstring('bbbbb')
        print(n)
        assert n == 1

        n = sol.lengthOfLongestSubstring('pwwkew')
        print(n)
        assert n == 3

    unitTest(Solution())
    unitTest(Solution1())
