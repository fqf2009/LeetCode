# You are given two strings order and s. All the words of order are unique
# and were sorted in some custom order previously.
# Permute the characters of s so that they match the order that order was 
# sorted. More specifically, if a character x occurs before a character y 
# in order, then x should occur before y in the permuted string.
# Return any permutation of s that satisfies this property.
# Constraints:
#   1 <= order.length <= 26
#   1 <= s.length <= 200
#   order and s consist of lowercase English letters.
#   All the characters of order are unique.
from collections import Counter


# Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        letter_counter = Counter(s)
        res = []
        for ch in order:
            res.append(ch * letter_counter[ch])     # Counter return 0 for non-existing key
            del letter_counter[ch]

        for ch, freq in letter_counter.items():
            res.append(ch * freq)

        return ''.join(res)


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.customSortString(order = "cba", s = "abcd")
        print(r)
        assert r == "cbad"

        r = sol.customSortString(order = "cbafg", s = "abcd")
        print(r)
        assert r == "cbad"

    unit_test(Solution())
