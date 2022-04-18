# Given a positive integer n, find the smallest integer which has exactly 
# the same digits existing in the integer n and is greater in value than n. 
# If no such positive integer exists, return -1.

# Note that the returned integer should fit in 32-bit integer, if there is 
# a valid answer but it does not fit in 32-bit integer, return -1.
# Constraints:
#   1 <= n <= 2^31 - 1


# Permutation: T/S: O(n), O(n)
# Similar Problem: lc0031_nextPermutation.py
# Analysis:
# - scan from right to left, continue if monotonic increasing,
#   until find one decreasing, then from from right to left search
#   again for item bigger than this, and swap them, finally reverse 
#   all digits at the rear part
# - e.g.: 263153221
#   - first scan from right to left: 1, 2, 2, 3, 5, all increasing;
#   - then encounter 1, decreasing, scan again find 2, bigger than 1;
#   - swap 1 and 2, we get: 263 2 532 1 1
#   - finally, we reverse the 53211 to 11235, and get: 263 2 11235
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        pivot = 0
        for i in reversed(range(len(s)-1)):
            if s[i] < s[i+1]:
                pivot = i + 1
                for j in reversed(range(pivot, len(s))):
                    if s[j] > s[i]:
                        s[i], s[j] = s[j], s[i]
                        break
                break

        res = int(''.join(s[:pivot] + (s[pivot:][::-1])))
        return res if res > n and res <= 2**31 - 1 else -1


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.nextGreaterElement(12)
        print(r)
        assert r == 21

        r = sol.nextGreaterElement(263153221)
        print(r)
        assert r == 263211235

        r = sol.nextGreaterElement(21)
        print(r)
        assert r == -1

    unit_test(Solution())
