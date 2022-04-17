from typing import List

#Given an m x n matrix, return all elements of the matrix in spiral order.

# Time: O(m*n)
# - Control logic:
#   - assume matrix dimension: m x n
#   - each time an entire row or column is scanned, m or n is reduced by 1;
#   - if either m or n reach 0, the scan ends;
#   - the index i and j change pattern in each direction of scan:
#     j + 1, i + 1, j - 1, i - 1
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0]) # max move per direction
        step = 1     # 1 when moving right, down; -1 when moving left, up
        i, j = 0, -1 # current position
        res = []
        while m * n > 0:
            for _ in range(n):
                j += step
                res.append(matrix[i][j])
            m -= 1
            for _ in range(m):
                i += step
                res.append(matrix[i][j])
            n -= 1
            step *= -1

        return res

# too slow, too complex?
class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        # Boundries
        left, right, top, bottom = -1, n, 0, m
        orient = 0
        res = []
        i, j = 0, 0
        while True:
            res.append(matrix[i][j])
            if orient == 0:
                if j + 1 < right:
                    j += 1
                    continue
                elif i + 1 < bottom:
                    right -= 1
                    i += 1
                    orient += 1
                    continue
                else:
                    break
            elif orient == 1:
                if i + 1 < bottom:
                    i += 1
                    continue
                elif j - 1 > left:
                    bottom -= 1
                    j = j - 1
                    orient += 1
                else:
                    break
            elif orient == 2:
                if j - 1 > left:
                    j = j - 1
                    continue
                elif i - 1 > top:
                    left += 1
                    i -= 1
                    orient += 1
                else:
                    break
            else: # orient = 3
                if i - 1 > top:
                    i -= 1
                    continue
                elif j + 1 < right:
                    top += 1
                    j += 1
                    orient = 0

        return res


if __name__ == '__main__':
    r = Solution().spiralOrder(matrix = [[1,2,3],
                                         [4,5,6],
                                         [7,8,9]])
    print(r)
    assert(r == [1,2,3,6,9,8,7,4,5])

    r = Solution().spiralOrder(matrix = [[1,2,3,4],
                                         [5,6,7,8],
                                         [9,10,11,12]])
    print(r)
    assert(r == [1,2,3,4,8,12,11,10,9,5,6,7])
