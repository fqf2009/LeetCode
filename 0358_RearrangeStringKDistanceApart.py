# Given a string s and an integer k, rearrange s such that the same
# characters are at least distance k from each other. If it is not
# possible to rearrange the string, return an empty string "".

# Constraints:
#   1 <= s.length <= 3 * 10^5
#   s consists of only lowercase English letters.
#   0 <= k <= s.length
from collections import Counter
import heapq

# !!! Wrong - e.g. s="aabbcc", k=2, it first get 'abab', left 'cc', then fail !!!
# PriorityQueue: O(n), initial scan O(n), PQ processing: O(26*log(26)) => O(1)
# - improvement - generate as much as string possible in one round of pup-up,
#   and reduce the PriorityQueue push times.
# - e.g.:
#   [(-100, 'a'), (-90, 'b'), (-80, 'c')] get poped up from queue,
#   do not just take 'abc', and then push [(-99, 'a'), ...] back,
#   instead, push back [(-20, 'a'), (-10, 'b')]
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0: return s

        pq = [(-y, x) for x, y in Counter(s).items()]   # max heap
        heapq.heapify(pq)
        res = []
        while pq:
            temp = []
            if len(pq) < k and -pq[0][0] > 1:
                return ""

            for _ in range(min(k, len(pq))):
                temp.append(heapq.heappop(pq))
            repeat = - temp[-1][0]
            res.append((''.join(x[1] for x in temp))*repeat)

            for cnt, ch in temp:
                if cnt + repeat != 0:
                    heapq.heappush(pq, (cnt + repeat, ch))

        return "".join(res)


# PriorityQueue: O(n*log(26)) => O(n)
class Solution1:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0: return s     # without this, leads to Time Limit Exceeded

        pq = [(-y, x) for x, y in Counter(s).items()]  # max heap
        heapq.heapify(pq)
        res = []
        while pq:
            temp = []
            if len(pq) < k and -pq[0][0] > 1:
                return ""
                
            for _ in range(min(k, len(pq))):
                cnt, ch = heapq.heappop(pq)
                res.append(ch)
                cnt += 1        # cnt is negative
                if cnt:
                    temp.append((cnt, ch))

            for x in temp:
                heapq.heappush(pq, x)

        return "".join(res)


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.rearrangeString(s="a", k=0)
        print(r)
        assert r == "a"

        r = sol.rearrangeString(s="aabbcc", k=3)
        print(r)
        assert r == "abcabc"

        r = sol.rearrangeString(s="aabbcc", k=2)
        print(r)
        assert r == "abcabc"

        r = sol.rearrangeString(s="aaabc", k=3)
        print(r)
        assert r == ""

        r = sol.rearrangeString(s="aaadbbcc", k=2)
        print(r)
        assert r == "abacabcd" or r == "ababcacd"

    # unitTest(Solution())  # Wrong
    unitTest(Solution1())
