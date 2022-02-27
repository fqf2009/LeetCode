# You are given two strings s and t. In one step, you can 
# append any character to either s or t.
# Return the minimum number of steps to make s and t anagrams of each other.
# An anagram of a string is a string that contains the same characters 
# with a different (or the same) ordering.
# Constraints:
#   1 <= s.length, t.length <= 2 * 10^5
#   s and t consist of lowercase English letters.
from collections import Counter


# Counter: T/S: O(m+n), O(m+n), where m = len(s), n = len(t)
# - Note in Python: sum([]) = 0
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq1 = Counter(s)
        freq2 = Counter(t)
        freq3 = (freq1 - freq2) + (freq2 - freq1)
        return sum(freq3.values())  # freq3.total()  # Python 3.10


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.minSteps(s = "leetcode", t = "coats")
        print(r)
        assert r == 7

        r = sol.minSteps(s = "night", t = "thing")
        print(r)
        assert r == 0
        
    unitTest(Solution())
