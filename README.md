# 4x4 Silverman Chess - Implementation Process

## Overview

This project is a custom chess implementation using Python and the `customtkinter` library to create a 4x4 version of chess, often referred to as Silverman Chess. The chess game features standard chess pieces (King, Queen, Castle, and Pawn), with moves governed by the same rules but adapted for a smaller board size. This README describes the step-by-step process involved in the development of the game.

---

## Implementation Process

### 1. **Setting Up the Game Board**
   - The `Board` class is responsible for creating the game window and board. The board size is set to 400x400 pixels, making it appropriate for the 4x4 grid.
   - We store the board structure in `squaresData`, which contains the coordinates and link information for each square.
     - Each square is assigned its color (`#c6947a` for light brown and `#7c4529` for dark brown) and relative positions (using `relx` and `rely` for placement).
     - Each square has "links" connecting it to neighboring squares, facilitating piece movement logic.

### 2. **Square Class**
   - The `Square` class represents each square on the board. Each square:
     - Contains metadata such as color, coordinates, and links to its neighboring squares.
     - Has a `piece` attribute that stores the current piece on that square (if any).
     - The `createSquare()` method creates a `CTkButton` for each square and places it on the window.
     - The `reverseLinks()` function handles movement direction when a piece needs to evaluate possible moves backward or diagonally.

### 3. **Piece Class and Inheritance Structure**
   - The `Piece` class is the base class for all chess pieces. It:
     - Tracks the player (white or black) who owns the piece.
     - Stores the piece’s current square and the graphic (e.g., "♚" for the white king).
     - Uses inheritance to differentiate between different piece types, as follows:
       - **King** and **Pawn** are handled by `ShortRange` (movement is limited to one square in any direction).
       - **Castle** and **Queen** are handled by `LongRange` (pieces can move across multiple squares).
       - `Empty` pieces represent squares that are empty or occupied by a non-playing piece.

### 4. **ShortRange and LongRange Movement Logic**
   - `ShortRange` and `LongRange` classes are used to manage movement.
     - **ShortRange:** Handles the King and Pawn. These pieces can only move to adjacent squares or capture diagonally (Pawns). The movement rules are defined through the `getMoves()` and `getSquares()` methods.
     - **LongRange:** Handles the Castle and Queen. These pieces can move multiple squares along a straight line or diagonally. They evaluate possible moves by recursively checking links to further squares.

### 5. **Player Class**
   - The `Player` class is responsible for tracking players, their pieces, and their color assignments (either black or white).
   - Each player is initialized with a unique number (0 or 1) to differentiate their turns and control piece movements.

### 6. **Piece Movement**
   - The game logic for moving pieces is embedded in the `getMoves()` and `movePiece()` methods.
   - When a player clicks a piece, the game evaluates possible moves for that piece based on its type.
   - All squares are temporarily disabled, and only valid moves are enabled for the player to choose.
   - When a player selects a new square, the piece is moved there, and the turn is passed to the next player.

### 7. **Linking Squares**
   - The `linkSquares()` method establishes the connections between neighboring squares, ensuring that pieces can move in all allowed directions (diagonally, horizontally, vertically).
   - For instance, the top-left square is connected to its adjacent squares via keys like `'diagpp'` (diagonally up and right) or `'below'` (directly below).

### 8. **Creating and Placing Pieces**
   - The `createPieces()` method initializes the pieces on the board at the start of the game.
     - The first 8 squares are populated with white pieces, and the last 8 squares are filled with black pieces.
     - Each square gets a `Piece` object, which assigns a `graphic` (e.g., "♕" for the white queen) and a color.

### 9. **User Interaction**
   - The user interacts with the game through `CTkButton` elements that act as squares on the board.
   - When a square is clicked, the board evaluates whether a valid move can be made.
   - If the move is valid, the piece moves, and the UI updates to reflect the new state (with new piece locations and color changes for the next turn).

---

## Conclusion

The Silverman Chess game implementation is built using object-oriented programming principles. Classes like `Board`, `Square`, `Piece`, `Player`, `ShortRange`, and `LongRange` break down the game's logic into manageable units. The `customtkinter` library is used to create a graphical interface for the board and squares. This 4x4 chess version is simplified but retains essential chess rules for gameplay.
