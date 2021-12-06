from typing import List

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other. Given an integer n, return all
# distinct solutions to the n-queens puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens' placement,
# where 'Q' and '.' both indicate a queen and an empty space, respectively.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def validPos(i, curPos) -> bool:
            for j in range(i):
                if pos[j] == curPos or abs(curPos - pos[j]) == i - j:
                    return False
            return True

        def saveSolution(ans, mirrorAns, pos, n):
            board = []
            mirrorBoard = []
            for j in pos:
                line = '.' * j + 'Q' + '.' * (n - j - 1)
                board.append(line)
                mirrorBoard.append(line[::-1])
            if pos[0] < n // 2:
                mirrorAns.append(mirrorBoard)
            ans.append(board)

        ans = []
        mirrorAns = []
        i = 0
        pos = [0] * n   # Queens' position on each line of board
        while i > 0 or (i == 0 and pos[i] < (n + 1) // 2):
            if pos[i] < n:
                if validPos(i, pos[i]):
                    i += 1
                    if i == n:
                        saveSolution(ans, mirrorAns, pos, n)
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

        ans.extend(mirrorAns[::-1])
        return ans


if __name__ == '__main__':
    sol = Solution()

    r = sol.solveNQueens(4)
    print(r)
    assert(r == [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]])

    r = sol.solveNQueens(1)
    print(r)
    assert(r == [["Q"]])
