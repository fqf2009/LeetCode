# You are given two 0-indexed strings s and target. You can take some 
# letters from s and rearrange them to form new strings.
# Return the maximum number of copies of target that can be formed by 
# taking letters from s and rearranging them.
# Constraints:
#   1 <= s.length <= 100
#   1 <= target.length <= 10
#   s and target consist of lowercase English letters.
from typing import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        c1, c2 = Counter(s), Counter(target)
        return min(c1[ch] // freq for ch, freq in c2.items())


if __name__ == '__main__':
    def unit_rearrangeCharacters(sol):
        r = sol.rearrangeCharacters("ilovecodingonleetcode", target = "code")
        print(r)
        assert r == 2

        r = sol.rearrangeCharacters("abcba", target = "abc")
        print(r)
        assert r == 1

        r = sol.rearrangeCharacters("abbaccaddaeea", target = "aaaaa")
        print(r)
        assert r == 1

    unit_rearrangeCharacters(Solution())
