# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.
# Given a string s that represents a DNA sequence, return all the 10-letter-long
# sequences (substrings) that occur more than once in a DNA molecule.
# You may return the answer in any order.
from typing import List
from collections import Counter, defaultdict

# Rabin-Karp: Constant-time slice using Rolling Hash:
# T/S:  O(N), O(N)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        def decode(ch) -> int:
            if ch == 'A':
                return 0
            elif ch == 'C':
                return 1
            elif ch == 'G':
                return 2
            else:
                return 3

        if len(s) <= 10:
            return []

        rh = 0
        for i in range(10):
            v = decode(s[i])
            rh = rh * 4 + v
        
        freq = defaultdict(list)
        freq[rh].append(0)

        for i in range(10, len(s)):
            rh = (rh - (4**9) * decode(s[i-10])) * 4 + decode(s[i])
            freq[rh].append(i - 10 + 1)

        return [s[y[0]: y[0] + 10] for _, y in freq.items() if len(y) > 1]


# Linear-time window slice (substring + hashset)
# Time complexity: O((N−L)L), where L is 10
# when L is small, this is actually more efficient than the extra effort to decode.
class Solution1:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        c = Counter([s[i: i+10] for i in range(len(s)-9)])
        return [x for x, y in c.items() if y > 1]


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
        print(r)
        assert sorted(r) == ["AAAAACCCCC", "CCCCCAAAAA"]

        r = sol.findRepeatedDnaSequences("AAAAAAAAAAAAA")
        print(r)
        assert r == ["AAAAAAAAAA"]

        r = sol.findRepeatedDnaSequences("AAAAAAAAAAA")
        print(r)
        assert r == ["AAAAAAAAAA"]

    unitTest(Solution())
    unitTest(Solution1())
