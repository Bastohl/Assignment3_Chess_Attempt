class ShortRange:
    def __init__(self, graphic, piece, links):
        self.graphic= graphic
        self.piece= piece
        self.links= links
        self.playing= True

    def getSquares(self, square):  
        samePlayer= False
        opponentPlayer= False
        if square and square.piece:
            samePlayer= (square.piece.player.number == self.piece.player.number) and (square.piece.piece.playing)
            opponentPlayer= (square.piece.player.number != self.piece.player.number) and (square.piece.piece.playing)
        outsideBoard= (not square)
        if outsideBoard or samePlayer or (opponentPlayer and self.link==self.condition1) or (self.link in self.condition2 and not square.piece.piece.playing):
            pass
        else:
            self.links[self.link]= square

    def getMoves(self):
        for link in list(self.links.keys()):
            self.links[link]= None
            self.link= link
            square= self.piece.square.links[self.link]            
            self.getSquares(square)
        moves= []
        for link in self.links.values():
            if link:
                moves.append(link)
        return moves

class King(ShortRange):
    def __init__(self, piece):
        self.graphic= {'black':'♔', 'white':'♚'}
        self.piece= piece
        self.links= {'diagpp':0, 'diagnp':0, 'diagnn':0, 'diagpn':0, 'above':0, 'below':0, 'right':0, 'left':0}
        self.condition1= None
        self.condition2= [None,None]
        super().__init__(self.graphic, self.piece, self.links)

class Pawn(ShortRange):
    def __init__(self, piece):
        self.graphic= {'black':'♙', 'white':'♟'}
        self.piece= piece
        self.links= [{'diagpn':0, 'diagnn':0, 'below':0}, {'diagpp':0, 'diagnp':0, 'above':0}]
        self.condition1= ['below','above'][self.piece.player.number]
        self.condition2= [['diagnn','diagpn'], ['diagnp','diagpp']][self.piece.player.number]
        super().__init__(self.graphic, self.piece, self.links[self.piece.player.number])

class LongRange:
    def __init__(self, graphic, piece, links):
        self.graphic= graphic
        self.piece= piece
        self.links= links
        self.playing= True

    def getSquares(self, square):
        samePlayer= False
        opponentPlayer= False
        if square and square.piece:      
            samePlayer= (square.piece.player.number == self.piece.player.number) and (square.piece.piece.playing)
            opponentPlayer= (square.piece.player.number != self.piece.player.number) and (square.piece.piece.playing)            
        outsideBoard= (not square)        
        if outsideBoard or samePlayer:
            pass
        elif opponentPlayer:
            self.links[self.link].append(square)
        else:        
            self.links[self.link].append(square)
            self.getSquares(square.links[self.link])                

    def getMoves(self):
        for link in list(self.links.keys()):
            self.links[link]= []
            self.link= link
            square= self.piece.square.links[self.link]            
            self.getSquares(square)
        moves= []
        for link in self.links.values():
            moves.extend(link)
        return moves

class Castle(LongRange):
    def __init__(self, piece):
        self.graphic= {'black':'♖', 'white':'♜'}
        self.piece= piece
        self.links= {'above':[], 'below':[], 'right':[], 'left':[]}
        super().__init__(self.graphic, self.piece, self.links)

class Queen(LongRange):
    def __init__(self, piece):
        self.graphic= {'black':'♕', 'white':'♛'}
        self.piece= piece
        self.links= {'diagpp':[], 'diagnp':[], 'diagnn':[], 'diagpn':[], 'above':[], 'below':[], 'right':[], 'left':[]}
        super().__init__(self.graphic, self.piece, self.links)

class Empty:
    def __init__(self, piece):
        self.graphic= {'black':None, 'white':None}
        self.piece= piece; self.playing= False        