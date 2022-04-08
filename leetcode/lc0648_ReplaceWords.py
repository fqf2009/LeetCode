# In English, we have a concept called root, which can be followed by 
# some other word to form another longer word - let's call this word 
# successor. For example, when the root "an" is followed by the successor
# word "other", we can form a new word "another".
# Given a dictionary consisting of many roots and a sentence consisting 
# of words separated by spaces, replace all the successors in the sentence 
# with the root forming it. If a successor can be replaced by more than one
# root, replace it with the root that has the shortest length.
# Return the sentence after the replacement.
# Constraints:
#   1 <= dictionary.length <= 1000
#   1 <= dictionary[i].length <= 100
#   dictionary[i] consists of only lower-case letters.
#   1 <= sentence.length <= 106
#   sentence consists of only lower-case letters and spaces.
#   The number of words in sentence is in the range [1, 1000]
#   The length of each word in sentence is in the range [1, 1000]
#   Every two consecutive words in sentence will be separated by exactly one space.
#   sentence does not have leading or trailing spaces.
from typing import List


# Set (hashtable)
# - T/S: O(n*w^2), O(m+n), where n = len(sentence),
#        w = avg_width(words in dictionary), m = len(dictionary)
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        words = sentence.split()
        res = []
        for word in words:
            for i in range(1, len(word)+1):
                if word[:i] in roots:
                    res.append(word[:i])
                    break
            else:
                res.append(word)
        
        return ' '.join(res)


# Trie: T/S: O(n*w), O(m+n)
class Solution1:
    pass


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery")
        print(r)
        assert r == "the cat was rat by the bat"

        r = sol.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs")
        print(r)
        assert r == "a a b c"

    unitTest(Solution())
