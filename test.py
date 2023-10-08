from board import board
from piece import *
# Full board in progress
pieces = [[none([0,0],0),none([0,1],0),none([0,2],0),none([0,3],0),none([0,4],0),none([0,5],0),none([0,6],0),none([0,7],0)],
          [Pawn([1,0],(-1),0),Pawn([1,1],(-1),0),Pawn([1,2],(-1),0),Pawn([1,0],(-1),3),Pawn([1,4],(-1),0),Pawn([1,5],(-1),0),Pawn([1,6],(-1),0),Pawn([1,7],(-1),0)],
          [none([2,0],0),none([2,1],0),none([2,2],0),none([2,3],0),none([2,4],0),none([2,5],0),none([2,6],0),none([2,7],0)],
          [none([3,0],0),none([3,1],0),none([3,2],0),none([3,3],0),none([3,4],0),none([3,5],0),none([3,6],0),none([3,7],0)],
          [none([4,0],0),none([4,1],0),none([4,2],0),none([4,3],0),none([4,4],0),none([4,5],0),none([4,6],0),none([4,7],0)],
          [none([5,0],0),none([5,1],0),none([5,2],0),none([5,3],0),none([5,4],0),none([5,5],0),none([5,6],0),none([5,7],0)],
          [Pawn([6,0],1,0),Pawn([6,1],1,0),Pawn([6,2],1,0),Pawn([6,3],1,0),Pawn([6,4],1,0),Pawn([6,5],1,0),Pawn([6,6],1,0),Pawn([6,7],1,0)],
          [none([7,0],0),none([7,1],0),none([7,2],0),none([7,3],0),none([7,4],0),none([7,5],0),none([7,6],0),none([7,7],0)]]
b = board(pieces)


p = int(input("Would you like to play in literal mode or logic mode (human coordinate pairs or computer coordinate pairs)? 1 or 0: "))

b.print_board()

i = ""
tt = 0
turn_c = "white"
turn_c_i = 1
while i != "end":
    
    i = input(f"What is the move you would like to make {turn_c}? ")
    if i == "end":
        print(f"{turn_c} wins in {tt} moves")
        break
    if b.pieces[int(i[0]) - p][int(i[1]) - p].color == turn_c_i:
        if b.pieces[int(i[0]) - p][int(i[1]) - p].move([int(i[2]) - p, int(i[3]) - p], b) == 0:
            if turn_c == "white":
                turn_c = "black"
            else:
                turn_c = "white"
            turn_c_i *= -1
            tt += 1