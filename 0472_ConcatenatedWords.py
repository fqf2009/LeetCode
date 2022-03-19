# Given an array of strings words (without duplicates), return all the
# concatenated words in the given list of words.
# A concatenated word is defined as a string that is comprised entirely
# of at least two shorter words in the given array.
# Constraints:
#   1 <= words.length <= 10^4
#   0 <= words[i].length <= 30
#   words[i] consists of only lowercase English letters.
#   0 <= sum(words[i].length) <= 10^5
from typing import List


# Dict + DFS
# - not any faster than Solution1, string slicing does not consume much resource
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)

        def isConcatenated(word: str, subWordPos: List[int]):
            if len(word) == 0:
                return len(subWordPos) > 1
            for i in range(len(word)):
                if word[:i+1] in wordSet:
                    subWordPos.append(i)
                    if isConcatenated(word[i+1:], subWordPos):
                        return True
                    subWordPos.pop()
            return False

        return [word for word in words if isConcatenated(word, [])]


# Dict + DFS
class Solution1:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)

        def isConcatenated(word: str, subWords: List[str]):
            if len(word) == 0:
                return len(subWords) > 1
            for i in range(len(word)):
                if word[:i+1] in wordSet:
                    subWords.append(word[:i+1])
                    if isConcatenated(word[i+1:], subWords):
                        return True
                    subWords.pop()
            return False

        return [word for word in words if isConcatenated(word, [])]


if __name__ == '__main__':
    def unitTest(sol):
        words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog",
                 "hippopotamuses", "rat", "ratcatdogcat"]
        r = sol.findAllConcatenatedWordsInADict(words)
        print(r)
        assert r == ["catsdogcats", "dogcatsdog", "ratcatdogcat"]

        r = sol.findAllConcatenatedWordsInADict(["cat", "dog", "catdog"])
        print(r)
        assert r == ["catdog"]

    unitTest(Solution())
    unitTest(Solution1())
