# A square has its [piece value, [coordinates: x, y], color_id: 1 or -1

class board:
    def __init__(self, pieces):
        self.pieces = pieces

    
    def check_board_pos(self, check_square):
        for x in range(8):
            for y in range(8):
                if self.pieces[x][y].board_pos == check_square:
                    print(self.pieces[x][y].val)
                    return self.pieces[x][y].val
    def print_board(self):
        nice_board = [[],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      []]
        z = 0
        print("---------------------------------")
        for x in range(8):
            line = ""
            for y in range(8):
                square_id = []
                if self.pieces[x][y].color == 0:
                    id = " "
                else:
                    if self.pieces[x][y].color == 1:
                        id = "w"
                    else:
                        id = "b"
                if self.pieces[x][y].color != 0:   
                    val = self.pieces[x][y].val
                else:
                    val = 0
                    
                if val == 0:
                    square_id.append("  ")
                elif val == 1:
                    square_id.append("Pa")
                elif val == 2:
                    square_id.append("Kn")
                elif val == 3:
                    square_id.append("Bi")
                elif val == 4:
                    square_id.append("Ro")
                elif val == 5:
                    square_id.append("Qu")
                elif val == 6:
                    square_id.append("Ki")
                  
                square_id.append(id)
                
                square = f"|{square_id[0]}{square_id[1]}"
                
                line += square
            line += "|"
            
            print(line)
            print("---------------------------------")
            z += 1

        
                
