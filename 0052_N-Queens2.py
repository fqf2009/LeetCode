from typing import List

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other. Given an integer n, return the number
# of distinct solutions to the n-queens puzzle.

class Solution:
    def totalNQueens(self, n: int) -> int:
        def validPos(i, curPos) -> bool:
            for j in range(i):
                if pos[j] == curPos or abs(curPos - pos[j]) == i - j:
                    return False
            return True

        ans = 0
        mirrorAns = 0
        i = 0
        pos = [0] * n   # Queens' position on each line of board
        while i > 0 or (i == 0 and pos[i] < (n + 1) // 2):
            if pos[i] < n:
                if validPos(i, pos[i]):
                    i += 1
                    if i == n:
                        ans += 1
                        if pos[0] < n // 2:
                            mirrorAns += 1
                        i -= 1
                        pos[i] = 0
                        i -= 1
                        pos[i] += 1
                else:
                    pos[i] += 1
            else:
                pos[i] = 0
                i -= 1
                pos[i] += 1

        return ans + mirrorAns


if __name__ == '__main__':
    sol = Solution()

    r = sol.totalNQueens(4)
    print(r)
    assert(r == 2)

    r = sol.totalNQueens(1)
    print(r)
    assert(r == 1)
