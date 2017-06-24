# TicTacAPI - Python Engine for TicTacToe
Design/API
## Classes
 ----------------------------------------------------------
### User
#### Variables
 
**uid**

Type : uuid4() 

Description: Unique identifier representing a user. This could also allow for long term user storage and username reuse    
name
    Type: string
    Description: Username for the user
 
 
Methods
 
__init__
    Parameters:
 string: name
 
getUserDict
    Description: Returns a dictionary representation of the object.
    Return:
        Dict: user
 
 
getId
Description: Returns the object’s uid
    Return:
        UUID: uid
 
getName
Description: Returns the object’s name
    Return:
        String : name
 

 
 
 
Board
 
Variables
 
uid
Type : uuid4() 
Description: Unique identifier representing a board. This could also allow for long term 
board storage, game replayability, and game review
 
available_moves
Type : list 
Description: List of moves (total 9) that can be marked as the move is made to 
track available playable positions on the board
 
Slices
    Type: dict
    Description: Dictionary of lists that represent the vertical, horizontal, and diagonal slices 
            of the board
 
Methods
 
__init__
Parameters:
 Dict : Dictionary representing the board 
 
getId
Description: Returns the object’s uid
    Return:
        UUID
 
 
 
updateAvailable_moves
    Parameters:
        Int: position
    Return:
        Boolean 
    Description:
        Takes the integer position of the proposed player move checks to see if the 
position is free. If the position is free, method will mark it and return True. If the 
position is already played the method will return False
    
getAvailable_moves
    Return:
        List
    Description:
        Return a list of available playable positions on the board
 
setSlice
    Parameters:
        UUID: uid
        Int: slice mode
        Int: slice position index
    Description:
        Updates the slice list of the given index under the following conditions    
If the list is in the [0,0] form the index [0] will be updated with the supplied UID and the index [1] will be set to 1
If the list has a UID in index [0] and the uid provided matches the current uid, then index [1] will be incremented by 1
If the list has a UID in index [0] and the uid provided matches the current uid, then the list will be set to [-1,-1]
If the list has -1 in index [0] skip the operation
    
 
getVertical
    Parameters:
        Int: Vertical Position index
Return:
List
Description:
Return the list at the position index provided
 
getHorizontal
    Parameters:
        Int: Horizontal Position index
Return:
List
Description:
Return the list at the position index provided
 
getDiagonal
    Parameters:
        Int: Diagonal Position index
Return:
List
Description:
Return the list at the position index provided
 
 
 
checkWin
    Return:
        Boolean
    Description:
        Checks over all of the horizontal, vertical, and diagonal lists and checks for an 
Index [1] with the value three. If the value in index [0] is -1 the list in the index is skipped
 
 
 
setPiece
    Parameters: 
Int:  board position 1-9
User: user
    Description:
        Takes the board position and populates the appropriate slices using a move 
dictionary
 
 
---------------------------------
 
Game
 
Variables
 
game_uid
Type : uuid4() 
Description: Unique identifier representing a Game. This could also allow for long term 
game storage, game replayability, and game review
 
Users
    Type: list
    Description: List of User objects representing the game players
 
state
    Type: int
    Description: Integer that represents the three states of the game:
        0 - Wating for player
        1 - Player 1 move
        2 - Player 2 move
        3 - Game Over
 
Board
    Type: Board
    Description: Board object containing the current board state
 
 
Methods
 
__init__
Parameters:
 Dict : Dictionary representing the game
 
getId
Description: Returns the object’s uid
    Return:
        UUID
 
move
    Parameters: 
        Int: board index
    Description: uses a numerical index representing a space on the board and a player to                 Update the board and change the state of the game. Checks for a win. Swaps player 
        and returns user if no win     
Return:
        Boolean if false || UID if true
