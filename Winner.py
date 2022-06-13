from Board import Board


class win(Board):
    def __int__(self, rows, cols ):
        super().__init__(rows, cols)
        """
        - - -
        - - -
        - - -
        """
    def win(self, x_cord, y_cord, val):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                    #print(f"{self.board[0][y]}{self.board[1][y]}{self.board[2][y]}")
                    if self.board[x][0] == "x" and self.board[x][1] == "x" and self.board[x][2] == "x":
                        return "Congrats you won horizontally"
                    if self.board[0][y] == "x" and self.board[1][y] == "x" and self.board[2][y] == "x":
                        return "Congrats you won vertically"
                    if self.board[x][0] == "o" and self.board[x][1] == "o" and self.board[x][2] == "o":
                        return "Haha the computer won horizontally"
                    if self.board[0][y] == "o" and self.board[1][y] == "o" and self.board[2][y] == "o":
                        return "Haha the computer won vertically"


