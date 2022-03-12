# Given a string s consisting of some words separated by some number of 
# spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# Constraints:
#   1 <= s.length <= 10^4
#   s consists of only English letters and spaces ' '.
#   There will be at least one word in s.

# Just count it
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for ch in reversed(s):
            if ch != ' ':
                count += 1
            elif count > 0:
                break

        return count

    
# Two pointers
class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        start = stop = -1
        for i, ch in enumerate(reversed(s)):
            if ch == ' ':
                if start == -1:
                    continue
                else:
                    break
            elif start == -1:
                start = stop = i
            else:
                stop = i
        
        return stop - start + 1


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.lengthOfLastWord('Hello World')
        print(r)
        assert r == 5

        r = sol.lengthOfLastWord("   fly me   to   the moon  ")
        print(r)
        assert r == 4

        r = sol.lengthOfLastWord('luffy is still joyboy')
        print(r)
        assert r == 6

    unitTest(Solution())
    unitTest(Solution1())
