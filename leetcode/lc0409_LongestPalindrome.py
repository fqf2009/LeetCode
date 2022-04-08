# Given a string s which consists of lowercase or uppercase letters, 
# return the length of the longest palindrome that can be built with 
# those letters.
# Letters are case sensitive, for example, "Aa" is not considered 
# a palindrome here.

from typing import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        even, odd = 0, 0
        for _, x in freq.items():
            if x % 2 == 0:
                even += x
            else:
                even += x - 1
                odd = 1
        return even + odd


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.longestPalindrome(s = "ccc")
        print(r)
        assert r == 3

        r = sol.longestPalindrome(s = "abccccdd")
        print(r)
        assert r == 7

        r = sol.longestPalindrome(s = "a")
        print(r)
        assert r == 1

        r = sol.longestPalindrome(s = "bb")
        print(r)
        assert r == 2

        s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
        r = sol.longestPalindrome(s)
        print(r)
        assert r == 983

    unitTest(Solution())
