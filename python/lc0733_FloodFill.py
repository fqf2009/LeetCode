# An image is represented by an m x n integer grid image where 
# image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and newColor. You should 
# perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels 
# connected 4-directionally to the starting pixel of the same color as 
# the starting pixel, plus any pixels connected 4-directionally to those 
# pixels (also with the same color), and so on. Replace the color of all 
# of the aforementioned pixels with newColor.

# Return the modified image after performing the flood fill.
from typing import List

# BFS
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        delta = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        image[sr][sc] = newColor    # mark visited before enqueue
        que = [(sr, sc)]
        while len(que) > 0:
            sr, sc = que.pop()
            for dx, dy in delta:
                sr1, sc1 = sr + dy, sc + dx
                if (sr1 >= 0 and sr1 < m and sc1 >= 0 and sc1 < n and 
                    image[sr1][sc1] == oldColor):
                    image[sr1][sc1] = newColor  # mark visited before enqueue
                    que.append((sr1, sc1))

        return image


# DFS
class Solution1:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image

        image[sr][sc] = newColor
        delta = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        for dx, dy in delta:
            sr1, sc1 = sr + dy, sc + dx
            if (sr1 >= 0 and sr1 < m and sc1 >= 0 and sc1 < n and 
                image[sr1][sc1] == oldColor):
                self.floodFill(image, sr1, sc1, newColor)

        return image


if __name__ == "__main__":
    def unitTest(sol):
        r = sol.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2)
        print(r)
        assert r == [[2,2,2],[2,2,0],[2,0,1]]

        r = sol.floodFill(image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2)
        print(r)
        assert r == [[2,2,2],[2,2,2]]

        r = sol.floodFill(image = [[0,0,0],[0,1,1]], sr = 1, sc = 1, newColor = 1)
        print(r)
        assert r == [[0,0,0],[0,1,1]]


    unitTest(Solution())
    unitTest(Solution1())
