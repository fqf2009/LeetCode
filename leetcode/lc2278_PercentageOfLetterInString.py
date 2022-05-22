# Given a string s and a character letter, return the percentage of
# characters in s that equal letter rounded down to the nearest whole percent.
# Constraints:
#   1 <= s.length <= 100
#   s consists of lowercase English letters.
#   letter is a lowercase English letter.


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return s.count(letter) * 100 // len(s)


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.percentageLetter("foobar", letter="o")
        print(r)
        assert r == 33

        r = sol.percentageLetter(s="jjjj", letter="k")
        print(r)
        assert r == 0

        r = sol.percentageLetter("a", "a")
        print(r)
        assert r == 100

    unit_test(Solution())
