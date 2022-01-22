# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.
# Given a string s that represents a DNA sequence, return all the 10-letter-long
# sequences (substrings) that occur more than once in a DNA molecule.
# You may return the answer in any order.
from typing import List
from collections import Counter


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        c = Counter([s[i: i+10] for i in range(len(s)-9)])
        return [x for x, y in c.items() if y > 1]


if __name__ == '__main__':
    sol = Solution()

    r = sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    print(r)
    assert(sorted(r) == ["AAAAACCCCC", "CCCCCAAAAA"])

    r = sol.findRepeatedDnaSequences("AAAAAAAAAAAAA")
    print(r)
    assert(r == ["AAAAAAAAAA"])

    r = sol.findRepeatedDnaSequences("AAAAAAAAAAA")
    print(r)
    assert(r == ["AAAAAAAAAA"])
