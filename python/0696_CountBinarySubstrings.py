# Give a binary string s, return the number of non-empty substrings that have 
# the same number of 0's and 1's, and all the 0's and all the 1's in these 
# substrings are grouped consecutively.
# Substrings that occur multiple times are counted the number of times they occur.
# Example 1:
#   Input: s = "00110011"
#   Output: 6
#   Explanation:
#     There are 6 substrings that have equal number of 
#     consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
#     Notice that some of these substrings repeat and are counted the number
#     of times they occur.
#     Also, "00110011" is not a valid substring because all the 0's (and 1's) 
#     are not grouped together.
# Example 2:
#   Input: s = "10101"
#   Output: 4
#   Explanation: There are 4 substrings: "10", "01", "10", "01" that have 
#                equal number of consecutive 1's and 0's.
# Constraints:
#   1 <= s.length <= 10^5
#   s[i] is either '0' or '1'.


# T/S: O(n), O(1)
# Analysis:
# - scan through string, for any substring ending at pos i:
#   if s[i] = 0 and current 0's count <= previous 1's count, or
#   if s[i] = 1 and current 1's count <= previous 0's count, then
#   this substring meets the requirement
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ones = zeros = 0
        ch0 = ''
        res = 0
        for ch in s:
            if ch == '0':
                zeros = zeros + 1 if ch == ch0 else 1
                if zeros <= ones: res += 1
            else:
                ones = ones + 1 if ch == ch0 else 1
                if ones <= zeros: res += 1
            ch0 = ch

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.countBinarySubstrings('00110011')
        print(r)
        assert r == 6

        r = sol.countBinarySubstrings('10101')
        print(r)
        assert r == 4

    unitTest(Solution())
