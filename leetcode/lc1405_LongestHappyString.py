# A string s is called happy if it satisfies the following conditions:
# - s only contains the letters 'a', 'b', and 'c'.
# - s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# - s contains at most a occurrences of the letter 'a'.
# - s contains at most b occurrences of the letter 'b'.
# - s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy
# string. If there are multiple longest happy strings, return any of
# them. If there is no such string, return the empty string "".
# A substring is a contiguous sequence of characters within a string.
# Constraints:
#   0 <= a, b, c <= 100
#   a + b + c > 0
import heapq


# Priority Queue + Greedy
# - note python's heapq is min queue.
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        hq = []
        if a > 0:
            heapq.heappush(hq, (-a, "a"))
        if b > 0:
            heapq.heappush(hq, (-b, "b"))
        if c > 0:
            heapq.heappush(hq, (-c, "c"))
        res = []
        while len(hq) > 1:
            cnt1, ch1 = heapq.heappop(hq)
            cnt2, ch2 = heapq.heappop(hq)
            cnt1, cnt2 = -cnt1, -cnt2

            cnt = min(2, cnt1)
            res.append(ch1 * cnt)
            cnt1 -= cnt

            cnt = 2 if (cnt2 >= 2 and cnt2 >= cnt1) else 1
            res.append(ch2 * cnt)
            cnt2 -= cnt

            if cnt1 > 0:
                heapq.heappush(hq, (-cnt1, ch1))
            if cnt2 > 0:
                heapq.heappush(hq, (-cnt2, ch2))

        if hq:
            cnt1, ch1 = heapq.heappop(hq)
            cnt1 = -cnt1
            res.append(ch1 * min(2, cnt1))

        return "".join(res)


# Sort + Greedy
class Solution1:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        arr = [[a, "a"], [b, "b"], [c, "c"]]
        res = []
        while True:
            arr.sort()  # assending, arr[2] has most available count
            i = 1 if len(res) >= 2 and res[-2] == res[-1] == arr[2][1] else 2
            if arr[i][0] == 0: break # no available char to use
            res.append(arr[i][1])
            arr[i][0] -= 1

        return ''.join(res)


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.longestDiverseString(a=1, b=1, c=7)
        print(r)
        assert r == "ccaccbcc" or r =="ccbccacc"

        r = sol.longestDiverseString(a=7, b=1, c=0)
        print(r)
        assert r == "aabaa"

    unit_test(Solution())
    unit_test(Solution1())
