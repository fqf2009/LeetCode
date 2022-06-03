# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating
# characters in chars:
#   If the group's length is 1, append the character to s.
#   Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be
# stored in the input character array chars. Note that group lengths that are
# 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.
# You must write an algorithm that uses only constant extra space.
# Constraints:
# 1 <= chars.length <= 2000
# chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
from itertools import chain
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        pos, cnt = 0, 1
        for ch1, ch2 in zip(chars[0:], chain(chars[1:], ["**"])):
            if ch1 == ch2:
                cnt += 1
            else:
                chars[pos] = ch1
                pos += 1
                if cnt > 1:
                    for digit in str(cnt):
                        chars[pos] = digit
                        pos += 1
                cnt = 1

        return pos


if __name__ == "__main__":

    def unit_test(sol):
        input = ["a", "a", "b", "b", "c", "c", "c"]
        r = sol.compress(input)
        print(r, input)
        assert r == 6
        assert input[:r] == ["a", "2", "b", "2", "c", "3"]

        input = ["a"]
        r = sol.compress(input)
        print(r, input)
        assert r == 1
        assert input[:r] == ["a"]

        input = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        r = sol.compress(input)
        print(r, input)
        assert r == 4
        assert input[:r] == ["a", "b", "1", "2"]

    unit_test(Solution())
