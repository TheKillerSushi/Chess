CHESS

Struct:
[br1]{bk1}[bb1]{bK }[bQ ]{bb2}[bk2]{br2}
{bp1}[bp2]{bp3}[bp4]{bp5}[bp6]{bp7}[bp8]
[   ]{   }[   ]{   }[   ]{   }[   ]{   }
{   }[   ]{   }[   ]{   }[   ]{   }[   ]
[   ]{   }[   ]{   }[   ]{   }[   ]{   }
{   }[   ]{   }[   ]{   }[   ]{   }[   ]
[wp1]{wp2}[wp3]{wp4}[wp5]{wp6}[wp7]{wp8}
{wr1}[wk1]{wb1}[wK ]{wQ }[wb2]{wk2}[wr2]


[[none([0,0],0),none([0,1],0),none([0,2],0),none([0,3],0),none([0,4],0),none([0,5],0),none([0,6],0),none([0,7],0)],
          [none([1,0],0),none([1,1],0),none([1,2],0),none([1,3],0),none([1,4],0),none([1,5],0),none([1,6],0),none([1,7],0)],
          [none([2,0],0),none([2,1],0),none([2,2],0),none([2,3],0),none([2,4],0),none([2,5],0),none([2,6],0),none([2,7],0)],
          [none([3,0],0),none([3,1],0),none([3,2],0),none([3,3],0),none([3,4],0),none([3,5],0),none([3,6],0),none([3,7],0)],
          [none([4,0],0),none([4,1],0),none([4,2],0),none([4,3],0),none([4,4],0),none([4,5],0),none([4,6],0),none([4,7],0)],
          [none([5,0],0),none([5,1],0),none([5,2],0),none([5,3],0),none([5,4],0),none([5,5],0),none([5,6],0),none([5,7],0)],
          [none([6,0],0),none([6,1],0),none([6,2],0),none([6,3],0),none([6,4],0),none([6,5],0),none([6,6],0),none([6,7],0)]],
          [none([7,0],0),none([7,1],0),none([7,2],0),none([7,3],0),none([7,4],0),none([7,5],0),none([7,6],0),none([7,7],0)]]

PAWNS:
2 spaces first move is just "y" line + 2

Calculate movement via equation: y = y + c
Calculate first pawn 2 push via equaiton: y = y + 2c
calcualte new location after capture via equation: x = x + 1 if its a right capture or x = x - 1 if left
and equation: y = y + c

En passant is unknown
