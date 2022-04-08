# Given two strings s1 and s2, return true if s2 contains a 
# permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the 
# substring of s2.

# Constraints:
#   1 <= s1.length, s2.length <= 104
#   s1 and s2 consist of lowercase English letters.


# Sliding window - T/S: O(n), O(n)
# simplify a little
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        cmp = {}
        for i in range(n1):
            cmp.setdefault(s1[i], [0, 0])[0] += 1
        diff = len(cmp)

        for i in range(n2):
            if i >= n1:
                v = cmp[s2[i-n1]]
                if v[0] == v[1]:
                    diff += 1
                elif v[0] == v[1] - 1:
                    diff -= 1
                v[1] -= 1

            v = cmp.setdefault(s2[i], [0, 0])
            if v[0] == v[1]:
                diff += 1
            elif v[0] == v[1] + 1:
                diff -= 1
            v[1] += 1

            if diff == 0:
                return True

        return False


# Sliding window - T/S: O(n), O(n)
# - assume the length of two strings are n1, n2
# - the target is find substring in s2, with length n1, having
#   the same letters frequency count as s1.
# - use a sliding window, each time remove/add a letter, and
#   adjust the frequency count and diff count dynamically.
class Solution1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        cmp = {}
        for i in range(n1):
            cmp.setdefault(s1[i], [0, 0])[0] += 1
            cmp.setdefault(s2[i], [0, 0])[1] += 1

        diff = 0
        for v in cmp.values():
            if v[0] != v[1]:
                diff += 1 

        if diff == 0:
            return True

        for i in range(n1, n2):
            v = cmp[s2[i-n1]]
            if v[0] == v[1]:
                diff += 1
            elif v[0] == v[1] - 1:
                diff -= 1
            v[1] -= 1

            v = cmp.setdefault(s2[i], [0, 0])
            if v[0] == v[1]:
                diff += 1
            elif v[0] == v[1] + 1:
                diff -= 1
            v[1] += 1

            if diff == 0:
                return True

        return False


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.checkInclusion(s1 = "abc", s2 = "bbbca")
        print(r)
        assert r == True

        r = sol.checkInclusion(s1 = "ab", s2 = "eidbaooo")
        print(r)
        assert r == True

        r = sol.checkInclusion(s1 = "ab", s2 = "eidboaoo")
        print(r)
        assert r == False

    unitTest(Solution())
    unitTest(Solution1())
