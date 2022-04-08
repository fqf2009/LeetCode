# You have n computers. You are given the integer n and a 0-indexed integer
# array batteries where the ith battery can run a computer for batteries[i]
# minutes. You are interested in running all n computers simultaneously
# using the given batteries.

# Initially, you can insert at most one battery into each computer. After
# that and at any integer time moment, you can remove a battery from a
# computer and insert another battery any number of times. The inserted
# battery can be a totally new battery or a battery from another computer.
# You may assume that the removing and inserting processes take no time.

# Note that the batteries cannot be recharged.

# Return the maximum number of minutes you can run all the n computers simultaneously.

from typing import List


# Sort batteries first, then plug them to computers starting from highest capacity to lowest, 
# the remaining are backup batteries. Anytime an in-use battery has lower capacity than backup 
# batteries, it will be swapped out as backup.
# So we can think of total amount of backup capacity as water, to fill up the in-use batteries
# Time complexity: O(n*log(n)), where sorting is O(n*log(n)), fillup is O(n)
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        extraCapacity = sum(batteries[0: len(batteries) - n])
        computers = batteries[len(batteries) - n:]
        res = computers[0]
        for i in range(len(computers)):
            if i == len(computers) - 1:
                fillUp = extraCapacity // (i + 1)
            else:
                fillUp = min(extraCapacity // (i + 1), computers[i + 1] - res)
            res += fillUp
            extraCapacity -= fillUp * (i + 1)
            if extraCapacity < (i + 2):
                return res

        return res


if __name__ == '__main__':
    def unitTest(sol):
        r = sol.maxRunTime(n=2, batteries=[3, 3, 3])
        print(r)
        assert (r == 4)

        r = sol.maxRunTime(n=2, batteries=[1, 1, 1, 1])
        print(r)
        assert (r == 2)

        r = sol.maxRunTime(n=3, batteries=[1, 1, 1, 1, 55, 99])
        print(r)
        assert (r == 4)

    unitTest(Solution())
