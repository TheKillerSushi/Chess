
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
        self.enpassant = False
    # AHHHHHHHHHHH AHHHHHHHH AHHHHHHH
    # Okay i need to ummmmmm maybe do a check move thingy thing.
    def move(self, new_board_pos,  board):
        if self.turn == 0 and new_board_pos[0] == self.board_pos[0] + 2  * (self.color * -1) and new_board_pos[1] == self.board_pos[1]:
            middle_board_pos = [self.board_pos[0], self.board_pos[1]]

            middle_board_pos[0] = middle_board_pos[0] - self.color 

            #if board.check_board_pos(new_board_pos) != 0 or board.check_board_pos(middle_board_pos) != 0:
            #    board.print_board()
            #    print("Invalid move")
            #    return 2
            # updates old square
            board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
            self.board_pos = new_board_pos
            # updates new square
            self.turn += 1
            board.pieces[new_board_pos[0]][new_board_pos[1]] = Pawn(new_board_pos, self.color, self.turn)
            board.print_board()
            board.pieces[new_board_pos[0]][new_board_pos[1]].enpassant = True
            return 0

        elif new_board_pos[0] == self.board_pos[0] - self.color and new_board_pos[1] == self.board_pos[1]:
            if board.check_board_pos(new_board_pos) != 0:
                board.print_board()
                return 1
            board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
            self.board_pos = new_board_pos
            # updates new square
            self.turn += 1
            board.pieces[new_board_pos[0]][new_board_pos[1]] = Pawn(new_board_pos, self.color, self.turn)
            board.print_board()
            return 0
        elif new_board_pos[0] == self.board_pos[0] + (self.color * -1) and board.pieces[new_board_pos[0]][new_board_pos[1]].val == 0 and(new_board_pos[1] == self.board_pos[1] + 1 or new_board_pos[1] == self.board_pos[1] - 1) :
            if board.pieces[self.board_pos[0]][new_board_pos[1]].val == 1:
                if board.pieces[self.board_pos[0]][new_board_pos[1]].enpassant == True:
                    board.pieces[self.board_pos[0]][new_board_pos[1]] = none([[self.board_pos[0]],[new_board_pos[1]]], 0)
                    board.pieces[self.board_pos[0]][self.board_pos[1]] = none([[self.board_pos[0]],[self.board_pos[1]]], 0)
                    self.board_pos = new_board_pos
                    board.pieces[self.board_pos[0]][self.board_pos[1]] = self
                    board.print_board()
                    return 0
            
        elif new_board_pos[0] == self.board_pos[0] + (self.color * -1) and board.pieces[new_board_pos[0]][new_board_pos[1]].val > 0 and (new_board_pos[1] == self.board_pos[1] + 1 or new_board_pos[1] == self.board_pos[1] - 1) and board.pieces[new_board_pos[0]][new_board_pos[1]].color != self.color:
            board.pieces[self.board_pos[0]][self.board_pos[1]] = none([[self.board_pos[0]],[self.board_pos[1]]],0)
            self.board_pos = new_board_pos
            board.pieces[self.board_pos[0]][self.board_pos[1]] = self
            board.print_board()
            return 0
class Knight:
    def __init__(self, board_pos, color, turn):
        self.board_pos = board_pos
        self.color = color
        self.val = 2
        self.turn = turn
    
    #def move(self, new_board_pos, board):
        # +2 -1, +2 +1, -2 + 1, -2 -1, -1 +2, -1 -2, +1 -2, +1 +2 
    #    if new_board_pos == board.pieces[self.board_pos[0] + 2][self.board_pos[1] + 1].board_pos and :

    def move(self, new_board_pos, board):
        if board.pieces[new_board_pos[0]][new_board_pos[1]].color == self.color:
            return 1
        if new_board_pos[0] == self.board_pos[0] + 1:
            if new_board_pos[1] == self.board_pos[1] + 2:
                board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                board.pieces[self.board_pos[0]][self.board_pos[1]] = none([new_board_pos[0], new_board_pos[1]], 0)
                self.board_pos = [new_board_pos[0], new_board_pos[1]]
                board.print_board()
                return 0

            if new_board_pos[1] == self.board_pos[1] - 2:
                board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                board.pieces[self.board_pos[0]][self.board_pos[1]] = none([new_board_pos[0], new_board_pos[1]], 0)
                self.board_pos = [new_board_pos[0], new_board_pos[1]]
                board.print_board()
                return 0
        if new_board_pos[0] == self.board_pos[0] - 1:
            if new_board_pos[1] == self.board_pos[1] + 2:
                board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                board.pieces[self.board_pos[0]][self.board_pos[1]] = none([new_board_pos[0], new_board_pos[1]], 0)
                self.board_pos = [new_board_pos[0], new_board_pos[1]]
                board.print_board()
                return 0
            if new_board_pos[1] == self.board_pos[1] - 2:
                board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                board.pieces[self.board_pos[0]][self.board_pos[1]] = none([new_board_pos[0], new_board_pos[1]], 0)
                self.board_pos = [new_board_pos[0], new_board_pos[1]]
                board.print_board()
                return 0
        if new_board_pos[0] == self.board_pos[0] + 2:
            if new_board_pos[1] == self.board_pos[1] + 1:
                board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                board.pieces[self.board_pos[0]][self.board_pos[1]] = none([new_board_pos[0], new_board_pos[1]], 0)
                self.board_pos = [new_board_pos[0], new_board_pos[1]]
                board.print_board()
                return 0
            if new_board_pos[1] == self.board_pos[1] - 1:
                board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                board.pieces[self.board_pos[0]][self.board_pos[1]] = none([new_board_pos[0], new_board_pos[1]], 0)
                self.board_pos = [new_board_pos[0], new_board_pos[1]]
                board.print_board()
                return 0
        if new_board_pos[0] == self.board_pos[0] - 2:
            if new_board_pos[1] == self.board_pos[1] + 1:
                board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                board.pieces[self.board_pos[0]][self.board_pos[1]] = none([new_board_pos[0], new_board_pos[1]], 0)
                self.board_pos = [new_board_pos[0], new_board_pos[1]]
                board.print_board()
                return 0
            if new_board_pos[1] == self.board_pos[1] - 1:
                board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                board.pieces[self.board_pos[0]][self.board_pos[1]] = none([new_board_pos[0], new_board_pos[1]], 0)
                self.board_pos = [new_board_pos[0], new_board_pos[1]]
                board.print_board()
                return 0
            
class Bishop:
    def __init__(self, board_pos, color, turn):
        self.board_pos = board_pos
        self.color = color
        self.val = 3
        self.turn = turn

    def move(self, new_board_pos, board):
        if board.pieces[new_board_pos[0]][new_board_pos[1]].color == self.color:
            board.print_board()
            return 1
        find_square = [self.board_pos[0], self.board_pos[1]]
        if new_board_pos[0] < self.board_pos[0]:
            if new_board_pos[1] < self.board_pos[1]:
                while find_square != new_board_pos:
                    find_square[0] -= 1
                    find_square[1] -= 1
                    if find_square == new_board_pos:
                        board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                        board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
                        self.board_pos = new_board_pos
                        board.print_board()
                        return 0
                    if board.pieces[find_square[0]][find_square[1]].val > 0:
                        board.print_board()
                        return 1
            
            if new_board_pos[1] > self.board_pos[1]:
                while find_square != new_board_pos:
                    find_square[0] -= 1
                    find_square[1] += 1
                    if find_square == new_board_pos:
                        board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                        board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
                        self.board_pos = new_board_pos
                        board.print_board()
                        return 0
                    if board.pieces[find_square[0]][find_square[1]].val > 0:
                        board.print_board()
                        return 1
            
            if new_board_pos[1] > self.board_pos[1]:
                while find_square != new_board_pos:
                    find_square[0] -= 1
                    find_square[1] += 1
                    if find_square == new_board_pos:
                        board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                        board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
                        self.board_pos = new_board_pos
                        board.print_board()
                        return 0
                    if board.pieces[find_square[0]][find_square[1]].val > 0:
                        board.print_board()
                        return 1
                    
        if new_board_pos[0] > self.board_pos[0]:
            if new_board_pos[1] < self.board_pos[1]:
                while find_square != new_board_pos:
                    find_square[0] += 1
                    find_square[1] -= 1
                    if find_square == new_board_pos:
                        board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                        board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
                        self.board_pos = new_board_pos
                        board.print_board()
                        return 0
                    if board.pieces[find_square[0]][find_square[1]].val > 0:
                        board.print_board()
                        return 1
            
            if new_board_pos[1] > self.board_pos[1]:
                while find_square != new_board_pos:
                    find_square[0] += 1
                    find_square[1] += 1
                    if find_square == new_board_pos:
                        board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                        board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
                        self.board_pos = new_board_pos
                        board.print_board()
                        return 0
                    if board.pieces[find_square[0]][find_square[1]].val > 0:
                        board.print_board()
                        return 1

class Rook:
    def __init__(self, board_pos, color, turn):
        self.board_pos = board_pos
        self.color = color
        self.val = 4
        self.turn = turn
    
    def move(self, new_board_pos, board):
        if board.pieces[new_board_pos[0]][new_board_pos[1]].color == self.color:
            board.print_board()
            return 1
        find_square = [self.board_pos[0], self.board_pos[1]]
        if self.board_pos[0] == new_board_pos[0]:
            if new_board_pos[1] < self.board_pos[1]:
                while find_square != new_board_pos:
                    find_square[1] -= 1
                    if find_square == new_board_pos:
                        board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                        board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
                        self.board_pos = new_board_pos
                        self.turn += 1
                        board.print_board()
                        return 0
                    if board.pieces[find_square[0]][find_square[1]].val > 0:
                        board.print_board()
                        return 1
            
            if new_board_pos[1] > self.board_pos[1]:
                while find_square != new_board_pos:
                    find_square[1] += 1
                    if find_square == new_board_pos:
                        board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                        board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
                        self.board_pos = new_board_pos
                        board.print_board()
                        self.turn += 1
                        return 0
                    if board.pieces[find_square[0]][find_square[1]].val > 0:
                        board.print_board()
                        return 1
        
        if self.board_pos[1] == new_board_pos[1]:
            if new_board_pos[0] < self.board_pos[0]:
                while find_square != new_board_pos:
                    find_square[0] -= 1
                    if find_square == new_board_pos:
                        board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                        board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
                        self.board_pos = new_board_pos
                        board.print_board()
                        self.turn += 1
                        return 0
                    if board.pieces[find_square[0]][find_square[1]].val > 0:
                        board.print_board()
                        return 1
            
            if new_board_pos[0] > self.board_pos[0]:
                while find_square != new_board_pos:
                    find_square[0] += 1
                    if find_square == new_board_pos:
                        board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                        board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
                        self.board_pos = new_board_pos
                        board.print_board()
                        self.turn += 1
                        return 0
                    if board.pieces[find_square[0]][find_square[1]].val > 0:
                        board.print_board()
                        return 1
class Queen:
    def __init__(self, board_pos, color, turn):
        self.board_pos = board_pos
        self.color = color
        self.val = 5
        self.turn = turn
    
    def move(self, new_board_pos, board):
        if board.pieces[new_board_pos[0]][new_board_pos[1]].color == self.color:
            board.print_board()
            return 1
        find_square = [self.board_pos[0], self.board_pos[1]]
        if new_board_pos[0] == self.board_pos[0] or new_board_pos[1] == self.board_pos[1]:
            if self.board_pos[0] == new_board_pos[0]:
                if new_board_pos[1] < self.board_pos[1]:
                    while find_square != new_board_pos:
                        find_square[1] -= 1
                        if find_square == new_board_pos:
                            board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                            board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
                            self.board_pos = new_board_pos
                            board.print_board()
                            return 0
                        if board.pieces[find_square[0]][find_square[1]].val > 0:
                            board.print_board()
                            return 1
            
                if new_board_pos[1] > self.board_pos[1]:
                    while find_square != new_board_pos:
                        find_square[1] += 1
                        if find_square == new_board_pos:
                            board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                            board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
                            self.board_pos = new_board_pos
                            board.print_board()
                            return 0
                        if board.pieces[find_square[0]][find_square[1]].val > 0:
                            board.print_board()
                            return 1
        
            if self.board_pos[1] == new_board_pos[1]:
                if new_board_pos[0] < self.board_pos[0]:
                    while find_square != new_board_pos:
                        find_square[0] -= 1
                        if find_square == new_board_pos:
                            board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                            board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
                            self.board_pos = new_board_pos
                            board.print_board()
                            return 0
                        if board.pieces[find_square[0]][find_square[1]].val > 0:
                            board.print_board()
                            return 1
            
                if new_board_pos[0] > self.board_pos[0]:
                    while find_square != new_board_pos:
                        find_square[0] += 1
                        if find_square == new_board_pos:
                            board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                            board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
                            self.board_pos = new_board_pos
                            board.print_board()
                            return 0
                        if board.pieces[find_square[0]][find_square[1]].val > 0:
                            board.print_board()
                            return 1
                        
        if new_board_pos[0] < self.board_pos[0]:
            if new_board_pos[1] < self.board_pos[1]:
                while find_square != new_board_pos:
                    find_square[0] -= 1
                    find_square[1] -= 1
                    if find_square == new_board_pos:
                        board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                        board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
                        self.board_pos = new_board_pos
                        board.print_board()
                        return 0
                    if board.pieces[find_square[0]][find_square[1]].val > 0:
                        board.print_board()
                        return 1
            
            if new_board_pos[1] > self.board_pos[1]:
                while find_square != new_board_pos:
                    find_square[0] -= 1
                    find_square[1] += 1
                    if find_square == new_board_pos:
                        board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                        board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
                        self.board_pos = new_board_pos
                        board.print_board()
                        return 0 
                    if board.pieces[find_square[0]][find_square[1]].val > 0:
                        board.print_board()
                        return 1
            
            if new_board_pos[1] > self.board_pos[1]:
                while find_square != new_board_pos:
                    find_square[0] -= 1
                    find_square[1] += 1
                    if find_square == new_board_pos:
                        board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                        board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
                        self.board_pos = new_board_pos
                        board.print_board()
                        return 0
                    if board.pieces[find_square[0]][find_square[1]].val > 0:
                        board.print_board()
                        return 1
                    
        if new_board_pos[0] > self.board_pos[0]:
            if new_board_pos[1] < self.board_pos[1]:
                while find_square != new_board_pos:
                    find_square[0] += 1
                    find_square[1] -= 1
                    if find_square == new_board_pos:
                        board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                        board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
                        self.board_pos = new_board_pos
                        board.print_board()
                        return 0
                    if board.pieces[find_square[0]][find_square[1]].val > 0:
                        board.print_board()
                        return 1
            
            if new_board_pos[1] > self.board_pos[1]:
                while find_square != new_board_pos:
                    find_square[0] += 1
                    find_square[1] += 1
                    if find_square == new_board_pos:
                        board.pieces[new_board_pos[0]][new_board_pos[1]] = self
                        board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
                        self.board_pos = new_board_pos
                        board.print_board()
                        return 0
                    if board.pieces[find_square[0]][find_square[1]].val > 0:
                        board.print_board()
                        return 1
                    
class King:
    def __init__(self, board_pos, color, turn):
        self.board_pos = board_pos
        self.color = color
        self.val = 6
        self.turn = turn

    def move(self, new_board_pos, board):
        if board.pieces[new_board_pos[0]][new_board_pos[1]].color == self.color:
            board.print_board()
            return 1
        if self.turn == 0 and new_board_pos[0] == self.board_pos[0]:
            if new_board_pos[1] == self.board_pos[1] - 2:
                if board.pieces[self.board_pos[0]][self.board_pos[1] - 4].turn == 0:
                    if board.pieces[self.board_pos[0]][self.board_pos[1] - 4].move([self.board_pos[0], self.board_pos[1] - 1], board) == 0:
                        board.pieces[self.board_pos[0]][self.board_pos[1] - 2] = self
                        board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
                        self.board_pos = new_board_pos
                        board.print_board()
                        self.turn += 1
                        return 0
            if new_board_pos[1] == self.board_pos[1] + 2:
                if board.pieces[self.board_pos[0]][self.board_pos[1] + 3].turn == 0:
                    if board.pieces[self.board_pos[0]][self.board_pos[1] + 3].move([self.board_pos[0], self.board_pos[1] + 1], board) == 0:
                        board.pieces[self.board_pos[0]][self.board_pos[1] + 2] = self
                        board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
                        self.board_pos = new_board_pos
                        board.print_board()
                        self.turn += 1
                        return 0
        if new_board_pos[0] == self.board_pos[0] - 1 and new_board_pos[1] == self.board_pos[1] - 1:
            board.pieces[new_board_pos[0]][new_board_pos[1]] = self
            board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
            self.board_pos = new_board_pos
            board.print_board()
            return 0
        if new_board_pos[0] == self.board_pos[0] - 1 and new_board_pos[1] == self.board_pos[1]:
            board.pieces[new_board_pos[0]][new_board_pos[1]] = self
            board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
            self.board_pos = new_board_pos
            board.print_board()
            return 0
        if new_board_pos[0] == self.board_pos[0] - 1 and new_board_pos[1] == self.board_pos[1] + 1:
            board.pieces[new_board_pos[0]][new_board_pos[1]] = self
            board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
            self.board_pos = new_board_pos
            board.print_board()
            return 0
        if new_board_pos[0] == self.board_pos[0] and new_board_pos[1] == self.board_pos[1] - 1:
            board.pieces[new_board_pos[0]][new_board_pos[1]] = self
            board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
            self.board_pos = new_board_pos
            board.print_board()
            return 0
        if new_board_pos[0] == self.board_pos[0] and new_board_pos[1] == self.board_pos[1] + 1:
            board.pieces[new_board_pos[0]][new_board_pos[1]] = self
            board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
            self.board_pos = new_board_pos
            board.print_board()
            return 0
        if new_board_pos[0] == self.board_pos[0] + 1 and new_board_pos[1] == self.board_pos[1] - 1:
            board.pieces[new_board_pos[0]][new_board_pos[1]] = self
            board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
            self.board_pos = new_board_pos
            board.print_board()
            return 0
        if new_board_pos[0] == self.board_pos[0] + 1 and new_board_pos[1] == self.board_pos[1]:
            board.pieces[new_board_pos[0]][new_board_pos[1]] = self
            board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
            self.board_pos = new_board_pos
            board.print_board()
            return 0
        if new_board_pos[0] == self.board_pos[0] - 1 and new_board_pos[1] == self.board_pos[1] + 1:
            board.pieces[new_board_pos[0]][new_board_pos[1]] = self
            board.pieces[self.board_pos[0]][self.board_pos[1]] = none([self.board_pos[0], self.board_pos[1]], 0)
            self.board_pos = new_board_pos
            board.print_board()
            return 0
                    