from stack import Stack
import time

MIN_CELL_NUM = 1
MAX_CELL_NUM = 10


class Board(object):
    DEFAULT_BOARD = [
    [5, 0, 0, 0, 7, 0, 0, 8, 4],
    [0, 0, 9, 0, 0, 1, 2, 0, 0],
    [0, 0, 0, 5, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 9, 6, 0, 4, 0],
    [7, 5, 3, 0, 0, 0, 1, 0, 0],
    [0, 7, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 2, 0],
    [9, 0, 0, 0, 0, 0, 3, 0, 0]
    ]

    def __init__(self, board=DEFAULT_BOARD):
        self.board = board
        self._change_stack = Stack()  # stores the cells xy values you have changed

    def btsolve(self):
        """
        The function preformes a backtracking method to solve a sudoku board.
        :return: bool, whether is succeeded to solve the board or not.
        """
        start_time = time.time()
        empty_cell = self._find_empty_cell()
        if not empty_cell:
            print 'it took me {0} seconds!'.format(time.time() - start_time)
            return True
        row, col = empty_cell
        for num in range(MIN_CELL_NUM, MAX_CELL_NUM):  # 1 - 9
            if self._is_valid(num, row, col):
                self.board[row][col] = num
                if self.btsolve():
                    return True
                self.board[row][col] = 0
        return False

    def stackbtsolve(self):
        start_time = time.time()
        empty_cell = self._find_empty_cell()
        while self._find_empty_cell():
            row, col = empty_cell

            for num in range(MIN_CELL_NUM, MAX_CELL_NUM):
                if self._is_valid(num, row, col):
                    self.board[row][col] = num
                    self._change_stack.push((row, col))
                    #print 'A - changed {0}, {1} to {2}'.format(row, col, num)
                    break

            while self.board[row][col] == 0 and not self._change_stack.empty():
                row, col = self._change_stack.pop()
                #print row, col, self.board[row][col]
                value = self.board[row][col]
                self.board[row][col] = 0

                for num in range(value + 1, MAX_CELL_NUM):
                    if self._is_valid(num, row, col):
                        self.board[row][col] = num
                        self._change_stack.push((row, col))
                        #print 'B - changed {0}, {1} to {2}'.format(row, col, num)
                        break

            empty_cell = self._find_empty_cell()
        print 'it took me {0} seconds!'.format(time.time() - start_time)


    def _is_valid(self, num, x, y):
        """

        :param num: a number to check if can be placed in board[x][y]
        :param x: the x pos of the empty cell
        :param y: the y pos of the empty cell
        :return: a bool, means :param num: can be placed in board[x][y].
        """
        # check row
        for i in range(9):
            if self.board[x][i] == num:
                return False

        # check col
        for i in range(9):
            if self.board[i][y] == num:
                return False

        # check box
        box_x = x // 3
        box_y = y // 3

        for i in range(box_x * 3, box_x * 3 + 3):
            for j in range(box_y * 3, box_y * 3 + 3):
                if self.board[i][j] == num and (i, j) != (x, y):
                    return False

        return True

    def _find_empty_cell(self):
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if self.board[i][j] == 0:
                    cell = (i, j)
                    return cell
        return None

    def print_board(self):
        """
        The function prints the board :)
        """
        for i, row in enumerate(self.board):
            if i % 3 == 0 and i != 0:
                print "- - - - - - - - - - - - - - - - - "

            for j, cell in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print ' | ',
                print str(cell) + ' ',
            print ''


b = Board()
b.print_board()
b.stackbtsolve()
print ''
b.print_board()


