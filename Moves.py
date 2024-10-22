class ShortRange:
    def __init__(self, graphic, piece, links):
        self._graphic= graphic
        self._piece= piece
        self._links= links
        self._playing= True

    def getSquares(self, square):  
        samePlayer= False
        opponentPlayer= False
        if square!=None and square._piece:
            samePlayer= (square._piece._player._number == self._piece._player._number) and (square._piece._piece._playing)
            opponentPlayer= (square._piece._player._number != self._piece._player._number) and (square._piece._piece._playing)
        outsideBoard= (not square)
        if outsideBoard or samePlayer or (opponentPlayer and self._link==self._condition1) or (self._link in self._condition2 and not square._piece._piece._playing):
            pass
        else:
            self._links[self._link]= square

    def getMoves(self):         
        for link in list(self._links.keys()):
            self._links[link]= None
            self._link= link
            square= self._piece._square._links[self._link]            
            self.getSquares(square)
        moves= []
        for link in self._links.values():
            if link:
                moves.append(link)        
        return moves

class King(ShortRange):
    def __init__(self, piece):
        self._graphic= {'black':'♔', 'white':'♚'}
        self._piece= piece
        self._links= {'diagpp':0, 'diagnp':0, 'diagnn':0, 'diagpn':0, 'above':0, 'below':0, 'right':0, 'left':0}
        self._condition1= None
        self._condition2= [None,None]
        super().__init__(self._graphic, self._piece, self._links)

class Pawn(ShortRange):
    def __init__(self, piece):
        self._graphic= {'black':'♙', 'white':'♟'}
        self._piece= piece
        self._links= [{'diagpn':0, 'diagnn':0, 'below':0}, {'diagpp':0, 'diagnp':0, 'above':0}]
        self._condition1= ['below','above'][self._piece._player._number]
        self._condition2= [['diagnn','diagpn'], ['diagnp','diagpp']][self._piece._player._number]
        super().__init__(self._graphic, self._piece, self._links[self._piece._player._number])

    def checkAscend(self):
        if (self._piece._square._board._squares.index(self._piece._square)<4 and self._piece._square._board._turn==1) or (self._piece._square._board._squares.index(self._piece._square)>24 and self._piece._square._board._turn==0):
            self._piece._piece= Queen(self._piece)
            self._piece._graphic= self._piece._piece._graphic[self._piece._color]
        return self._piece

class LongRange:
    def __init__(self, graphic, piece, links):
        self._graphic= graphic
        self._piece= piece
        self._links= links
        self._playing= True

    def getSquares(self, square):
        samePlayer= False
        opponentPlayer= False
        if square!=None and square._piece:      
            samePlayer= (square._piece._player._number == self._piece._player._number) and (square._piece._piece._playing)
            opponentPlayer= (square._piece._player._number != self._piece._player._number) and (square._piece._piece._playing)            
        outsideBoard= (not square)        
        if outsideBoard or samePlayer:
            pass
        elif opponentPlayer:
            self._links[self._link].append(square)
        else:
            self._links[self._link].append(square)
            self.getSquares(square._links[self._link])                

    def getMoves(self):
        for link in list(self._links.keys()):
            self._links[link]= []
            self._link= link
            square= self._piece._square._links[self._link]            
            self.getSquares(square)
        moves= []
        for link in self._links.values():
            moves.extend(link)
        return moves

class Rook(LongRange):
    def __init__(self, piece):
        self._graphic= {'black':'♖', 'white':'♜'}
        self._piece= piece
        self._links= {'above':[], 'below':[], 'right':[], 'left':[]}
        super().__init__(self._graphic, self._piece, self._links)

class Bishop(LongRange):
    def __init__(self, piece):
        self._graphic= {'black':'♗', 'white':'♝'}
        self._piece= piece
        self._links= {'diagpp':[], 'diagnp':[], 'diagnn':[], 'diagpn':[]}
        super().__init__(self._graphic, self._piece, self._links)

class Queen(LongRange):
    def __init__(self, piece):
        self._graphic= {'black':'♕', 'white':'♛'}
        self._piece= piece
        self._links= {'diagpp':[], 'diagnp':[], 'diagnn':[], 'diagpn':[], 'above':[], 'below':[], 'right':[], 'left':[]}
        super().__init__(self._graphic, self._piece, self._links)

class Knight():
    def __init__(self, piece):
        self._graphic= {'black':'♘', 'white':'♞'}
        self._piece= piece
        self._playing= True

    def getMoves(self):
        self._links= {'abover':['above','diagpp'], 'abovel':['above','diagnp'], 'belowl':['below','diagnn'], 'belowr':['below','diagpn'], 'righta':['right','diagpp'], 'lefta':['left','diagnp'], 'leftb':['left','diagnn'], 'rightn':['right','diagpn']}
        self._pLinks= self._piece._square._links
        for link in self._links.keys():
            linkV= self._links[link]
            second= None
            first= self._piece._square._links[linkV[0]]
            if first:
                second= first._links[linkV[1]]
            if second:
                if second._piece._player._number== self._piece._player._number and second._piece._piece._playing:
                    second= None
            self._links[link]= second
        return list(self._links.values())

class Empty:
    def __init__(self, piece):
        self._graphic= {'black':None, 'white':None}
        self._piece= piece; self._playing= False        