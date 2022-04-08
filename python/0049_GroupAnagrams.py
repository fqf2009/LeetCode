# Given an array of strings strs, group the anagrams together. You can
# return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly once.
# Constraints:
#   1 <= strs.length <= 10^4
#   0 <= strs[i].length <= 100
#   strs[i] consists of lowercase English letters.
from typing import List
from collections import Counter


# group by sorted string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}
        for s in strs:
            grp.setdefault(tuple(sorted(s)), list()).append(s)

        return list(grp.values())


# Counter - T/S: O(n*k), O(n), where k is avg length of strings
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}
        for s in strs:
            grp.setdefault(frozenset(Counter(s).items()), list()).append(s)

        return list(grp.values())


# this is wrong, because each string can have repeated letters
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}
        for s in strs:
            grp.setdefault(frozenset(s), list()).append(s)

        return list(grp.values())


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        print(r)
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        for x in expected:
            x.sort()
        for x in r:
            x.sort()
        assert sorted(r) == sorted(expected)

        r = sol.groupAnagrams(["ddddddddddg", "dgggggggggg"])
        print(r)
        expected = [["dgggggggggg"], ["ddddddddddg"]]
        assert sorted(r) == sorted(expected)

        r = sol.groupAnagrams([""])
        print(r)
        assert r == [[""]]

        r = sol.groupAnagrams(["a"])
        print(r)
        assert r == [["a"]]

    unitTest(Solution())
    unitTest(Solution1())
