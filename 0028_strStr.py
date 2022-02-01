# Implement strStr().

# Return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.

# Clarification:
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an
# empty string. This is consistent to C's strstr() and Java's indexOf().

# Constraints:
#   0 <= haystack.length, needle.length <= 5 * 104
#   haystack and needle consist of only lower-case English characters.


# KMP is difficult to understand, difficult to code
# Rolling hash is much easier to understand and code: O(n)
# https://en.wikipedia.org/wiki/Rolling_hash
#  - suppose len(needle) = k
#  - hash = ( c1*p^(k-1) + c2*p^(k-2) + ... + ck*p^0 ) % m, where k, m are constant
#  - find the matching hash, and then compare again in case of hash collision
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = len(needle)
        if k == 0:
            return 0
        if k > len(haystack):
            return -1

        pk, p, m, h1, h2 = 1, 31, 53, 0, 0
        for i in reversed(range(k)):
            pk = pk % m
            h1 = (h1 + (ord(haystack[i]) - ord('a') + 1) * pk) % m
            h2 = (h2 + (ord(needle[i]) - ord('a') + 1) * pk) % m
            pk *= p

        pk //= p
        if h1 == h2 and haystack[0:k] == needle:
            return 0

        for i in range(len(haystack) - k):
            h1 = ((h1 + m - (ord(haystack[i]) - ord('a') + 1)*pk % m) * p
                  + (ord(haystack[i+k])-ord('a')+1)) % m
            if h1 == h2 and haystack[i+1:i+k+1] == needle:
                return i+1

        return -1


# KMP algorithm: O(n+m)
# - https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
# - https://www.youtube.com/watch?v=JoF0Z7nVSrA
# LPS (Longest Prefix Suffix)
class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        lps = [0] * len(needle)
        prevLps, i = 0, 1
        while i < len(needle):
            if needle[prevLps] == needle[i]:
                lps[i] = prevLps + 1
                i += 1
                prevLps += 1
            elif prevLps == 0:
                lps[i] = 0
                i += 1
            else:
                prevLps = lps[prevLps - 1]

        i = 0  # pointer to haystack
        j = 0  # pointer to needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            elif j == 0:
                i += 1
            else:
                j = lps[j-1]

        return -1


# Time exceeded.
# Worse case: O(n*m), where n = len(haystack), m = len(needle)
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:    # required, when both haystack and needle are empty
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
            else:
                return i

        return -1


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.strStr("hello", "")
        print(r)
        assert (r == 0)

        r = sol.strStr("", "")
        print(r)
        assert (r == 0)

        r = sol.strStr("a", "a")
        print(r)
        assert (r == 0)

        r = sol.strStr("hello", "ll")
        print(r)
        assert (r == 2)

        r = sol.strStr("aaaaa", "bba")
        print(r)
        assert(r == -1)

        r = sol.strStr("aaabb", "bba")
        print(r)
        assert(r == -1)

        r = sol.strStr("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaa",
                       "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaa")
        print(r)
        assert(r == 2)

        r = sol.strStr("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaa",
                       "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaa")
        print(r)
        assert(r == -1)

    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
