# In an alien language, surprisingly, they also use English lowercase
# letters, but possibly in a different order. The order of the alphabet
# is some permutation of lowercase letters.
# Given a sequence of words written in the alien language, and the order
# of the alphabet, return true if and only if the given words are sorted
# lexicographically in this alien language.
# Constraints:
#   1 <= words.length <= 100
#   1 <= words[i].length <= 20
#   order.length == 26
#   All characters in words[i] and order are English lowercase letters.
from typing import List


# Dict (HashMap)
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        if n == 1:
            return True
        letterOrders = {x:i for i, x in enumerate(order)}
        for i in range(n - 1):
            w1, w2 = words[i], words[i+1]
            l1, l2 = len(w1), len(w2)
            for ch1, ch2 in zip(w1, w2):
                if letterOrders[ch1] > letterOrders[ch2]:
                    return False
                if letterOrders[ch1] < letterOrders[ch2]:
                    break
            else:
                if l1 > l2:
                    return False

        return True


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
        print(r)
        assert r == True

        r = sol.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz")
        print(r)
        assert r == False

        r = sol.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz")
        print(r)
        assert r == False

    unitTest(Solution())
