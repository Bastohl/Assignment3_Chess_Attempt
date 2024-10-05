import customtkinter as ctk
from moves2 import Pawn, King, Castle, Bishop, Queen, Empty
class Square:
    def __init__(self, data, board):
        self.data= data #includes color, coordinate
        self.board= board
        self.piece= None        
        self.links= {'diagnp':None, 'above':None, 'diagpp':None,
                       'left':None,               'right':None,
                     'diagnn':None, 'below':None, 'diagpn':None}

    def createSquare(self):
        self.square= ctk.CTkButton(self.board.board,
                                   width=90, height=90, 
                                   text=self.piece.graphic, text_color= self.piece.color, font= ctk.CTkFont(size=40), 
                                   fg_color= self.data['color'], hover_color= '#94b06c', text_color_disabled= self.piece.player.disableColor,
                                   corner_radius= 3.5,
                                   command= lambda: self.getMoves())
        self.square.place(relx= self.data['x'], rely=self.data['y'])

    def reverseLinks(self):
        linksCopy= list(self.links.values())[:]
        linksCopy.reverse()
        links= list(self.links.keys())
        for l in range(len(linksCopy)):
            self.links[links[l]]= linksCopy[l] 

    def movePiece(self):        
        self.piece = Piece(type(self.board.chosen.piece.piece), self.board.chosen.piece.player, self)        
        self.board.chosen.piece.piece = Empty(self.board.chosen.piece)
        self.board.chosen.piece.graphic = None
        self.board.turn= 1-self.board.turn

    def getMoves(self):
        if self.piece.piece.playing and not self.board.moving:
            if not self.board.turn:
                self.board.turn= self.piece.player.number
            self.board.chosen= self
            moves= self.piece.piece.getMoves()
            self.board.moving= True
            for square in self.board.squares:
                square.square.configure(state= 'disabled')
                if (square in moves):
                    square.square.configure(fg_color= 'green', state= 'normal')
                if (square==self):
                    square.square.configure(fg_color= 'grey', state= 'normal')
        elif self.board.moving:
            if self != self.board.chosen:
                self.movePiece()
            self.board.moving= False
            for square in self.board.squares:
                square.square.configure(fg_color= square.data['color'], text=square.piece.graphic, text_color= square.piece.color)
                if square.piece.player.number== self.board.turn:
                    square.square.configure(state= 'normal')
                else:
                    square.square.configure(state= 'disabled')

class Piece:
    def __init__(self, name, player, square):        
        self.player= player
        self.piece= name(self)
        self.square= square
        self.color= self.player.color
        self.graphic= self.piece.graphic[self.color]             
        self.square.piece= self
        self.square.createSquare()        
        self.player.pieces.append(self)

class Player:
    def __init__(self, number, board):
        self.number= number
        self.board= board
        self.disableColors= ['#979795','#343433']
        self.disableColor= self.disableColors[self.number]
        self.colors= ['white','black']
        self.color= self.colors[self.number]
        self.pieces= []

class Board:
    def __init__(self, squaresData, pieceTypes):
        self.squaresData= squaresData
        self.pieceTypes= pieceTypes
        self.board= ctk.CTk(); self.board.geometry('360x450'); self.board.title('4x4 Silverman Chess') #create the ui board        
        self.players= [Player(n, self) for n in range(2)] #create 2 players with unique numbers
        self.squares= []
        self.moving= False
        self.chosen= None
        self.turn= None

    def createPieces(self):
        for p in range(len(self.pieceTypes)):
            pieceType= self.pieceTypes[p]            
            square= self.squares[p]
            if p<=9:
                player= self.players[0]
                Piece(pieceType, player, square)
            if p>=10:
                player= self.players[1]
                Piece(pieceType, player, square)

    def linkSquares(self):
        for squareData in self.squaresData:            
            linkOrder= ['diagnp','above','diagpp',   'left','right',   'diagnn','below','diagpn']        
            links= squareData['links']
            square= squareData['square']
            for l in range(len(links)):
                link= links[l]
                next_link= linkOrder[l] # uses the links index so that it can get its corresponding name in the linkOrder list
                if link:
                    square_link= self.squares[link]
                    square.links[next_link]= square_link
        self.createPieces()

    def createSquares(self):
        for squareData in self.squaresData:
            squareInd= self.squaresData.index(squareData) 
            squareData['ind']= squareInd
            new_square= Square(squareData, self)
            squareData['square']= new_square
            self.squares.append(new_square)
        self.linkSquares()

pieceTypes= [Bishop, Queen, King, Castle,
             Pawn, Pawn, Pawn, Pawn,
             Empty,Empty,Empty,Empty,
             Pawn, Pawn, Pawn, Pawn,
             Bishop, Queen, King, Castle]
n= None; lb= '#c6947a'; db= '#7c4529'
squaresData= [{'x':0, 'y':0.00, 'color':lb, 'links':[n,n,n,  n,1, n,4,5]},   {'x':0.25, 'y':0.00, 'color':db, 'links':[n,n,n, 0,2, 4,5,6]},     {'x':0.50, 'y':0.00, 'color':lb, 'links':[n,n,n, 1,3, 5,6,7]},     {'x':0.75, 'y':0.00, 'color':db, 'links':[n,n,n, 2,n, 6,7,n]},
              {'x':0, 'y':0.20, 'color':db, 'links':[n,0,1,  n,5, n,8,9]},   {'x':0.25, 'y':0.20, 'color':lb, 'links':[0,1,2, 4,6, 8,9,10]},    {'x':0.50, 'y':0.20, 'color':db, 'links':[1,2,3, 5,7, 9,10,11]},   {'x':0.75, 'y':0.20, 'color':lb, 'links':[2,3,n, 6,n, 10,11,n]},
              {'x':0, 'y':0.40, 'color':lb, 'links':[n,4,5,  n,9, n,12,13]}, {'x':0.25, 'y':0.40, 'color':db, 'links':[4,5,6, 8,10, 12,13,14]}, {'x':0.50, 'y':0.40, 'color':lb, 'links':[5,6,7, 9,11, 13,14,15]}, {'x':0.75, 'y':0.40, 'color':db, 'links':[6,7,n, 10,n, 14,15,n]},
              {'x':0, 'y':0.60, 'color':db, 'links':[n,8,9,  n,13, n,16,17]}, {'x':0.25, 'y':0.60, 'color':lb, 'links':[8,9,10, 12,14, 16,17,18]}, {'x':0.50, 'y':0.60, 'color':db, 'links':[9,10,11, 13,15, 17,18,19]}, {'x':0.75, 'y':0.60, 'color':lb, 'links':[10,11,n, 14,n, 18,19,n]},
              {'x':0, 'y':0.80, 'color':lb, 'links':[n,12,13, n,18, n,n,n]},   {'x':0.25, 'y':0.80, 'color':db, 'links':[12,13,14, 16,18, n,n,n]},  {'x':0.50, 'y':0.80, 'color':lb, 'links':[13,14,15, 17,19, n,n,n]}, {'x':0.75, 'y':0.80, 'color':db, 'links':[14,15,n, 18,n, n,n,n]}]

board1= Board(squaresData, pieceTypes)
board1.createSquares()
board1.board.mainloop()
