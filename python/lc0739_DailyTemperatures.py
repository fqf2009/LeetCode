from typing import List

# Given an array of integers temperatures represents the daily temperatures, return
# an array answer such that answer[i] is the number of days you have to wait after
# the ith day to get a warmer temperature. If there is no future day for which this
# is possible, keep answer[i] == 0 instead.

# use stack to track each day no. when temperatures keep getting down. If ever
# temperature goes up than the day's on top of stack, pop out all those with 
# lower temperature in stack, and calculate the days in between.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tStack = []
        waitDays = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(tStack) > 0 and temperatures[tStack[-1]] < temperatures[i]:
                j = tStack.pop()
                waitDays[j] = i - j
            tStack.append(i)

        return waitDays


if __name__ == '__main__':
    sol = Solution()

    temperatures = [73,74,75,71,69,72,76,73]
    r = sol.dailyTemperatures(temperatures)
    print(r)
    assert(r == [1,1,4,2,1,1,0,0])

    temperatures = [30,40,50,60]
    r = sol.dailyTemperatures(temperatures)
    print(r)
    assert(r == [1,1,1,0])

    temperatures = [30,60,90]
    r = sol.dailyTemperatures(temperatures)
    print(r)
    assert(r == [1,1,0])
