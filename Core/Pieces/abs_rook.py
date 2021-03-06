#! /usr/bin/env python3
import string
alphabet=string.ascii_uppercase[0:8] #string used for chess board
lb = alphabet.index("B")
ub = alphabet.index("G")

class AbsRook:
    """A piece of chess"""
    def __init__(self,c,a):
        self.piece="Rook"
        self.color=bool(c)
        self.army=str(a)
    
    def rookMoves(self,x,y):
    #Returns Valid moves to the model
        listV=[]
        listH=[]
        """Rook moves, vertical line, + horizontal line
        add the tuple to lists(H&V) declared above"""
        for yValue in range(1,9):
           listV+=[(x,yValue)] 
        for xValue in range(alphabet.index('A'),alphabet.index('H')+1):
           listH+=[(alphabet[xValue],y)]

        """Remove moves which are not moves"""
        listH.remove((x,y))
        listV.remove((x,y))


        return listH+listV

    def rookValidate(self, x, y, plateau, moves):
        moves2 = moves

        return moves2
