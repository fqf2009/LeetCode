# You are given a 0-indexed string array words, where words[i] consists 
# of lowercase English letters.
# In one operation, select any index i such that 0 < i < words.length 
# and words[i - 1] and words[i] are anagrams, and delete words[i] from 
# words. Keep performing this operation as long as you can select an 
# index that satisfies the conditions.
# Return words after performing all operations. It can be shown that
# selecting the indices for each operation in any arbitrary order will 
# lead to the same result.
# An Anagram is a word or phrase formed by rearranging the letters of 
# a different word or phrase using all the original letters exactly once. 
# For example, "dacb" is an anagram of "abdc".
# Constraints:
#   1 <= words.length <= 100
#   1 <= words[i].length <= 10
#   words[i] consists of lowercase English letters.
from typing import Counter, List


# Counter to avoid sorting
class Solution2:
    def removeAnagrams(self, w: List[str]) -> List[str]:
        return [w[i] for i in range(len(w)) 
                        if i == 0 or Counter(w[i]) != Counter(w[i-1])]

# Oneliner
class Solution1:
    def removeAnagrams(self, w: List[str]) -> List[str]:
        return [w[i] for i in range(len(w)) 
                        if i == 0 or sorted(w[i]) != sorted(w[i-1])]


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        w1 = words[0]
        res = [w1]
        for w2 in words[1:]:
            if sorted(w1) != sorted(w2):
                res.append(w2)
            w1 = w2

        return res


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.removeAnagrams(["a","b","a"])
        print(r)
        assert r == ["a", "b", "a"]

        r = sol.removeAnagrams(["abba","baba","bbaa","cd","cd"])
        print(r)
        assert r == ["abba","cd"]

        r = sol.removeAnagrams(["a","b","c","d","e"])
        print(r)
        assert r == ["a","b","c","d","e"]

    unit_test(Solution())
    unit_test(Solution1())
    unit_test(Solution2())
