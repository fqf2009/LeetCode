# A string can be abbreviated by replacing any number of non-adjacent, non-empty 
# substrings with their lengths. The lengths should not have leading zeros.
# For example, a string such as "substitution" could be abbreviated as (but not
# limited to):
#   "s10n" ("s ubstitutio n")
#   "sub4u4" ("sub stit u tion")
#   "12" ("substitution")
#   "su3i1u2on" ("su bst i t u ti on")
#   "substitution" (no substrings replaced)
# The following are not valid abbreviations:
#   "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
#   "s010n" (has leading zeros)
#   "s0ubstitution" (replaces an empty substring)
# Given a string word and an abbreviation abbr, return whether the string matches 
# the given abbreviation.
# A substring is a contiguous non-empty sequence of characters within a string.
# Constraints:
#   1 <= word.length <= 20
#   word consists of only lowercase English letters.
#   1 <= abbr.length <= 10
#   abbr consists of lowercase English letters and digits.
#   All the integers in abbr will fit in a 32-bit integer.


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbrLen = 0
        wordIdx = 0
        for ch in abbr:
            if '0' <= ch <= '9':
                if ch == '0' and abbrLen == 0:
                    return False
                abbrLen = abbrLen * 10 + ord(ch) - ord('0')
            else:
                wordIdx += abbrLen
                abbrLen = 0
                if wordIdx >= len(word) or word[wordIdx] != ch:
                    return False
                wordIdx += 1
        
        wordIdx += abbrLen
        return wordIdx == len(word)


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.validWordAbbreviation("substitution", "s10n")
        print(r)
        assert r == True

        r = sol.validWordAbbreviation("substitution", "sub4u4")
        print(r)
        assert r == True

        r = sol.validWordAbbreviation("substitution", "12")
        print(r)
        assert r == True

        r = sol.validWordAbbreviation("substitution", "su3i1u2on")
        print(r)
        assert r == True

        r = sol.validWordAbbreviation("substitution", "substitution")
        print(r)
        assert r == True

        r = sol.validWordAbbreviation("substitution", "s55n")
        print(r)
        assert r == False

        r = sol.validWordAbbreviation("substitution", "s010n")
        print(r)
        assert r == False

        r = sol.validWordAbbreviation("substitution", "s0ubstitution")
        print(r)
        assert r == False

        r = sol.validWordAbbreviation("internationalization", "i12iz4n")
        print(r)
        assert r == True

        r = sol.validWordAbbreviation( "apple", "a2e")
        print(r)
        assert r == False

        r = sol.validWordAbbreviation( "apple", "a2l1")
        print(r)
        assert r == True

        r = sol.validWordAbbreviation( "apple", "5")
        print(r)
        assert r == True

        r = sol.validWordAbbreviation( "apple", "3")
        print(r)
        assert r == False

        r = sol.validWordAbbreviation( "apple", "3le")
        print(r)
        assert r == True

    unitTest(Solution())
