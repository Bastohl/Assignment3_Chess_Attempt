class ShortRange:
    def __init__(self, graphic, piece, links):
        self.graphic= graphic
        self.piece= piece
        self.links= links
        self.playing= True

    def getSquares(self, square):  
        samePlayer= False
        opponentPlayer= False
        if square!=None and square.piece:
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

    def checkAscend(self):
        if (self.piece.square.board.squares.index(self.piece.square)<4 and self.piece.square.board.turn==1) or (self.piece.square.board.squares.index(self.piece.square)>24 and self.piece.square.board.turn==0):
            self.piece.piece= Queen(self.piece)
            self.piece.graphic= self.piece.piece.graphic[self.piece.color]
        return self.piece

class LongRange:
    def __init__(self, graphic, piece, links):
        self.graphic= graphic
        self.piece= piece
        self.links= links
        self.playing= True

    def getSquares(self, square):
        samePlayer= False
        opponentPlayer= False
        if square!=None and square.piece:      
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

class Rook(LongRange):
    def __init__(self, piece):
        self.graphic= {'black':'♖', 'white':'♜'}
        self.piece= piece
        self.links= {'above':[], 'below':[], 'right':[], 'left':[]}
        super().__init__(self.graphic, self.piece, self.links)

class Bishop(LongRange):
    def __init__(self, piece):
        self.graphic= {'black':'♗', 'white':'♝'}
        self.piece= piece
        self.links= {'diagpp':[], 'diagnp':[], 'diagnn':[], 'diagpn':[]}
        super().__init__(self.graphic, self.piece, self.links)

class Queen(LongRange):
    def __init__(self, piece):
        self.graphic= {'black':'♕', 'white':'♛'}
        self.piece= piece
        self.links= {'diagpp':[], 'diagnp':[], 'diagnn':[], 'diagpn':[], 'above':[], 'below':[], 'right':[], 'left':[]}
        super().__init__(self.graphic, self.piece, self.links)

class Knight():
    def __init__(self, piece):
        self.graphic= {'black':'♘', 'white':'♞'}
        self.piece= piece
        self.playing= True

    def getMoves(self):
        self.links= {'abover':['above','diagpp'], 'abovel':['above','diagnp'], 'belowl':['below','diagnn'], 'belowr':['below','diagpn'], 'righta':['right','diagpp'], 'lefta':['left','diagnp'], 'leftb':['left','diagnn'], 'rightn':['right','diagpn']}
        self.pLinks= self.piece.square.links
        for link in self.links.keys():
            linkV= self.links[link]
            second= None
            first= self.piece.square.links[linkV[0]]
            if first:
                second= first.links[linkV[1]]
            if second:
                if second.piece.player.number== self.piece.player.number and second.piece.piece.playing:
                    second= None
            self.links[link]= second
        return list(self.links.values())

class Empty:
    def __init__(self, piece):
        self.graphic= {'black':None, 'white':None}
        self.piece= piece; self.playing= False        