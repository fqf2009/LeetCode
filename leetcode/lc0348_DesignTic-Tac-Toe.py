# Assume the following rules are for the tic-tac-toe game on an n x n board 
# between two players:
#  - A move is guaranteed to be valid and is placed on an empty block.
#  - Once a winning condition is reached, no more moves are allowed.
#  - A player who succeeds in placing n of their marks in a horizontal,
#    vertical, or diagonal row wins the game.
# Implement the TicTacToe class:
#  - TicTacToe(int n) Initializes the object the size of the board n.
#  - int move(int row, int col, int player) Indicates that the player
#    with id player plays at the cell (row, col) of the board. The move 
#    is guaranteed to be a valid move.
# Constraints:
#   2 <= n <= 100
#   player is 1 or 2.
#   0 <= row, col < n
#   (row, col) are unique for each different call to move.
#   At most n2 calls will be made to move.


# - save a little space
class TicTacToe:

    def __init__(self, n: int):
        self.board_size = n
        self.row_sum = [0] * n
        self.col_sum = [0] * n
        self.diag_sum = [0] * 2

    def move(self, row: int, col: int, player: int) -> int:
        pid = 1 if player == 1 else -1
        self.row_sum[row] += pid
        self.col_sum[col] += pid
        if row == col:
            self.diag_sum[0] += pid
        if row + col == self.board_size - 1:
            self.diag_sum[1] += pid
        
        if self.board_size in (abs(self.row_sum[row]), abs(self.col_sum[col]), 
                               abs(self.diag_sum[0]), abs(self.diag_sum[1])):
            return player
        else:
            return 0


class TicTacToe1:

    def __init__(self, n: int):
        self.board_size = n
        self.row_sum = [[0, 0] for _ in range(n)]
        self.col_sum = [[0, 0] for _ in range(n)]
        self.diag_sum = [[0, 0] for _ in range(2)]

    def move(self, row: int, col: int, player: int) -> int:
        pid = player - 1
        self.row_sum[row][pid] += 1
        self.col_sum[col][pid] += 1
        if row == col:
            self.diag_sum[0][pid] += 1
        if row + col == self.board_size - 1:
            self.diag_sum[1][pid] += 1
        
        if self.board_size in (self.row_sum[row][pid], self.col_sum[col][pid], 
                                self.diag_sum[0][pid], self.diag_sum[1][pid]):
            return player
        else:
            return 0


if __name__ == "__main__":

    def unitTest(Sol):
        inputs = [["move", "move", "move", "move", "move", "move", "move"],
                  [[0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1],
                   [1, 0, 2], [2, 1, 1]]]
        expected = [None, 0, 0, 0, 0, 0, 0, 1]
        outputs = [None]
        obj = Sol(3)                          # obj = TicTacToe(n)
        for method, param in zip(inputs[0], inputs[1]):
            r = getattr(obj, method)(*param)  # obj.move(row,col,player)
            outputs.append(r)
        print(outputs)
        assert outputs == expected

        inputs = [["move","move","move"],
                  [[0,0,2],[1,1,1],[0,1,2]]]
        expected = [None, 0, 0, 2]
        outputs = [None]
        obj = Sol(2)                          # obj = TicTacToe(n)
        for method, param in zip(inputs[0], inputs[1]):
            r = getattr(obj, method)(*param)  # obj.move(row,col,player)
            outputs.append(r)
        print(outputs)
        assert outputs == expected

        inputs = [["move","move","move"],
                  [[0,1,1],[1,1,2],[1,0,1]]]
        expected = [None, 0, 0, 1]
        outputs = [None]
        obj = Sol(2)                          # obj = TicTacToe(n)
        for method, param in zip(inputs[0], inputs[1]):
            r = getattr(obj, method)(*param)  # obj.move(row,col,player)
            outputs.append(r)
        print(outputs)
        assert outputs == expected

    unitTest(TicTacToe)
    unitTest(TicTacToe1)
