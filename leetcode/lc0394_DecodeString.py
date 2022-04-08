# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string 
# inside the square brackets is being repeated exactly k times. Note 
# that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no 
# extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain 
# any digits and that digits are only for those repeat numbers, k. 
# For example, there will not be input like 3a or 2[4].

# Constraints:
#   1 <= s.length <= 30
#   s consists of lowercase English letters, digits, and square brackets '[]'.
#   s is guaranteed to be a valid input.
#   All the integers in s are in the range [1, 300].
import re

# Stack, Regular Expression
# - put separator into capturing group '()', so that they  will be in the list:
#   re.split(r'(\[|\]|[0-9]+)', "3[ab20[cd]]") will return:
#   ['', '3', '', '[', 'ab', '20', '', '[', 'cd', ']', '', ']', '']
# - note the redundant '', they are inserted between two separators.
class Solution:
    def decodeString(self, s: str) -> str:
        A = re.split(r'(\[|\]|[0-9]+)', s)
        stk = []
        for x in A:
            if x == '[' or x == '':
                continue
            if x == ']':
                for j in reversed(range(len(stk))):
                    if isinstance(stk[j], int):
                        s1 = ''.join(stk[j+1:]) * stk[j]
                        del stk[j:]
                        stk.append(s1)
                        break
            elif x[0] >= '0' and x[0] <= '9':
                stk.append(int(x))
            else:
                stk.append(x)

        return ''.join(stk)


# Stack
class Solution1:
    def decodeString(self, s: str) -> str:
        stk = []
        i = 0
        while i < len(s):
            if s[i] == ']':
                for j in reversed(range(len(stk))):
                    if isinstance(stk[j], int):
                        s1 = ''.join(stk[j+1:]) * stk[j]
                        del stk[j:]
                        stk.append(s1)
                        break
            if s[i] >= '0' and s[i] <= '9':
                j = i
                while s[i+1] >= '0' and s[i+1] <= '9':
                    i += 1
                stk.append(int(s[j:i+1]))
            if s[i] >= 'a' and s[i] <= 'z':
                j = i
                while i+1 < len(s) and s[i+1] >= 'a' and s[i+1] <= 'z':
                    i += 1
                stk.append(s[j:i+1])
            i += 1
        
        return ''.join(stk)


if __name__ == '__main__':
    def unit_test(sol):
        r = sol.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")
        print(r)
        assert r == "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
        
        r = sol.decodeString("3[a]2[bc]")
        print(r)
        assert r == "aaabcbc"
    
        r = sol.decodeString("3[a2[c]]")
        print(r)
        assert r == "accaccacc"
    
        r = sol.decodeString("2[abc]3[cd]ef")
        print(r)
        assert r == "abcabccdcdcdef"
    
    unit_test(Solution())
    unit_test(Solution1())
