# There are n persons on a social media website. You are given an integer 
# array ages where ages[i] is the age of the ith person.
# A Person x will not send a friend request to a person y (x != y) if any 
# of the following conditions is true:
#  - age[y] <= 0.5 * age[x] + 7
#  - age[y] > age[x]
#  - age[y] > 100 && age[x] < 100
# Otherwise, x will send a friend request to y.
# Note that if x sends a request to y, y will not necessarily send a 
# request to x. Also, a person will not send a friend request to themself.
# Return the total number of friend requests made.
# Constraints:
#   n == ages.length
#   1 <= n <= 2 * 10^4
#   1 <= ages[i] <= 120
from typing import List


# Two pointers: O(n)
# Analysis:
# - rules for no suggestion
#   (1) age[y] <= 0.5 * age[x] + 7  =>  when x <= 14, 0.5*x+7 <= 14,
#       based on (1) & (2), no request suggestion for x <= 14
#   (2) age[x] >= age[y], sort ages array, and loop over
#   (3) already enforced by (2), no need to check
# - if there are people with the same age:
#   - accumulate the number of same age people
#   - make requests to the current people with same people
#   - otherwise reset the number to 1
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        j = 0
        res = 0
        same_age = 1
        for i in range(1, len(ages)):
            if ages[i] <= 14: continue
            while j < i and ages[j] <= 0.5 * ages[i] + 7:
                j += 1
            res += i - j
            if ages[i-1] == ages[i]:
                res += same_age
                same_age += 1
            else:
                same_age = 1

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.numFriendRequests([14,14,14,15,15,15])
        print(r)
        assert r == 6

        r = sol.numFriendRequests([16,16])
        print(r)
        assert r == 2

        r = sol.numFriendRequests([16,17,18])
        print(r)
        assert r == 2

        r = sol.numFriendRequests([20,30,100,110,120])
        print(r)
        assert r == 3

    unitTest(Solution())
