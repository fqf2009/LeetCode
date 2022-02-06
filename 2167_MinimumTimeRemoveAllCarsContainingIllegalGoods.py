# You are given a 0-indexed binary string s which represents a sequence of
# train cars. s[i] = '0' denotes that the ith car does not contain illegal
# goods and s[i] = '1' denotes that the ith car does contain illegal goods.

# As the train conductor, you would like to get rid of all the cars containing 
# illegal goods. You can do any of the following three operations any number of times:

#  - Remove a train car from the left end (i.e., remove s[0]) which takes 1 unit of time.
#  - Remove a train car from the right end (i.e., remove s[s.length - 1]) which takes 1 
#    unit of time.
#  - Remove a train car from anywhere in the sequence which takes 2 units of time.

# Return the minimum time to remove all the cars containing illegal goods.
# Note that an empty sequence of cars is considered to have no cars containing 
# illegal goods.


# Dynamic Porgraming (soft of): time O(n), Space O(n)
# - from left side, remove car using two methods:
#   a. remove every car, each take 1 unit of time;
#   b. remove only the illegal car, each take 2 unit of time.
# - assume dpla[i] and dplb[i] are the accumulated time cost for each  method at pos i
# - Note method a can switch to method any time, but not vice versa. so,
#   when dplb[i] is less than dpla[i], it will just store dpla[i]'s value
# - Do the same thing from right side, and calculate dpra[i] and dprb[i]
# - One more iteration to calculate the:
#       minTimeCost = min(min(dpla[i], dplb[i]) + min(dpra[n-i], dprb[n-i]))
#       where i is the split pos, i use 1-based index
# - To simplify a bit, no need to store dpla and dpra, they are just list(range(n+1))
class Solution:
    def minimumTime(self, s: str) -> int:
        def timeCost(s:str, dp):
            for i in range(1, len(s) + 1):
                if s[i-1] == '0':
                    dp[i] = min(dp[i-1], i)
                else:
                    dp[i] = min(dp[i-1] + 2, i)

        n = len(s)
        dpLeft  = [0] * (n + 1)
        dpRight = [0] * (n + 1)
        timeCost(s, dpLeft)
        timeCost(s[::-1], dpRight)

        # minTimeCost = n
        # for i in range(n + 1):
        #     minTimeCost = min(minTimeCost, dpLeft[i] + dpRight[n-i])
        # return minTimeCost

        # Pythonic way?
        return min([x + y for x, y in zip(dpLeft, dpRight[::-1])])

if __name__ == '__main__':
    def unit_test(sol):
        r = sol.minimumTime(s = "1100101")
        print(r)
        assert r == 5

        r = sol.minimumTime(s = "0010")
        print(r)
        assert r == 2

    unit_test(Solution())        
