# We can shift a string by shifting each of its letters to its successive letter.
# For example, "abc" can be shifted to be "bcd".
# We can keep shifting the string to form a sequence.
# For example, we can keep shifting "abc" to form the sequence:
# "abc" -> "bcd" -> ... -> "xyz".
# Given an array of strings strings, group all strings[i] that belong to the
# same shifting sequence. You may return the answer in any order.
# Constraints:
#   1 <= strings.length <= 200
#   1 <= strings[i].length <= 50
#   strings[i] consists of lowercase English letters.
from typing import List
from collections import defaultdict


# Simplify the hashing
# - what matters, or the invariant part, is the other letters' relative
#   lexical distance to the first letter;
# - e.g. from "ab" => 'b' - 'a' = 1
#        to   "bc" => 'c' - 'b' = 1
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for s in strings:
            key = tuple((ord(ch)-ord(s[0]))%26 for ch in s)
            map[key].append(s)

        return list(map.values())


# Find patterns: O(n)
# - normalize the string to the form: with leading letter as 'a'
# - use a map to store all strings with the same normalized form
class Solution1:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def normalize(s: str) -> str:
            base = ord("a")
            diff = ord(s[0]) - base
            return "".join(chr((ord(ch) - base - diff) % 26 + base) for ch in s)

        map = {}
        for s in strings:
            map.setdefault(normalize(s), []).append(s)

        return list(map.values())


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
        r = sorted(r)
        print(r)
        assert sorted(r) == [["a", "z"], ["abc", "bcd", "xyz"], ["acef"], ["az", "ba"]]

        r = sol.groupStrings(["a"])
        print(r)
        assert sorted(r) == [["a"]]

    unit_test(Solution())
    unit_test(Solution1())
