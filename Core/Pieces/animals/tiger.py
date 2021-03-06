#! /usr/bin/env python3
import string
from Core.Pieces.abs_bishop import AbsBishop
alphabet=string.ascii_uppercase[0:8] #string used for chess board
lb = alphabet.index("B")
ub = alphabet.index("G")

class Tiger(AbsBishop):
    """A piece of chess"""
    def __init__(self,c,a):
        self.piece="Tiger"
        self.color=bool(c)
        self.army=str(a)
    
    def moves(self,x,y):
#        return self.bishopMoves(x,y)
        """Returns Valid moves to the model"""
        listD=[]
        """Bishop moves, diagonal lines, both directions
        add the tuple to listD declared above
        needs four loops to work, 
        one to find "increasing coordinates" 
        one to find "decreasing coordinates" """
        xValue=alphabet.index(x)
        oxValue=xValue
        yValue=y
        while xValue < alphabet.index("H") and yValue < 8 and xValue < oxValue+2:
            xValue+=1
            yValue+=1
            listD+=[(alphabet[xValue],yValue)]
        xValue=alphabet.index(x)
        yValue=y
        while xValue > alphabet.index("A") and yValue > 1 and xValue > oxValue-2:
            xValue-=1
            yValue-=1
            listD+=[(alphabet[xValue],yValue)]
	
        xValue=alphabet.index(x)
        yValue=y
        while xValue > alphabet.index("A") and yValue < 8 and xValue > oxValue-2:
            xValue-=1
            yValue+=1
            listD+=[(alphabet[xValue],yValue)]
        xValue=alphabet.index(x)
        yValue=y
        while xValue < alphabet.index("H") and yValue > 1 and xValue < oxValue+2:
            xValue+=1
            yValue-=1
            listD+=[(alphabet[xValue],yValue)]



        return listD


