# Given an array of strings words and an integer k, return the k 
# most frequent strings.
# Return the answer sorted by the frequency from highest to lowest.
# Sort the words with the same frequency by their lexicographical order.
# Constraints:
#   1 <= words.length <= 500
#   1 <= words[i] <= 10
#   words[i] consists of lowercase English letters.
#   k is in the range [1, The number of unique words[i]]
import heapq
from typing import Counter, List


# Priority Queue: T/S: O(n + m*log(k)), O(k), where m = unique_items(words)
# - Faster, only need to maintain k items.
class Solution:
    class InvertStr:
        def __init__(self, s: str):
            self.s = s

        def __lt__(self, other):
            return self.s > other.s

        def __eq__(self, other):
            return self.s == other.s

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        def invert(s: str):
            # - both do not work for: "a","aa","aaa"
            # - because length is invariant!!!
            # return ''.join(chr(ord('z') - ord(c) + ord('a')) for c in s)
            return tuple(-ord(c) for c in s)

        counts = Counter(words)
        hq = []
        for s, freq in counts.items():
            if not hq or len(hq) < k:
                heapq.heappush(hq, [freq, self.InvertStr(s)])
            elif hq[0][0] < freq or (hq[0][0] == freq and hq[0][1] < self.InvertStr(s)):
                heapq.heapreplace(hq, [freq, self.InvertStr(s)])

        res = []
        while hq:
            res.append(heapq.heappop(hq)[1].s)

        return res[::-1]


# Sort: T/S: O(n + m*log(m)), O(m)
class Solution1:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [s for _, s in sorted((-freq, s) for s, freq in Counter(words).items())][:k]


if __name__ == "__main__":
    from unittest import TestCase, main
    from parameterized import parameterized, parameterized_class

    @parameterized_class(('solution',), [(Solution,), (Solution1,),])    # must be tuple!!!
    class TestSolution(TestCase):
        @parameterized.expand([
            (["a","aa","aaa"], 1, ["a"]),
            (["i","love","leetcode","i","love","coding"], 2, ["i","love"]),
            (["the","day","is","sunny","the","the","the","sunny","is","is"], 4, ["the","is","sunny","day"]),
        ])
        def test_topKFrequent(self, words, k, expected):
            sol = self.solution()       # type:ignore
            r = sol.topKFrequent(words, k)
            self.assertEqual(r, expected)

    main()
