# Implement strStr(). Return the index of the first occurrence of needle in 
# haystack, or -1 if needle is not part of haystack.
# Clarification:
#  - What should we return when needle is an empty string? This is a great
#    question to ask during an interview.
#  - For the purpose of this problem, we will return 0 when needle is an
#    empty string. This is consistent to C's strstr() and Java's indexOf().
# Constraints:
#   0 <= haystack.length, needle.length <= 5 * 10^4
#   haystack and needle consist of only lower-case English characters.


# Rolling hash is somewhat easier to understand: O(n)
#  - hash = ( c1*p^(k) + c2*p^(k-1) + ... + ck*p^1 ) % m, where k, m are constant
#  - find the matching hash, and then compare again in case of hash collision
class Solution0:
    def strStr(self, haystack: str, needle: str) -> int:
        k = len(needle)
        if k == 0:
            return 0
        if k > len(haystack):
            return -1

        pk, p, m, h1, h2 = 1, 31, 53, 0, 0
        for i in reversed(range(k)):
            pk = pk * p % m
            h1 = (h1 + (ord(haystack[i]) - ord('a') + 1) * pk) % m
            h2 = (h2 + (ord(needle[i]) - ord('a') + 1) * pk) % m

        if h1 == h2 and haystack[0:k] == needle:
            return 0

        for i in range(len(haystack) - k):
            h1 = (h1 + (ord(haystack[i+k])-ord('a')+1) +
                    m - (ord(haystack[i]) - ord('a') + 1)*pk % m) * p % m
            if h1 == h2 and haystack[i+1:i+k+1] == needle:
                return i+1

        return -1


# Rolling hash is somewhat easier to understand: O(n)
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


# KMP (Knuth–Morris–Pratt) algorithm: O(n+m)
# - https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
# - LPS (Longest common Prefix Suffix)
#   lps[i]: at position i, longest length of common prefix and suffix in string
# - e.g.: for the string "ababcababa":
#   i     lps[i]        substring           longest-common-prefix-suffix
#   0     0             a                   <empty>
#   1     0             ab                  <empty>
#   2     1             aba                 a
#   3     2             abab                ab
#   4     0             ababc               <empty>
#   5     1             ababca              a
#   6     2             ababcab             ab
#   7     3             ababcaba            aba
#   8     4             ababcabab           abab
#   9     3             ababcababa          aba
# - to calculate lps[i], start with the previousLPS (not the lps[i-1])
class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0

        lps = [0] * m
        for i in range(1, m):
            t = lps[i-1]
            while (t > 0 and needle[i] != needle[t]):
                t = lps[t-1]
            if needle[i] == needle[t]:
                t += 1
            lps[i] = t

        i = 0  # point to haystack
        j = 0  # point to needle
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return i - j
            elif j == 0:
                i += 1
            else:
                j = lps[j-1]

        return -1


# Brute force. Time exceeded.
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

        r = sol.strStr("mississippi", "sipp")
        print(r)
        assert (r == 6)

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

    unitTest(Solution0())
    unitTest(Solution())
    unitTest(Solution1())
    unitTest(Solution2())
