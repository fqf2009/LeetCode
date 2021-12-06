from typing import List
from operator import itemgetter

# You are given an array of n pairs, where pairs[i] = [lefti, righti] and lefti < righti.
# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
# Return the length longest chain which can be formed.
# You do not need to use up all the given intervals. You can select pairs in any order.

# Greedy: O(n), plus O(n*log(n) from sort
# Sorted on end time
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        curEnd = float('-inf')
        res = 0
        for start, end in sorted(pairs, key=itemgetter(1)):
            if curEnd < start:
                curEnd = end
                res += 1
        
        return res


# DP (Dynamic Programming): O(n^2), plus O(n*log(n) from sort
# Sorted on start time
class Solution1:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp = [0] * len(pairs)
        for i in range(len(pairs)):
            dp[i] = 1
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[j] + 1, dp[i])
        
        return max(dp)


if __name__ == '__main__':
    sol = Solution()

    pairs = [[1,2],[2,3],[3,4]]
    r = sol.findLongestChain(pairs)
    print(r)
    assert(r == 2)
    
    pairs = [[1,2],[7,8],[4,5]]
    r = sol.findLongestChain(pairs)
    print(r)
    assert(r == 3)
    