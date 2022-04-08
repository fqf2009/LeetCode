from typing import List
import numpy as np

# Given a 2D matrix matrix, handle multiple queries of the following type:
# Calculate the sum of the elements of matrix inside the rectangle defined 
# by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:
# NumMatrix(int[][] matrix) Initializes the object with the integer matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of 
# the elements of matrix inside the rectangle defined by its upper left 
# corner (row1, col1) and lower right corner (row2, col2).


# Use numpy to compute cumulative sum
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        arr = np.zeros((m + 1, n + 1), dtype='int64')
        arr[1:, 1:] = np.array(matrix, dtype='int64')
        self.sumMatrix = np.cumsum(np.cumsum(arr, axis = 0), axis = 1)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        i1, j1 = row1 + 1, col1 + 1
        i2, j2 = row2 + 1, col2 + 1
        return self.sumMatrix[i2,j2] - self.sumMatrix[i1-1,j2] - \
               self.sumMatrix[i2,j1-1] + self.sumMatrix[i1-1,j1-1]


# Use 1-based sum matrix to simplify code
class NumMatrix1:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.sumMatrix = [[0]*(n+1) for _ in range(m+1)]
        # Error: all rows will be the reference to the first row
        # self.sumMatrix = [[0] * (n+1)] * (m+1)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.sumMatrix[i][j] = matrix[i-1][j-1] + \
                                        self.sumMatrix[i-1][j] + \
                                        self.sumMatrix[i][j-1] - \
                                        self.sumMatrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        i1, j1 = row1 + 1, col1 + 1
        i2, j2 = row2 + 1, col2 + 1
        return self.sumMatrix[i2][j2] - self.sumMatrix[i1-1][j2] - \
               self.sumMatrix[i2][j1-1] + self.sumMatrix[i1-1][j1-1]


# DP approach: S(ABCD) = S(OD) - S(OB) - S(OC) + S(OA)
class NumMatrix2:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.sumMatrix = [[0]*n for _ in range(m)] # This is correct form of 2-D list init
        # self.sumMatrix = [[0]*n]*m  # Wrong: all m rows are the reference to the first row
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    self.sumMatrix[i][j] = matrix[i][j]
                elif i == 0:
                    self.sumMatrix[i][j] = matrix[i][j] + \
                        self.sumMatrix[i][j-1]
                elif j == 0:
                    self.sumMatrix[i][j] = matrix[i][j] + \
                        self.sumMatrix[i-1][j]
                else:
                    self.sumMatrix[i][j] = matrix[i][j] + self.sumMatrix[i-1][j] + \
                        self.sumMatrix[i][j-1] - self.sumMatrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.sumMatrix[row2][col2]
        elif row1 == 0:
            return self.sumMatrix[row2][col2] - self.sumMatrix[row2][col1-1]
        elif col1 == 0:
            return self.sumMatrix[row2][col2] - self.sumMatrix[row1-1][col2]
        else:
            return self.sumMatrix[row2][col2] - self.sumMatrix[row1-1][col2] - \
                self.sumMatrix[row2][col1-1] + self.sumMatrix[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
if __name__ == "__main__":
    input = [ ["NumMatrix", 
               "sumRegion", 
               "sumRegion", 
               "sumRegion"
              ],
              [ [ [3, 0, 1, 4, 2],
                  [5, 6, 3, 2, 1],
                  [1, 2, 0, 1, 5], 
                  [4, 1, 0, 1, 7], 
                  [1, 0, 3, 0, 5] ],
                [2, 1, 4, 3], 
                [1, 1, 2, 2], 
                [1, 2, 2, 4]
              ]
            ]
    expected = [None, 8, 11, 12]
    output = [None]
    obj = globals()[input[0][0]](input[1][0])
    for i in range(1, len(input[0])):
        output.append(getattr(obj, input[0][i])(*input[1][i]))
    print(output)
    assert(output == expected)
