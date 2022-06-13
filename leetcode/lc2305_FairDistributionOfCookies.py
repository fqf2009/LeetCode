# You are given an integer array cookies, where cookies[i] denotes
# the number of cookies in the ith bag. You are also given an integer
# k that denotes the number of children to distribute all the bags
# of cookies to. All the cookies in the same bag must go to the same
# child and cannot be split up.
# The unfairness of a distribution is defined as the maximum total
# cookies obtained by a single child in the distribution.
# Return the minimum unfairness of all distributions.
# Constraints:
#   2 <= cookies.length <= 8
#   1 <= cookies[i] <= 105
#   2 <= k <= cookies.length
from typing import List
import heapq


# Wrong!
# - However, even this solution can not leads to correct result,
#   it still lead to sub-optimal result.
# - for big data set, maybe this result can be used to help prune
#   pathes in backtracking solution.
class Solution1:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)
        bin = [0] * k
        heapq.heapify(bin)
        for i, c in enumerate(cookies):
            c1 = heapq.heappop(bin)
            heapq.heappush(bin, c1 + c)

        return max(bin)


# Backtrack
# - 3 times faster after bringing distributeCookies1 in.
class Solution:
    def distributeCookies1(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)
        bin = [0] * k
        heapq.heapify(bin)
        for c in cookies:
            c1 = heapq.heappop(bin)
            heapq.heappush(bin, c1 + c)

        return max(bin)

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        res = self.distributeCookies1(cookies, k)
        bin = [0] * k

        def backtrack(i):
            nonlocal res
            if i == n:
                res = max(bin)  # res = min(res, max(bin))
                return
            v = cookies[i]
            for j in range(k):
                if bin[j] + v >= res:  # skip sub-optimal solutions
                    continue
                bin[j] += v
                backtrack(i + 1)
                bin[j] -= v

        backtrack(0)
        return res


if __name__ == "__main__":

    def unit_test(sol):
        r = sol.distributeCookies([8, 15, 10, 20, 8], k=2)
        print(r)
        assert r == 31

        r = sol.distributeCookies([6, 1, 3, 2, 2, 4, 1, 2], k=3)
        print(r)
        assert r == 7

    unit_test(Solution())
