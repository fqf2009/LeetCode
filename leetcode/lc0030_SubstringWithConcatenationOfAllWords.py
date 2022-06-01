# You are given a string s and an array of strings words of the
# same length. Return all starting indices of substring(s) in s
# that is a concatenation of each word in words exactly once, in
# any order, and without any intervening characters.
# You can return the answer in any order.
# Constraints:
#   1 <= s.length <= 10^4
#   s consists of lower-case English letters.
#   1 <= words.length <= 5000
#   1 <= words[i].length <= 30
#   words[i] consists of lower-case English letters.
from typing import Counter, List


# T/S: O(n*m*L), where n = len(s), m = len(words), L = len(words[0])
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        counts = Counter(words)
        word_len = len(words[0])
        res = []
        for i in range(0, len(s) - len(words) * word_len + 1):
            seen = Counter()
            for j in range(len(words)):
                s1 = s[i + j * word_len : i + (j + 1) * word_len]
                if seen[s1] >= counts[s1]:
                    break
                seen[s1] += 1
            else:
                res.append(i)

        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.findSubstring("barfoothefoobarman", words=["foo", "bar"])
        print(r)
        assert sorted(r) == [0, 9]

        r = sol.findSubstring("wordgoodgoodgoodbestword", words=["word", "good", "best", "word"])
        print(r)
        assert sorted(r) == []

        r = sol.findSubstring("barfoofoobarthefoobarman", words=["bar", "foo", "the"])
        print(r)
        assert sorted(r) == [6, 9, 12]

    unit_test(Solution())
