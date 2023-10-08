
class none:
    def __init__(self, board_pos, color):
        self.color = 0
        self.board_pos = board_pos
        self.val = 0
class Pawn:
    def __init__(self, board_pos, color, turn):
        self.board_pos = board_pos
        self.color = color
        self.val = 1
        self.turn = turn
    # AHHHHHHHHHHH AHHHHHHHH AHHHHHHH
    # Okay i need to ummmmmm maybe do a check move thingy thing.
    def move(self, new_board_pos,  board):
        if self.turn == 0 and new_board_pos[0] == self.board_pos[0] + 2  * (self.color * -1) and new_board_pos[1] == self.board_pos[1]:
            middle_board_pos = [self.board_pos[0], self.board_pos[1]]

            middle_board_pos[0] = middle_board_pos[0] - self.color 

            if board.check_board_pos(new_board_pos) != 0 or board.check_board_pos(middle_board_pos) != 0:
                board.print_board()
                print("Invalid move")
                return 2
            # updates old square
            board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
            self.board_pos = new_board_pos
            # updates new square
            self.turn += 1
            board.pieces[new_board_pos[0]][new_board_pos[1]] = Pawn(new_board_pos, self.color, self.turn)
            board.print_board()
            return 0

        elif new_board_pos[0] == self.board_pos[0] - self.color:
            if board.check_board_pos(new_board_pos) != 0:
                board.print_board()
                print("Invalid move")
                return 2
            board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
            self.board_pos = new_board_pos
            # updates new square
            self.turn += 1
            board.pieces[new_board_pos[0]][new_board_pos[1]] = Pawn(new_board_pos, self.color, self.turn)
            board.print_board()
            return 0
            

            