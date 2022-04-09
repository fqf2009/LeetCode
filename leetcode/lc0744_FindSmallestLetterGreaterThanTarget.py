# Given a characters array letters that is sorted in non-decreasing 
# order and a character target, return the smallest character in the 
# array that is larger than target.
# Note that the letters wrap around.
# For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
# Constraints:
#   2 <= letters.length <= 10^4
#   letters[i] is a lowercase English letter.
#   letters is sorted in non-decreasing order.
#   letters contains at least two different characters.
#   target is a lowercase English letter.
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target = chr((ord(target) - ord('a') + 1) % 26 + ord('a'))
        lo, hi = 0, len(letters)
        while lo < hi:
            mid = (lo+hi) // 2
            if letters[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        
        if lo == len(letters):
            lo = 0
        return letters[lo]


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,),])    # must be tuple!!!
    class TestSolution(TestCase):
        @parameterized.expand([
            (["c","f","j"], 'a', 'c'),
            (["c","f","j"], 'e', 'f'),
            (["c","f","j"], 'f', 'j'),
            (["c","f","j"], 'j', 'c'),
            (["c","f","j"], 'z', 'c'),
        ])
        def test_nextGreatestLetter(self, letters, target, expected):
            sol = self.solution()       # type:ignore
            r = sol.nextGreatestLetter(letters, target)
            self.assertEqual(r, expected)

    main()
