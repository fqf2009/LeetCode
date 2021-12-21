from typing import List

# Given a rows x cols binary matrix filled with 0's and 1's, find the 
# largest rectangle containing only 1's and return its area.

# Stack - Please refer to LeetCode 84 - Largest rectangle area in histogram
# Scan every row of grid, calculate the max rect area in the formed 
# histogram by far.
class Solution:
    def largestRectAreaInHistogram(self, heights: List[int]) -> int:
        def getMaxArea(heights, rightBarPos, rightBarHeight) -> int:
            maxArea = 0
            h = 0
            while len(eabPos) > 0 and heights[eabPos[-1]] > rightBarHeight:
                i = eabPos.pop()
                h = heights[i]
                if len(eabPos) == 0:
                    leftBarPos = -1
                else:
                    leftBarPos = eabPos[-1]
                maxArea = max(maxArea, (rightBarPos - leftBarPos - 1) * h)
            return maxArea

        maxArea = 0
        eabPos = []        
        for i in range(len(heights)):
            if len(eabPos) != 0 and heights[eabPos[-1]] > heights[i]:
                maxArea = max(maxArea, getMaxArea(heights, i, heights[i]))
            eabPos.append(i)

        maxArea = max(maxArea, getMaxArea(heights, len(heights), -1))
        return maxArea

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0

        histo = [0] * len(matrix[0])
        maxArea = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '1':
                    histo[j] += 1
                else:
                    histo[j] = 0
            maxArea = max(maxArea, self.largestRectAreaInHistogram(histo))

        return maxArea


if __name__ == '__main__':
    sol = Solution()

    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"], 
              ["1", "0", "0", "1", "0"]]
    r = sol.maximalRectangle(matrix)
    print(r)
    assert(r == 6)

    matrix = [["0","1"],
              ["1","0"]]
    r = sol.maximalRectangle(matrix)
    print(r)
    assert(r == 1)

    matrix = []
    r = sol.maximalRectangle(matrix)
    print(r)
    assert(r == 0)

    matrix = [["0"]]
    r = sol.maximalRectangle(matrix)
    print(r)
    assert(r == 0)

    matrix = [["1"]]
    r = sol.maximalRectangle(matrix)
    print(r)
    assert(r == 1)

    matrix = [["0", "0"]]
    r = sol.maximalRectangle(matrix)
    print(r)
    assert(r == 0)
