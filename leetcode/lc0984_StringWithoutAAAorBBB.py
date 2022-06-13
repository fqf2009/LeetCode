# Given two integers a and b, return any string s such that:
# s has length a + b and contains exactly a 'a' letters,
# and exactly b 'b' letters,
# The substring 'aaa' does not occur in s, and
# The substring 'bbb' does not occur in s.
# Constraints:
#   0 <= a, b <= 100
#   It is guaranteed such an s exists for the given a and b.


# Greedy
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        n1, n2, ch1, ch2 = a, b, 'a', 'b'
        if a < b:
            n1, n2, ch1, ch2 = b, a, 'b', 'a'
        while n1 > 0:
            res.append(ch1)
            n1 -= 1
            if n1 > n2:
                res.append(ch1)
                n1 -= 1
            if n2 > 0:
                res.append(ch2)
                n2 -= 1

        return "".join(res)


if __name__ == "__main__":

    def unitTest(sol):
        r = sol.strWithout3a3b(a=1, b=2)
        print(r)
        assert r in ("abb", "abb", "bab", "bba")

        r = sol.strWithout3a3b(a=1, b=3)
        print(r)
        assert r in ("bbab", "babb")

        r = sol.strWithout3a3b(a=1, b=2)
        print(r)
        assert r in ("abb", "abb", "bab", "bba")

        r = sol.strWithout3a3b(a=4, b=1)
        print(r)
        assert r == "aabaa"

    unitTest(Solution())
