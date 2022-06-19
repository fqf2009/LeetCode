# Given a string of English letters s, return the greatest 
# English letter which occurs as both a lowercase and uppercase 
# letter in s. The returned letter should be in uppercase. If no 
# such letter exists, return an empty string.

# An English letter b is greater than another letter a if b appears 
# after a in the English alphabet.
# Constraints:
#   1 <= s.length <= 1000
#   s consists of lowercase and uppercase English letters.


class Solution:
    def greatestLetter(self, s: str) -> str:
        c1 = set(ch for ch in s if 'A' <= ch <= 'Z' )
        c2 = set(ch.upper() for ch in s if 'a' <= ch <= 'z' )
        c3 = c1 & c2    #  c1.intersection(c2)
        return max(c3) if c3 else ""   


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.greatestLetter("lEeTcOdE")
        print(r)
        assert r == "E"

        r = sol.greatestLetter("AbCdEfGhIjK")
        print(r)
        assert r == ""

        r = sol.greatestLetter("arRAzFif")
        print(r)
        assert r == "R"

    unit_test(Solution())
