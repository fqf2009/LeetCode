# You are given a string s and an array of strings words. You should 
# add a closed pair of bold tag <b> and </b> to wrap the substrings 
# in s that exist in words. If two such substrings overlap, you should 
# wrap them together with only one pair of closed bold-tag. If two 
# substrings wrapped by bold tags are consecutive, you should combine them.
# Return s after adding the bold tags.
# Constraints:
#   1 <= s.length <= 1000
#   0 <= words.length <= 100
#   1 <= words[i].length <= 1000
#   s and words[i] consist of English letters and digits.
#   All the values of words are unique.
from typing import List


# Trie - T/S: O(n*W), O(m*W), where n = len(s), W = avg(words length), m = len(words)
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        trie = {}
        for word in words:  # build trie
            branch = trie
            for ch in word:
                branch = branch.setdefault(ch, {})
            branch['*'] = None
        
        # match words using trie
        word_pos = []
        for i in range(len(s)):
            word_end = -1
            branch = trie
            for j in range(i, len(s)):
                if s[j] not in branch: break
                branch = branch[s[j]]
                if '*' in branch:
                    word_end = j
            if word_end >= 0:       # merge interval
                if word_pos and word_pos[-1][1] >= i-1:
                    word_pos[-1][1] = max(word_pos[-1][1], word_end)
                else:
                    word_pos.append([i, word_end])

        res = []
        word_end = -1
        for i, j in word_pos:
            res.append(s[word_end + 1: i])
            res.extend(["<b>", s[i: j+1], "</b>"])
            word_end = j
        res.append(s[word_end + 1: len(s)])
        
        return "".join(res)


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.addBoldTag("aaabbcc", ["aaa","aab","bc","aaabbcc"])
        print(r)
        assert r == "<b>aaabbcc</b>"

        r = sol.addBoldTag("abcxyz123", words = ["abc","123"])
        print(r)
        assert r == "<b>abc</b>xyz<b>123</b>"

        r = sol.addBoldTag("aaabbcc", words = ["aaa","aab","bc"])
        print(r)
        assert r == "<b>aaabbc</b>c"

    unit_test(Solution())
