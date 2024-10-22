import customtkinter as ctk
from Moves import Pawn, King, Rook, Bishop, Knight, Queen, Empty
class Square:
    def __init__(self, data, board):
        self._data= data #includes color, coordinate
        self._board= board
        self._piece= None        
        self._links= {'diagnp':None,'above':None,'diagpp':None,
                     'left':None,'right':None,
                     'diagnn':None,'below':None,'diagpn':None}

    def createSquare(self):
        self._square= ctk.CTkButton(self._board._board,width=100, height=100, text=self._piece._graphic, text_color= self._piece._color, font= ctk.CTkFont(size=45), fg_color= self._data['color'], hover_color= '#94b06c', text_color_disabled= self._piece._player._disableColor,corner_radius= 2,command= lambda: self.getMoves())
        self._square.place(relx= self._data['x'], rely=self._data['y'])

    def reverseLinks(self):
        linksCopy= list(self._links.values())[:]
        linksCopy.reverse()
        links= list(self._links.keys())
        for l in range(len(linksCopy)):
            self._links[links[l]]= linksCopy[l] 

    def movePiece(self):          
        self._piece = Piece(type(self._board._chosen._piece._piece), self._board._chosen._piece._player, self)        
        self._board._chosen._piece._piece = Empty(self._board._chosen._piece)
        self._board._chosen._piece._graphic = None
        if (self._piece._graphic== '♙') or (self._piece._graphic== '♟'):
            self._piece= self._piece._piece.checkAscend()         
        self._board._turn= 1-self._board._turn        

    def getMoves(self):               
        if self._piece._piece._playing and not self._board._moving:
            if not self._board._turn:
                self._board._turn= self._piece._player._number
            self._board._chosen= self
            moves= self._piece._piece.getMoves()
            self._board._moving= True
            for square in self._board._squares:
                square._square.configure(state= 'disabled')
                if (square in moves):
                    square._square.configure(fg_color= '#2a933f', state= 'normal')
                if (square==self):
                    square._square.configure(fg_color= 'grey', state= 'normal')
        elif self._board._moving:
            if self != self._board._chosen:
                self.movePiece()            
            self._board._moving= False
            for square in self._board._squares:
                square._square.configure(fg_color= square._data['color'], text=square._piece._graphic, text_color= square._piece._color)
                if square._piece._player._number== self._board._turn:
                    square._square.configure(state= 'normal')
                else:
                    square._square.configure(state= 'disabled')        

class Piece:
    def __init__(self, name, player, square):        
        self._player= player
        self._square= square
        self._piece= name(self)        
        self._color= self._player._color
        self._graphic= self._piece._graphic[self._color]             
        self._square._piece= self
        self._square.createSquare()        
        self._player._pieces.append(self)

class Player:
    def __init__(self, number, board):
        self._number= number
        self._board= board
        self._disableColors= ['#979795','#343433']
        self._disableColor= self._disableColors[self._number]
        self._colors= ['white','black']
        self._color= self._colors[self._number]
        self._pieces= []

class Board:
    def __init__(self, squaresData, pieceTypes):
        self._squaresData= squaresData
        self._pieceTypes= pieceTypes
        self._board= ctk.CTk(); self._board.geometry('500x600'); self._board.title('4x5 Silverman Chess') #create the ui board        
        self._players= [Player(n, self) for n in range(2)] #create 2 players with unique numbers
        self._squares= []
        self._moving= False
        self._chosen= None
        self._turn= None

    def createPieces(self):
        for p in range(len(self._pieceTypes)):
            pieceType= self._pieceTypes[p]            
            square= self._squares[p]
            if p<=14:
                player= self._players[0]
                Piece(pieceType, player, square)
            if p>=15:
                player= self._players[1]
                Piece(pieceType, player, square)

    def linkSquares(self):
        for squareData in self._squaresData:            
            linkOrder= ['diagnp','above','diagpp',   'left','right',   'diagnn','below','diagpn']        
            links= squareData['links']
            square= squareData['square']
            for l in range(len(links)):
                link= links[l]
                next_link= linkOrder[l] # uses the links index so that it can get its corresponding name in the linkOrder list
                if link!=None:
                    square_link= self._squares[link]
                    square._links[next_link]= square_link
        self.createPieces()

    def createSquares(self):
        for squareData in self._squaresData:
            squareInd= self._squaresData.index(squareData) 
            squareData['ind']= squareInd
            new_square= Square(squareData, self)
            squareData['square']= new_square
            self._squares.append(new_square)
        self.linkSquares()

pieceTypes = [
    Rook, Bishop, Queen, King, Knight, 
    Pawn, Pawn, Pawn, Pawn, Pawn, 
    Empty, Empty, Empty, Empty, Empty,
    Empty, Empty, Empty, Empty, Empty,
    Pawn, Pawn, Pawn, Pawn, Pawn, 
    Rook, Bishop, Queen, King, Knight
]

n = None
lb = '#bfa179'
db = '#895a2e'
squaresData = [
    {'x': 0.00, 'y': 0.00, 'color': lb, 'links': [n, n, n, n, 1, n, 5, 6]},      {'x': 0.20, 'y': 0.00, 'color': db, 'links': [n, n, n, 0, 2, 5, 6, 7]},         {'x': 0.40, 'y': 0.00, 'color': lb, 'links': [n, n, n, 1, 3, 6, 7, 8]},         {'x': 0.60, 'y': 0.00, 'color': db, 'links': [n, n, n, 2, 4, 7, 8, 9]},         {'x': 0.80, 'y': 0.00, 'color': lb, 'links': [n, n, n, 3, n, 8, 9, n]},
    {'x': 0.00, 'y': 0.167, 'color': db, 'links': [n, 0, 1, n, 6, n, 10, 11]},   {'x': 0.20, 'y': 0.167, 'color': lb, 'links': [0, 1, 2, 5, 7, 10, 11, 12]},     {'x': 0.40, 'y': 0.167, 'color': db, 'links': [1, 2, 3, 6, 8, 11, 12, 13]},     {'x': 0.60, 'y': 0.167, 'color': lb, 'links': [2, 3, 4, 7, 9, 12, 13, 14]},     {'x': 0.80, 'y': 0.167, 'color': db, 'links': [3, 4, n, 8, n, 13, 14, n]},
    {'x': 0.00, 'y': 0.333, 'color': lb, 'links': [n, 5, 6, n, 11, n, 15, 16]},  {'x': 0.20, 'y': 0.333, 'color': db, 'links': [5, 6, 7, 10, 12, 15, 16, 17]},   {'x': 0.40, 'y': 0.333, 'color': lb, 'links': [6, 7, 8, 11, 13, 16, 17, 18]},   {'x': 0.60, 'y': 0.333, 'color': db, 'links': [7, 8, 9, 12, 14, 17, 18, 19]},   {'x': 0.80, 'y': 0.333, 'color': lb, 'links': [8, 9, n, 13, n, 18, 19, n]},
    {'x': 0.00, 'y': 0.500, 'color': db, 'links': [n, 10, 11, n, 16, n, 20, 21]},{'x': 0.20, 'y': 0.500, 'color': lb, 'links': [10, 11, 12, 15, 17, 20, 21, 22]},{'x': 0.40, 'y': 0.500, 'color': db, 'links': [11, 12, 13, 16, 18, 21, 22, 23]},{'x': 0.60, 'y': 0.500, 'color': lb, 'links': [12, 13, 14, 17, 19, 22, 23, 24]},{'x': 0.80, 'y': 0.500, 'color': db, 'links': [13, 14, n, 18, n, 23, 24, n]},
    {'x': 0.00, 'y': 0.667, 'color': lb, 'links': [n, 15, 16, n, 21, n, 25, 26]},{'x': 0.20, 'y': 0.667, 'color': db, 'links': [15, 16, 17, 20, 22, 25, 26, 27]},{'x': 0.40, 'y': 0.667, 'color': lb, 'links': [16, 17, 18, 21, 23, 26, 27, 28]},{'x': 0.60, 'y': 0.667, 'color': db, 'links': [17, 18, 19, 22, 24, 27, 28, 29]},{'x': 0.80, 'y': 0.667, 'color': lb, 'links': [18, 19, n, 23, n, 28, 29, n]},
    {'x': 0.00, 'y': 0.833, 'color': db, 'links': [n, 20, 21, n, 26, n, n, n]},  {'x': 0.20, 'y': 0.833, 'color': lb, 'links': [20, 21, 22, 25, 27, n, n, n]},   {'x': 0.40, 'y': 0.833, 'color': db, 'links': [21, 22, 23, 26, 28, n, n, n]},   {'x': 0.60, 'y': 0.833, 'color': lb, 'links': [22, 23, 24, 27, 29, n, n, n]},   {'x': 0.80, 'y': 0.833, 'color': db, 'links': [23, 24, n, 28, n, n, n, n]}
]
board1= Board(squaresData, pieceTypes)
board1.createSquares()
board1._board.mainloop()
