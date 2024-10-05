# 4x4 Silverman Chess

### Project Title:
4x4 Silverman Chess

### Description:
This project is a simplified chess game with a 4x4 board, focusing on two players playing with fewer pieces than standard chess. The game is built using Python, leveraging the `customtkinter` library for the graphical interface. It implements a variety of chess pieces, each with unique movement rules, and incorporates core Object-Oriented Programming (OOP) concepts such as inheritance, polymorphism, and encapsulation. The `Square` class uses linked lists to represent connections between different board squares, and recursion is employed in calculating the valid moves for chess pieces, especially in `LongRange` and `ShortRange` classes.

---

## Classes, Attributes, and Methods:

### 1. **Square**  
- **Attributes**:  
  - `data`: Square data (coordinates and color).
  - `board`: The board to which the square belongs.
  - `piece`: The chess piece currently on the square.
  - `links`: A dictionary representing connections to other squares (linked list structure).
  
- **Methods**:  
  - `createSquare()`: Creates the square's button representation on the board.
  - `reverseLinks()`: Reverses the linked list of square connections.
  - `movePiece()`: Moves a chess piece to the square.
  - `getMoves()`: Retrieves available moves for a piece on the square.

### 2. **Piece**  
- **Attributes**:  
  - `player`: The player who owns the piece.
  - `piece`: The specific chess piece object (King, Pawn, etc.).
  - `square`: The square where the piece is located.
  - `color`: The piece's color based on the player.
  - `graphic`: The visual representation of the piece.
  
- **Methods**:  
  - Constructor that sets the piece's type, player, and square, and adds the piece to the player's list.

### 3. **Player**  
- **Attributes**:  
  - `number`: The player's unique number (0 or 1).
  - `board`: The board the player is interacting with.
  - `disableColor`: The color when the player cannot move.
  - `color`: The player's assigned piece color.
  - `pieces`: A list of all the player's chess pieces.
  
- **Methods**:  
  - Constructor that initializes a player with a number and board.

### 4. **Board**  
- **Attributes**:  
  - `squaresData`: Information on all the squares (coordinates, color, and links).
  - `pieceTypes`: Types of chess pieces.
  - `board`: The main `customtkinter` window.
  - `players`: A list containing the two players.
  - `squares`: A list of all squares on the board.
  - `moving`: A flag indicating whether a piece is being moved.
  - `chosen`: The selected square for the current move.
  - `turn`: Keeps track of whose turn it is.
  
- **Methods**:  
  - `createPieces()`: Creates chess pieces on the board.
  - `linkSquares()`: Establishes links between squares.
  - `createSquares()`: Initializes and positions squares on the board.

### 5. **ShortRange (Base class for King and Pawn)**  
- **Attributes**:  
  - `graphic`: Visual representation of the piece.
  - `piece`: The associated chess piece.
  - `links`: Available movement directions for short-range pieces (King, Pawn).
  - `playing`: A flag indicating if the piece is active.
  
- **Methods**:  
  - `getSquares()`: Recursively checks valid movement in one step for short-range pieces.
  - `getMoves()`: Calculates the available moves based on the piece's position.

### 6. **LongRange (Base class for Castle, Bishop, Queen)**  
- **Attributes**:  
  - `graphic`: Visual representation of the piece.
  - `piece`: The associated chess piece.
  - `links`: Available movement directions for long-range pieces (Castle, Bishop, Queen).
  - `playing`: A flag indicating if the piece is active.
  
- **Methods**:  
  - `getSquares()`: Recursively explores multiple squares along a direction for long-range pieces.
  - `getMoves()`: Calculates valid moves for long-range pieces by traversing the board.

### 7. **King** (Inherits from `ShortRange`)  
- **Attributes**:  
  - Inherits from `ShortRange` and defines movement in all 8 directions (diagonal, vertical, horizontal).
  
### 8. **Pawn** (Inherits from `ShortRange`)  
- **Attributes**:  
  - Inherits from `ShortRange` with movement restricted to one square forward and diagonal captures.

### 9. **Castle** (Inherits from `LongRange`)  
- **Attributes**:  
  - Inherits from `LongRange` with movement restricted to vertical and horizontal directions.

### 10. **Bishop** (Inherits from `LongRange`)  
- **Attributes**:  
  - Inherits from `LongRange` with movement restricted to diagonal directions.

### 11. **Queen** (Inherits from `LongRange`)  
- **Attributes**:  
  - Inherits from `LongRange` with movement in all directions (vertical, horizontal, diagonal).

### 12. **Empty**  
- **Attributes**:  
  - `graphic`: Representation for an empty square.
  - `piece`: A flag to indicate no piece is occupying this square.
  - `playing`: Always set to `False`.

---

## OOP Concepts Utilized:

### 1. **Encapsulation**  
Each class encapsulates its related attributes and methods, ensuring data is only modified through controlled access. For example, `Square` objects maintain their state (position, piece) and behavior (movement logic) independently.

### 2. **Inheritance**  
The `ShortRange` and `LongRange` classes serve as base classes, encapsulating shared logic for the movement of short-range and long-range chess pieces, respectively. Classes like `King`, `Pawn`, `Castle`, and `Bishop` inherit from these base classes, extending and specializing their functionality.

### 3. **Polymorphism**  
The game supports polymorphism through the way pieces of different types (like `King`, `Pawn`, `Castle`, etc.) can all be managed by the same board interface and `Square` class. This allows handling a variety of objects that follow the same interface but behave differently based on their type.

### 4. **Linked Lists in `Square` Class**  
The `Square` class uses a linked list structure to maintain references to neighboring squares on the board. Each square holds a dictionary of links (`left`, `right`, `above`, etc.) that point to adjacent squares, making the board connections dynamic and flexible for move calculations.

### 5. **Recursion in Movement Logic**  
Both `ShortRange` and `LongRange` classes use recursion to explore possible moves. In `LongRange`, recursion allows the piece to traverse multiple squares along a path (e.g., bishops moving diagonally), while `ShortRange` uses a simpler form of recursion to check adjacent squares.
