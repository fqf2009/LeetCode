# Given an array of strings words, find the longest string in words such that
# every prefix of it is also in words.
# For example, let words = ["a", "app", "ap"]. The string "app" has prefixes
# "ap" and "a", all of which are in words.
# Return the string described above. If there is more than one string with
# the same length, return the lexicographically smallest one, and if no
# string exists, return "".

# Constraints:
#   1 <= words.length <= 10^5
#   1 <= words[i].length <= 10^5
#   1 <= sum(words[i].length) <= 10^5
from typing import List


# Trie (Prefix Tree): O(N), where N is all characters in all words
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = {}
        longestWord = [""]

        def add(word: str):
            branch = trie
            for ch in word:
                branch = branch.setdefault(ch, {})
            branch.setdefault('*', None)

        def dfsLongest(root: dict, prefix: str):
            if len(prefix) > 0 and '*' not in root: return
            for ch in root.keys():
                if ch != '*':
                    dfsLongest(root[ch], prefix + ch)
            if len(prefix) > len(longestWord[0]) or  \
               len(prefix) == len(longestWord[0]) and prefix < longestWord[0]:
                longestWord[0] = prefix

        for word in words:
            add(word)

        dfsLongest(trie, "")
        return longestWord[0]


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.longestWord(["k", "ki", "kir", "kira", "kiran"])
        print(r)
        assert r == 'kiran'

        r = sol.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])
        print(r)
        assert r == 'apple'

        r = sol.longestWord(["abc", "bc", "ab", "qwe"])
        print(r)
        assert r == ''

    unitTest(Solution())
