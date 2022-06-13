class Board:
    def __init__(self, cols, rows):
        self.board = []
        list = []
        for x in range(rows):
            list = []
            for y in range(cols):
                list.append(" ")
            self.board.append(list)
        for x in range(cols):
            for y in range(rows):
                self.board[x][y] = "-"


